# Copyright (c) 2023 Saiyam Jain

import tkinter as tk
from tkinter import tix
import configparser
import map_viewer as mapv
import clocks_viewer as clocksv

class WorldClockApp(tix.Tk):
    def __init__(self):
        super().__init__()

        settings = configparser.ConfigParser()
        settings.read("settings.ini")

        COL_THEME = dict(settings["col_theme"])
        
        self.title("Python World Clock")
        self.iconbitmap(".\\images\\icon.ico")
        self.geometry("700x700")
        self["background"] = COL_THEME["bg_col"]

        map_frame = mapv.MapFrame(self, COL_THEME)
        map_frame.pack(fill = tk.BOTH, expand = 1, pady = 0)

        clocks_frame = clocksv.ClocksFrame(self, COL_THEME, map_frame.map_widget)
        clocks_frame.pack(fill = tk.BOTH, expand = 1)
        
        self.mainloop()

if __name__ == "__main__":
    WorldClockApp()