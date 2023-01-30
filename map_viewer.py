import tkinter as tk
import tkintermapview as tkmap

class MapFrame(tk.Frame):
    def __init__(self, master, COL_THEME):
        super().__init__(master, height = 350, bg = "red")
