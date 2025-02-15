import os
import shutil

def delete_pycache_dirs(path="."):
    try:
        for root, dirs, files in os.walk(path):
            for dir_name in dirs:
                if dir_name == "__pycache__":
                    pycache_path = os.path.join(root, dir_name)
                    print(f"Removendo {pycache_path}")
                    shutil.rmtree(pycache_path)
    except Exception as e:
        pass

delete_pycache_dirs()