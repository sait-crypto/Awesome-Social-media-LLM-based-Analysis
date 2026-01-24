import os
import sys
import configparser
import pandas as pd
import json
import shutil
import re
from pathlib import Path

# 添加 src 到路径以便复用逻辑
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.config_loader import get_config_instance

# 使用统一的配置加载器
config_instance = get_config_instance()
settings = config_instance.settings

# 获取配置路径 (ConfigLoader 已经将它们处理为绝对路径)
UPDATE_EXCEL = settings['paths']['update_excel']
UPDATE_JSON = settings['paths']['update_json']
FIGURE_DIR = settings['paths']['figure_dir']
PROJECT_ROOT = config_instance.project_root

def get_clean_title_hash(title):
    if not title or pd.isna(title):
        return "untitled"
    # 取前8个字符，去除非法文件名字符
    clean_prefix = re.sub(r'[^a-zA-Z0-9]', '', str(title)[:8])
    return clean_prefix

def get_unique_filename(original_path, title):
    """
    生成规则: 原名-{题目前8字符}-{不冲突最小正整数}
    """
    dirname, basename = os.path.split(original_path)
    filename, ext = os.path.splitext(basename)
    
    title_part = get_clean_title_hash(title)
    
    counter = 1
    while True:
        new_basename = f"{filename}-{title_part}-{counter}{ext}"
        new_full_path = os.path.join(FIGURE_DIR, new_basename)
        if not os.path.exists(new_full_path):
            return new_full_path
        counter += 1

def process_figures():
    print(f"Processing figures in: {FIGURE_DIR}")
    
    # 确保 figures 目录存在
    if not os.path.exists(FIGURE_DIR):
        os.makedirs(FIGURE_DIR)

    # 1. 处理 Excel
    if os.path.exists(UPDATE_EXCEL):
        try:
            print(f"Checking Excel template: {UPDATE_EXCEL}")
            df = pd.read_excel(UPDATE_EXCEL, engine='openpyxl')
            updated = False
            
            # 获取配置中的列名
            # 在 tag_config.py 中 table_name 是 "pipeline figure"
            # variable 是 "pipeline_image"
            target_col = "pipeline figure" 
            title_col = "title"

            # 兼容性检查：如果找不到 pipeline figure，尝试找 pipeline_image
            if target_col not in df.columns and "pipeline_image" in df.columns:
                target_col = "pipeline_image"

            if target_col in df.columns:
                for idx, row in df.iterrows():
                    img_path_raw = row[target_col]
                    title = row.get(title_col, "unknown")
                    
                    if pd.isna(img_path_raw) or str(img_path_raw).strip() == "":
                        continue

                    img_path_str = str(img_path_raw).strip()
                    
                    # 支持多图 ; 分隔
                    paths = [p.strip() for p in re.split(r'[;；]', img_path_str) if p.strip()]
                    new_paths = []
                    row_updated = False
                        
                    for p in paths:
                        # 构造可能的绝对路径
                        # 1. 如果 p 已经是绝对路径（不太可能，但防御性编程）
                        if os.path.isabs(p):
                            full_current_path = p
                        else:
                            # 2. 尝试相对于项目根目录
                            full_current_path = os.path.join(PROJECT_ROOT, p)
                            # 3. 如果找不到，尝试相对于 figures 目录 (用户可能只写了文件名)
                            if not os.path.exists(full_current_path):
                                full_current_path = os.path.join(FIGURE_DIR, os.path.basename(p))
                        
                        # 检查文件是否存在
                        if os.path.exists(full_current_path):
                            # 生成新名字 (绝对路径)
                            new_full_path = get_unique_filename(full_current_path, title)
                            
                            # 重命名文件
                            os.rename(full_current_path, new_full_path)
                            print(f"Renamed: {os.path.basename(full_current_path)} -> {os.path.basename(new_full_path)}")
                            
                            # 计算相对路径写入 Excel (相对于项目根目录，例如 figures/new_name.png)
                            rel_path = os.path.relpath(new_full_path, PROJECT_ROOT)
                            new_paths.append(rel_path.replace('\\', '/'))
                            row_updated = True
                            updated = True
                        else:
                            print(f"Warning: Image not found: {p} (looked at {full_current_path})")
                            new_paths.append(p) # 保持原样
                    
                    # 如果有更新，写回该行
                    if row_updated:
                        df.at[idx, target_col] = ";".join(new_paths)
            
            if updated:
                # 保持表头样式（尝试保留）
                try:
                    from src.core.update_file_utils import get_update_file_utils
                    ufu = get_update_file_utils()
                    ufu.write_excel_file(UPDATE_EXCEL, df)
                    print("Excel template updated with new image paths.")
                except Exception:
                    # 回退到普通保存
                    df.to_excel(UPDATE_EXCEL, index=False, engine='openpyxl')
                    print("Excel template updated (simple save).")

        except Exception as e:
            print(f"Error processing Excel figures: {e}")
            # 不阻断流程，可能只是没图
            import traceback
            traceback.print_exc()

    # 2. 处理 JSON
    if os.path.exists(UPDATE_JSON):
        try:
            print(f"Checking JSON template: {UPDATE_JSON}")
            with open(UPDATE_JSON, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            json_updated = False
            
            # 标准化 papers 列表
            papers = []
            if isinstance(data, list):
                papers = data
            elif isinstance(data, dict) and 'papers' in data:
                papers = data['papers']
            
            for paper in papers:
                # JSON 中的键通常是 variable 名: pipeline_image
                if 'pipeline_image' in paper and paper['pipeline_image']:
                    img_path_str = str(paper['pipeline_image']).strip()
                    if not img_path_str: continue

                    title = paper.get('title', 'unknown')
                    paths = [p.strip() for p in re.split(r'[;；]', img_path_str) if p.strip()]
                    new_paths = []
                    row_updated = False

                    for p in paths:
                        # 路径逻辑同上
                        if os.path.isabs(p):
                            full_current_path = p
                        else:
                            full_current_path = os.path.join(PROJECT_ROOT, p)
                            if not os.path.exists(full_current_path):
                                full_current_path = os.path.join(FIGURE_DIR, os.path.basename(p))
                        
                        if os.path.exists(full_current_path):
                            new_full_path = get_unique_filename(full_current_path, title)
                            os.rename(full_current_path, new_full_path)
                            print(f"Renamed (JSON): {os.path.basename(full_current_path)} -> {os.path.basename(new_full_path)}")
                            
                            rel_path = os.path.relpath(new_full_path, PROJECT_ROOT)
                            new_paths.append(rel_path.replace('\\', '/'))
                            row_updated = True
                            json_updated = True
                        else:
                            new_paths.append(p)
                    
                    if row_updated:
                        paper['pipeline_image'] = ";".join(new_paths)

            if json_updated:
                with open(UPDATE_JSON, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print("JSON template updated with new image paths.")

        except Exception as e:
            print(f"Error processing JSON figures: {e}")

if __name__ == "__main__":
    process_figures()