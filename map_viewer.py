import tkinter as tk
import tkintermapview as tkmap

class MapFrame(tk.Frame):
    def __init__(self, master, COL_THEME):
        super().__init__(master, height = 350, bg = COL_THEME["bg_col"])

        self.map_widget = tkmap.TkinterMapView(self, corner_radius = 10)
        self.map_widget.place(relx = 0.5, rely = 0.5, relheight = 0.9, relwidth = 0.8, anchor = tk.CENTER)
