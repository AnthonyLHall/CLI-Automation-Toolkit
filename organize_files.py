from pathlib import Path
import shutil

downloads_dir = Path.home() / "Downloads"
txt_folder = downloads_dir / "TXTFILES"
executables_folder = downloads_dir / "EXECUTABLES"
images_folder = downloads_dir / "IMAGES"
iso_folder = downloads_dir / "ISOs"


def initialize_directories():
    try:
        Path.mkdir(txt_folder)
    except:
        print("txt_folder already exists...")
    
    try:
        Path.mkdir(executables_folder)
    except:
        print("Executables already exists...")

    try:
        Path.mkdir(images_folder)
    except:
        print("Images already exists...")

    try:
        Path.mkdir(iso_folder)
    except:
        print("Isos already exists...")



def sort_files(directory):

    # move txt files
    for file in directory.iterdir():
        current_item = file.name
        if current_item.endswith(".txt") or current_item.endswith(".rtf"):
            shutil.move(file, txt_folder)

        if current_item.endswith(".iso"):
            shutil.move(file, iso_folder)

        if current_item.endswith(".dmg"):
            shutil.move(file, executables_folder)

        if current_item.endswith(".png"):
            shutil.move(file, images_folder)


initialize_directories()


sort_files(downloads_dir)