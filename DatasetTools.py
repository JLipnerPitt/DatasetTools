import os
import tkinter as tk
from tkinter import filedialog

def select_folder():

    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open the file explorer and ask for a directory
    folder_selected = filedialog.askdirectory()

    # Destroy the root window after the directory is chosen
    root.destroy()

    return folder_selected

def rename_files(directory, name, count=1):
    i = count
    for file in os.listdir(directory):
        old = os.path.join(directory, file)

        if (i<10):
            new = os.path.join(directory, name + "-0{}.safetensors".format(i))
        else:
            new = os.path.join(directory, name + "-{}.safetensors".format(i))

        os.rename(old,new)
        i += 1
    os.startfile(dir) # open the C:\Windows folder

def remove_text(directory, text):
    for file in os.listdir(directory):
        old = os.path.join(directory, file)
        new = old.replace(text,'')
        os.rename(old,new)
    os.startfile(dir) # open the C:\Windows folder

def printnumbers(n):
    for i in range(n-1):
        if (i+1<10):
            print("-0{}, ".format(i+1),end='')
        else:
            print("-{}, ".format(i+1),end='')
    print("-{} ".format(n),end='')

dir = select_folder()
str = "HarribelIllusV8"
rename_files(dir,str)

#printnumbers(25)
#remove_text(dir,"_cleanup")