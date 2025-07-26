import os
import shutil

def organize_by_type(folder):
    for filename in os.listdir(folder):
        if '.' in filename:
            ext = filename.split('.')[-1]
            target_dir = os.path.join(folder, ext.upper())
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(os.path.join(folder, filename), os.path.join(target_dir, filename))

organize_by_type(".")
