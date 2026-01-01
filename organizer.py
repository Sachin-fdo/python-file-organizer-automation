import os
import shutil
from pathlib import Path

def organize_files(folder_path, dry_run=True):
    folder = Path(folder_path)

    if not folder.exists():
        print("Folder does not exist.")
        return

    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix.lower().replace(".", "")
            ext_folder = folder / (ext if ext else "no_extension")

            if dry_run:
                print(f"[DRY RUN] Move {file.name} -> {ext_folder}/")
            else:
                ext_folder.mkdir(exist_ok=True)
                shutil.move(str(file), ext_folder / file.name)
                print(f"Moved {file.name} -> {ext_folder}/")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python organizer.py <folder_path> [--run]")
        exit()

    path = sys.argv[1]
    run_mode = "--run" in sys.argv

    organize_files(path, dry_run=not run_mode)
