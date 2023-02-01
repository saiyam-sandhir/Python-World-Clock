import tkinter as tk
import os

class ClockAdder(tk.Toplevel):
    def __init__(self, master, COL_THEME):
        super().__init__(master)
        self.title("Add a Timebar")
        self.iconbitmap(".\\images\\icon.ico")
        self.geometry("300x300")
        self["background"] = COL_THEME["bg_col"]

class ClocksFrame(tk.Frame):
    def __init__(self, master, COL_THEME):
        super().__init__(master, height = 275, bg = COL_THEME["bg_col"])

        if os.path.exists(".\\registered_timebars.csv"):
            if os.stat(".\\registered_timebars.csv").st_size == 0:
                print("empty")

            else:
                print("not empty")

        else:
            print("does not exist")