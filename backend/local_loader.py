import os
import shutil

def load_local_documents(folder_path, target_dir='docs'):
    """
    Kopieert alle bestanden uit een lokale map (inclusief submappen) naar de docs directory.
    """
    os.makedirs(target_dir, exist_ok=True)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            src = os.path.join(root, file)
            rel = os.path.relpath(src, folder_path)
            dst = os.path.join(target_dir, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
