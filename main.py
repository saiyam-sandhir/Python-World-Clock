import tkinter as tk
import configparser

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

        map_frame = tk.Frame(self, height = 350, bg = COL_THEME["bg_col"])
        map_frame.pack(fill = tk.BOTH, expand = 1, pady = 0)

        clocks_frame = tk.Frame(self, height = 350, bg = COL_THEME["bg_col"])
        clocks_frame.pack(fill = tk.BOTH, expand = 1)

        self.mainloop()

if __name__ == "__main__":
    WorldClockApp()