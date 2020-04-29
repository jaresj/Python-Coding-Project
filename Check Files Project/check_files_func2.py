import os
import sqlite3
import shutil
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askdirectory


import check_files_main
import check_files_gui



def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))

# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        #this closes app
        self.master.destroy()
        os._exit(0)
        
def source_directory(self):
    self.folder1 = askdirectory()
    self.txt_browse1.insert(0,self.folder1)
    
def destination_directory(self):
    self.folder2 = askdirectory()
    self.txt_browse2.insert(0,self.folder2)
    
def move_files(self):
    for filename in os.listdir(path=self.folder1):
        if filename.endswith('.txt'):
            shutil.move(os.path.join(self.folder1, filename), (self.folder2))
            continue
        else:
            continue

       

#============================================================================







if __name__ == "__main__":
    pass
    
