import os
import sys
import hashlib
import configparser
import pandas as pd
import json
import shutil
import re

# 添加 src 到路径以便复用逻辑（如果需要）
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

UPDATE_EXCEL = config['paths']['update_excel']
UPDATE_JSON = config['paths']['update_json']
FIGURE_DIR = config['paths']['figure_dir']

def get_clean_title_hash(title):
    if not title:
        return "untitled"
    # 取前8个字符，去除非法文件名字符
    clean_prefix = re.sub(r'[^a-zA-Z0-9]', '', title[:8])
    return clean_prefix

def get_unique_filename(original_path, title):
    """
    生成规则: 原名-{题目前8字符}-{不冲突最小正整数}
    """
    dirname, basename = os.path.split(original_path)
    filename, ext = os.path.splitext(basename)
    
    title_part = get_clean_title_hash(title)
    
    # 基础新名字模式
    # 这里假设 original_path 是 "figures/abc.png"
    # 我们只关心文件名部分重命名
    
    counter = 1
    while True:
        new_basename = f"{filename}-{title_part}-{counter}{ext}"
        new_full_path = os.path.join(FIGURE_DIR, new_basename)
        if not os.path.exists(new_full_path):
            return new_full_path
        counter += 1

def process_figures():
    # 1. 处理 Excel
    if os.path.exists(UPDATE_EXCEL):
        try:
            df = pd.read_excel(UPDATE_EXCEL, engine='openpyxl')
            updated = False
            
            # 假设列名是 'pipeline_image' (根据你的 tag_config.py 实际情况调整)
            # 在你的 tag_config.py 中 table_name 是 "pipeline figure"，variable 是 "pipeline_image"
            # pd.read_excel 读取的是 table_name
            target_col = "pipeline figure" 
            title_col = "title"

            if target_col in df.columns:
                for idx, row in df.iterrows():
                    img_path = str(row[target_col]).strip()
                    title = str(row.get(title_col, "unknown"))
                    
                    # 检查是否包含有效图片路径 (支持多图 ; 分隔)
                    if img_path and img_path.lower() != 'nan':
                        paths = [p.strip() for p in re.split(r'[;；]', img_path) if p.strip()]
                        new_paths = []
                        
                        for p in paths:
                            # 规范化路径
                            full_current_path = p
                            # 如果用户只写了文件名，拼上目录
                            if not p.startswith(FIGURE_DIR):
                                full_current_path = os.path.join(FIGURE_DIR, p)
                            
                            # 检查文件是否存在
                            if os.path.exists(full_current_path):
                                # 生成新名字
                                new_path = get_unique_filename(full_current_path, title)
                                
                                # 重命名文件
                                os.rename(full_current_path, new_path)
                                print(f"Renamed: {full_current_path} -> {new_path}")
                                
                                # 使用相对路径存回 Excel (例如 figures/xxx.png)
                                # 确保使用正斜杠
                                new_paths.append(new_path.replace('\\', '/'))
                                updated = True
                            else:
                                print(f"Warning: Image not found {full_current_path}")
                                new_paths.append(p) # 保持原样
                        
                        # 更新 DataFrame
                        df.at[idx, target_col] = ";".join(new_paths)
            
            if updated:
                df.to_excel(UPDATE_EXCEL, index=False, engine='openpyxl')
                print("Excel template updated with new image paths.")

        except Exception as e:
            print(f"Error processing Excel figures: {e}")
            sys.exit(1)

    # 2. 处理 JSON (逻辑类似，略，根据 JSON 结构遍历)
    # 如果你也用 JSON 提交，请在此处添加 JSON 的解析和重命名逻辑

if __name__ == "__main__":
    # 确保 figures 目录存在
    if not os.path.exists(FIGURE_DIR):
        os.makedirs(FIGURE_DIR)
    process_figures()