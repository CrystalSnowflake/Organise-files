import os
import shutil
import time as t

path = "C:/Users/jhari/Desktop/Memories"
fpath = "C:/Users/jhari/Desktop/Memories/Folders"
ipath = "C:/Users/jhari/Desktop/Memories/Images"
vpath = "C:/Users/jhari/Desktop/Memories/Videos"

files = os.listdir(path)

folders = []
imgs = []
vids = []

for file in files:
    name, extension = os.path.splitext(file)

    if extension == '':
        folders.append(file)
    elif extension in ['.png', '.jpg', '.jpeg', '.tiff']:
        imgs.append(file)
    elif extension in ['.mp3', '.mp4', '.avi']:
        vids.append(file)

wait = t.sleep(2000)

for folder in folders:
    pfrom = path + '/' + file
    pto = fpath + '/' + file

    if os.path.exists(fpath):
        print(f"Moving {folder} to its destination...")
        wait
        shutil.move(pfrom, pto)
        print(f"{folder} successfully moved!")
    else:
        print("Creating destination...")
        wait
        os.mkdir(fpath)
        print(f"Moving {folder} to its destination...")
        wait
        shutil.move(pfrom, pto)
        print(f"{folder} successfully moved!")

for img in imgs:
    pfrom = path + '/' + img
    pto = ipath + '/' + img

    if os.path.exists(ipath):
        print(f"Moving {img} to its destination...")
        wait
        shutil.move(pfrom, pto)
        print(f"{img} successfully moved!")
    else:
        print("Creating destination...")
        wait
        os.mkdir(ipath)
        print(f"Moving {img} to its destination...")
        wait
        shutil.move(pfrom, pto)
        print(f"{img} successfully moved!")

for vid in vids:
    pfrom = path + '/' + vid
    pto = vpath + '/' + vid

    if os.path.exists(vpath):
        print(f"Moving {vid} to its destination...")
        wait
        shutil.move(pfrom, pto)
        print(f"{vid} successfully moved!")
    else:
        print("Creating destination...")
        os.mkdir(vpath)
        print(f"Moving {vid} to its destination...")
        shutil.move(pfrom, pto)
        print(f"{vid} successfully moved!")
