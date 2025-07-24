import os
import shutil
from pathlib import Path

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Code": [".py", ".js", ".html", ".css"],
    "Archives": [".zip", ".rar"],
    "Others": []
}

def organize_folder(target_folder: str):
    path = Path(target_folder)

    for file in path.iterdir():
        if file.is_file():
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if file.suffix.lower() in extensions:
                    dest_folder = path / folder
                    dest_folder.mkdir(exist_ok=True)
                    shutil.move(str(file), dest_folder / file.name)
                    moved = True
                    break

            if not moved:
                other_folder = path / "Others"
                other_folder.mkdir(exist_ok=True)
                shutil.move(str(file), other_folder / file.name)



if __name__ == "__main__":
    folder_to_organize = input("Enter the full path of folder to organize: ")
    organize_folder(folder_to_organize)
    print("✅ Folder organized successfully!")