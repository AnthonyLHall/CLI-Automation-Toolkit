from pathlib import Path
import os

downloads_dir = Path.home() / "Downloads"
txt_folder = downloads_dir / "TXTFILES"
executables_folder = downloads_dir / "EXECUTABLES"
Path.mkdir(txt_folder)

for item in txt_folder.iterdir():
    print(item)

def sort_files(directory):

    try:
        Path.mkdir(txt_folder)
    except:
        print("txt_folder already exists...")

    try:
        Path.mkdir(executables_folder)
    except:
        print("Executables already exists...")

    for file in directory.iterdir():
        print(file)

