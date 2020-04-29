# Python Ver:   3.8.2
#
# Author:       Justice
#
# Purpose:      Check Files
#
#
# Tested OS:    This code was written and tested to work with windows 10.

from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Be sure to import out other modules
# so we can have access to them
import check_files_gui
import check_files_func


# Frame is the tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, *kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,200) #(Height, Width)
        self.master.maxsize(500,200)
        # This CenterWindow method will center our app on the user's screen
        check_files_func.center_window(self,500,200)
        self.master.title("Check file")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: check_files_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separeate module,
        # keeping your code compartmentalized and clutter free
        check_files_gui.load_gui(self)

"""
    It is from these few lines of code that python will begin our gui and application
    The (if __name__ == "__main__":) part is basically telling Python that if this script
    is ran, it should start by running the code below this line....in this case we have
    instructed Python to run the following in this order

    root = tk.Tk()               #This instantiates the Tk.() root frame (window into being
    App = ParentWindow(root)     #This instantiates our own class as an App object
    root.mainloop()              #This ensures the Tkinter class object, our window, to keep looping
                                 #meaning, it will stay open until we instruct it to close
"""
 







if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
