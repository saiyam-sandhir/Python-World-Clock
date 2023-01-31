import tkinter as tk
import configparser
import map_viewer as mapv
from clock import TimeBar

class WorldClockApp(tk.Tk):
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

        clocks_frame = tk.Frame(self, height = 275, bg = COL_THEME["bg_col"])
        clocks_frame.pack(fill = tk.BOTH, expand = 1)

        ##A function that checks if csv exits or not
        ##if yes and not empty:
        ##      continue
        ##else:
        ##      create a toplevel window that takes details from the user about the local time zone or his/her coordinates
        ##      using those details create a timebar with its delete button removed/disabled
        
        self.mainloop()

if __name__ == "__main__":
    WorldClockApp()