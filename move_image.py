import os
import shutil

# 定義來源根資料夾和目標資料夾
source_root = "./ffhq_dataset"  # 替換為來源資料夾的父目錄
destination_folder = "./img_data"  # 替換為目標資料夾

# 確保目標資料夾存在
os.makedirs(destination_folder, exist_ok=True)

# 遍歷來源根資料夾下的所有資料夾
for folder_name in os.listdir(source_root):
    folder_path = os.path.join(source_root, folder_name)
    
    # 僅處理以 '000' 開頭的資料夾
    if os.path.isdir(folder_path) and folder_name.startswith("000"):
        for root, _, files in os.walk(folder_path):
            for file in files:
                source_file = os.path.join(root, file)  # 檔案完整路徑
                destination_file = os.path.join(destination_folder, file)  # 複製目標路徑
                
                # 檢查是否已存在重名檔案
                if os.path.exists(destination_file):
                    print(f"檔案 {destination_file} 已存在，跳過...")
                    continue
                
                # 複製檔案
                shutil.copy2(source_file, destination_file)
                print(f"已複製: {source_file} -> {destination_file}")

print("所有檔案已成功複製到目標資料夾！")
