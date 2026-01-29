import os
import sys
import hashlib
import configparser
import pandas as pd
import json
import shutil
import re
from pathlib import Path

# Add src to path to import config_loader
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.core.config_loader import get_config_instance

config_instance = get_config_instance()
settings = config_instance.settings

# Path Configuration (Absolute Paths)
PROJECT_ROOT = str(config_instance.project_root)
UPDATE_EXCEL = str(Path(settings['paths']['update_excel']).resolve())
UPDATE_JSON = str(Path(settings['paths']['update_json']).resolve())

# Target Directory (Main Branch Figures - Final Destination)
FIGURE_DIR_REL = settings['paths']['figure_dir']
FIGURE_DIR = str(Path(PROJECT_ROOT) / FIGURE_DIR_REL)

# Source Directory (PR Branch Figures - Staging Area)
# Passed via env var from GitHub Action
PR_FIGURE_DIR_ENV = os.environ.get('PR_FIGURES_DIR')
PR_FIGURE_DIR = str(Path(PR_FIGURE_DIR_ENV).resolve()) if PR_FIGURE_DIR_ENV else FIGURE_DIR

def calculate_file_hash(filepath):
    """Calculate MD5 hash of a file."""
    if not os.path.exists(filepath):
        return None
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            buf = f.read(65536)
            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(65536)
        return hasher.hexdigest()
    except Exception:
        return None

def get_clean_title_hash(title):
    if not title or pd.isna(title):
        return "untitled"
    # Keep first 8 alphanumeric chars
    clean_prefix = re.sub(r'[^a-zA-Z0-9]', '', str(title)[:8])
    return clean_prefix

def get_smart_unique_path(source_path, original_basename, title):
    """
    Determine the final destination path for an image.
    Logic:
    1. If target (original name) doesn't exist -> Use original name.
    2. If target exists and hash MATCHES -> Use original name (no rename needed).
    3. If target exists and hash DIFFERS -> Rename (Name-Title-Count.ext).
    """
    filename, ext = os.path.splitext(original_basename)
    source_hash = calculate_file_hash(source_path)
    
    # Attempt 1: Try original name
    target_path = os.path.join(FIGURE_DIR, original_basename)
    
    if not os.path.exists(target_path):
        # Target doesn't exist, safe to use
        return target_path, False
        
    # Target exists, check hash
    target_hash = calculate_file_hash(target_path)
    if source_hash == target_hash:
        print(f"  [Info] Identical image exists at {original_basename}. Using existing.")
        return target_path, False # False = No rename (conflict resolved by reuse)
    
    print(f"  [Info] Conflict detected at {original_basename} (Hash mismatch). Renaming...")
    
    # Attempt 2+: Rename logic
    title_part = get_clean_title_hash(title)
    counter = 1
    
    while True:
        new_basename = f"{filename}-{title_part}-{counter}{ext}"
        new_full_path = os.path.join(FIGURE_DIR, new_basename)
        
        if not os.path.exists(new_full_path):
            return new_full_path, True # True = Renamed
            
        # Check hash of this renamed variant too (idempotency check)
        if calculate_file_hash(new_full_path) == source_hash:
            print(f"  [Info] Identical image found at {new_basename}. Using existing.")
            return new_full_path, False
            
        counter += 1

def resolve_pr_image(p):
    """
    Locate the image provided in the template.
    Order:
    1. Check PR Staging Directory (Priority)
    2. Check Main Figures Directory (For existing images referenced in template)
    """
    basename = os.path.basename(p)
    
    # 1. Look in PR Staging
    pr_path = os.path.join(PR_FIGURE_DIR, basename)
    if os.path.exists(pr_path):
        return pr_path, True # True = Found in PR
    
    # 2. Look in Main Figures
    main_path = os.path.join(FIGURE_DIR, basename)
    if os.path.exists(main_path):
        return main_path, False # False = Found in Main
        
    # 3. Fallback: Check if p is an absolute path or relative path that works as-is
    if os.path.exists(p):
        return p, False
        
    return None, False

def process_figures():
    print(f"Processing figures.")
    print(f"  - Source (PR Temp): {PR_FIGURE_DIR}")
    print(f"  - Target (Main): {FIGURE_DIR}")
    
    if not os.path.exists(FIGURE_DIR):
        os.makedirs(FIGURE_DIR)

    # --- Process Excel ---
    if os.path.exists(UPDATE_EXCEL):
        try:
            print(f"Checking Excel template: {UPDATE_EXCEL}")
            df = pd.read_excel(UPDATE_EXCEL, engine='openpyxl')
            updated = False
            
            # Identify columns
            target_col = "pipeline figure" 
            if target_col not in df.columns and "pipeline_image" in df.columns:
                target_col = "pipeline_image"
            title_col = "title"

            if target_col in df.columns:
                for idx, row in df.iterrows():
                    img_path_raw = row[target_col]
                    title = row.get(title_col, "untitled")
                    
                    if pd.isna(img_path_raw) or str(img_path_raw).strip() == "":
                        continue

                    # Split multiple images
                    raw_paths = [p.strip() for p in re.split(r'[;；]', str(img_path_raw).strip()) if p.strip()]
                    new_relative_paths = []
                    row_dirty = False
                        
                    for p in raw_paths:
                        src_path, is_from_pr = resolve_pr_image(p)
                        
                        if src_path:
                            # Determine destination
                            dst_path, renamed = get_smart_unique_path(src_path, os.path.basename(p), title)
                            
                            # Move Logic:
                            # Only move if we are actually changing location (PR -> Main) 
                            # and the destination doesn't exist yet.
                            if os.path.abspath(src_path) != os.path.abspath(dst_path):
                                if not os.path.exists(dst_path):
                                    print(f"  [Move] {os.path.basename(src_path)} -> {os.path.basename(dst_path)}")
                                    shutil.move(src_path, dst_path)
                                else:
                                    # Destination exists (Hash match verified by get_smart_unique_path)
                                    # We can delete the temp copy in PR folder to clean up
                                    if is_from_pr:
                                        # print(f"  [Clean] Removing temp PR copy: {os.path.basename(src_path)}")
                                        os.remove(src_path)

                            # Normalize path for Excel (Relative to Project Root, Forward Slashes)
                            rel_path = os.path.relpath(dst_path, PROJECT_ROOT).replace('\\', '/')
                            
                            if rel_path != p.replace('\\', '/'):
                                row_dirty = True
                            
                            new_relative_paths.append(rel_path)
                        else:
                            print(f"Warning: Image not found anywhere: {p}")
                            new_relative_paths.append(p) # Keep original text if not found
                    
                    if row_dirty:
                        df.at[idx, target_col] = ";".join(new_relative_paths)
                        updated = True
            
            if updated:
                from src.core.update_file_utils import get_update_file_utils
                get_update_file_utils().write_excel_file(UPDATE_EXCEL, df)
                print("Excel template updated.")

        except Exception as e:
            print(f"Error processing Excel figures: {e}")
            import traceback
            traceback.print_exc()

    # --- Process JSON (Same logic) ---
    if os.path.exists(UPDATE_JSON):
        try:
            print(f"Checking JSON template: {UPDATE_JSON}")
            with open(UPDATE_JSON, 'r', encoding='utf-8') as f:
                data = json.load(f)
            json_updated = False
            
            papers = data if isinstance(data, list) else data.get('papers', [])
            for paper in papers:
                if 'pipeline_image' in paper and paper['pipeline_image']:
                    img_path_str = str(paper['pipeline_image']).strip()
                    if not img_path_str: continue
                    title = paper.get('title', 'untitled')
                    
                    raw_paths = [p.strip() for p in re.split(r'[;；]', img_path_str) if p.strip()]
                    new_relative_paths = []
                    row_dirty = False

                    for p in raw_paths:
                        src_path, is_from_pr = resolve_pr_image(p)
                        if src_path:
                            dst_path, renamed = get_smart_unique_path(src_path, os.path.basename(p), title)
                            
                            if os.path.abspath(src_path) != os.path.abspath(dst_path):
                                if not os.path.exists(dst_path):
                                    print(f"  [Move] {os.path.basename(src_path)} -> {os.path.basename(dst_path)}")
                                    shutil.move(src_path, dst_path)
                                else:
                                    if is_from_pr: os.remove(src_path)
                            
                            rel_path = os.path.relpath(dst_path, PROJECT_ROOT).replace('\\', '/')
                            if rel_path != p.replace('\\', '/'):
                                row_dirty = True
                            new_relative_paths.append(rel_path)
                        else:
                            new_relative_paths.append(p)
                    
                    if row_dirty:
                        paper['pipeline_image'] = ";".join(new_relative_paths)
                        json_updated = True

            if json_updated:
                from src.core.update_file_utils import get_update_file_utils
                get_update_file_utils().write_json_file(UPDATE_JSON, data)
                print("JSON template updated.")

        except Exception as e:
            print(f"Error processing JSON figures: {e}")

if __name__ == "__main__":
    process_figures()