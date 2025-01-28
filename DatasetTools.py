import os
import tkinter as tk
import shutil
from tkinter import filedialog
from PIL import Image

def create_folder(dir, folder_name="temp"):
    directory = dir
    folder_path = os.path.join(directory, folder_name)  # joins creates directory/folder_name path
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)  # delete folder if it already exists
    os.makedirs(folder_path)  # creates folder in specified directory
    return folder_path

def select_folder():

    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open the file explorer and ask for a directory
    folder_selected = filedialog.askdirectory()

    # Destroy the root window after the directory is chosen
    root.destroy()

    return folder_selected

def rename_files(name, count=1):
    directory = select_folder()
    i = count
    for file in os.listdir(directory):
        old = os.path.join(directory, file)

        if (i<10):
            new = os.path.join(directory, name + "-0{}.safetensors".format(i))
        else:
            new = os.path.join(directory, name + "-{}.safetensors".format(i))

        os.rename(old,new)
        i += 1
    os.startfile(directory) # open the C:\Windows folder

def remove_text(text):
    directory = select_folder()
    for file in os.listdir(directory):
        old = os.path.join(directory, file)
        new = old.replace(text,'')
        os.rename(old,new)
    os.startfile(directory) # open the C:\Windows folder

def printnumbers(n):
    for i in range(n-1):
        if (i+1<10):
            print("-0{}, ".format(i+1),end='')
        else:
            print("-{}, ".format(i+1),end='')
    print("-{} ".format(n),end='')

def check_resolution():
    dir = select_folder()
    imgs = []
    for file in os.listdir(dir):
        img = Image.open(os.path.join(dir, file))
        width, height = img.size
        resolution = width*height
        if width != 1024 and height != 1024:
            imgs.append(os.path.join(dir, file))
    
    if len(imgs) == 0:
        return
    else:
        new_folder = create_folder(dir)
        for file in imgs:
            shutil.copy(file, new_folder)

def separate_images(tag: str):
    dir = select_folder()
    directory2 = create_folder("with", os.path.dirname(dir))
    directory3 = create_folder("without", os.path.dirname(dir))

    for filename in os.listdir(dir):
        if filename.endswith(".txt"):  # Ensure we're only looking at .txt files
            with open(os.path.join(dir, filename), 'r') as file:
                contents = file.read()
                if tag in contents:
                    txtfile = os.path.join(dir, filename)
                    imgfile = os.path.join(dir, filename.replace('.txt', '.jpg'))
                    shutil.copy(txtfile, directory2)
                    shutil.copy(imgfile, directory2)
                else:
                    txtfile = os.path.join(dir, filename)
                    imgfile = os.path.join(dir, filename.replace('.txt', '.jpg'))
                    shutil.copy(txtfile, directory3)
                    shutil.copy(imgfile, directory3)



                
#rename_files("HarribelIllusV24")

#check_resolution()
#printnumbers(15)
#remove_text("_cleanup")
separate_images("huge weapon")