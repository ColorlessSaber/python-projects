"""
Python Ver: 3.13

Author: Michael Heilman

Purpose: An application that moves file(s) from one folder to another with a click of a button. Also,
automatically check each file to see if they are new or modified within the last 24 hours, if either true then
transfer them accordingly.
"""
import os, shutil
import datetime as dt
import tkinter as tk
from tkinter import filedialog

class ParentWindow(tk.Frame):
    def __init__(self, primary):
        super().__init__()

        # build the window
        self.primary = primary
        self.primary.title('File Transfer')

        # create the button and entry field for source selection
        self.btn_source_dir = tk.Button(text='Select Source', width=20, command=self.source_dir)
        self.btn_source_dir.grid(row=0, column=0, padx=(20,10), pady=(30,0))
        self.entry_source_dir = tk.Entry(width=75)
        self.entry_source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        # create the button and entry field for destination selection
        self.btn_destination_dir = tk.Button(text='Select Destination', width=20, command=self.destination_dir)
        self.btn_destination_dir.grid(row=1, column=0, padx=(20,10), pady=(15,10))
        self.entry_destination_dir = tk.Entry(width=75)
        self.entry_destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))

        # button to start the transfer
        self.btn_transfer = tk.Button(text='Transfer Files', width=20, command=self.transfer_files)
        self.btn_transfer.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        # button to close application
        self.btn_exit = tk.Button(text='Exit', width=20, command=self.exit_program)
        self.btn_exit.grid(row=2, column=2, padx=(10,40), pady=(0,15))

    def source_dir(self):
        """
        Opens a file-dialog window to allow user to select the source directory.
        """
        select_source_dir = filedialog.askdirectory()
        self.entry_source_dir.delete(0, tk.END) # clear the entry source directory for newly selected directory.
        self.entry_source_dir.insert(0, select_source_dir)

    def destination_dir(self):
        """
        Opens a file-dialog window to allow user to select the destination directory
        """
        select_destination_dir = filedialog.askdirectory()
        self.entry_destination_dir.delete(0, tk.END) # clear the entry destination directory for newly selected directory.
        self.entry_destination_dir.insert(0, select_destination_dir)

    def transfer_files(self):
        """
        Moves the files from the source directory to the destination directory
        """
        source = self.entry_source_dir.get()
        destination = self.entry_destination_dir.get()
        source_files = os.listdir(source)

        # check each file and see if they meet one of the following requirements:
        # 1) must be new
        # 2) edited within the last 24 hours
        current_datetime = dt.datetime.now()
        for file in source_files:
            file_timestamp = dt.datetime.fromtimestamp(os.path.getmtime(source + '/' + file))
            if (current_datetime - file_timestamp) < dt.timedelta(days=1):
                shutil.move(source + '/' + file, destination)
                print(file + ' was successfully transferred.')

    def exit_program(self):
        """
        Closes the application when function actives
        """
        self.primary.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = ParentWindow(root)
    root.mainloop()
