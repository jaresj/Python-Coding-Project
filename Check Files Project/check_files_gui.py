from tkinter import *
import tkinter as tk

# Be sure to import our other modules
# so we can have access to them
import check_files_main
import check_files_func


def load_gui(self):

    self.txt_browse1 = tk.Entry(self.master,text='')
    self.txt_browse1.grid(row=1,column=1,rowspan=1,columnspan=8,padx=(30,0),pady=(45,0),stick=N+E+W)
    self.txt_browse2 = tk.Entry(self.master,text='')
    self.txt_browse2.grid(row=2,column=1,rowspan=1,columnspan=8,padx=(30,0),pady=(10,0),stick=N+E+W)

    self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda: check_files_func.source_directory(self))
    self.btn_browse1.grid(row=1,column=0,padx=(25,0),pady=(45,0),sticky=W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda: check_files_func.destination_directory(self))
    self.btn_browse2.grid(row=2,column=0,padx=(25,0),pady=(10,0),sticky=W)
    self.btn_chkForFiles = tk.Button(self.master,width=12,height=2,text='Check for files...',command=lambda: check_files_func.move_files(self))
    self.btn_chkForFiles.grid(row=3,column=0,padx=(25,0),pady=(10,0),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: check_files_func.ask_quit(self))
    self.btn_close.grid(row=3,column=8,padx=(250,0),pady=(15,0),sticky=E)




if __name__ == "__main__":
    pass

