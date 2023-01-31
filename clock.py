import customtkinter as ctk
import tkinter as tk
from datetime import datetime
import pytz
from PIL import Image

class Time(tk.Label):
    def __init__(self, master, time_zone: str, COL_THEME):
        super().__init__(master, text = datetime.now(pytz.timezone(time_zone)).strftime("%H:%M:%S"), bg = COL_THEME["fg_col"], fg = COL_THEME["txt_col"], font = ("Arial", 20, "bold"))

    def register_timezone(self):
        pass

    def update_time(self):
        pass

class TimeBar(ctk.CTkFrame):
    def __init__(self, master, time_zone: str, COL_THEME):
        super().__init__(master, height = 50, corner_radius = 20, bg_color = COL_THEME["bg_col"], fg_color = COL_THEME["fg_col"])

        time_Label = Time(self, time_zone, COL_THEME)
        time_Label.place(x = 10, y = 25, anchor = tk.W)

        time_zone_Label = tk.Label(self, text = time_zone, bg = COL_THEME["fg_col"], fg = COL_THEME["txt_col"], font = ("Arial", 13, "bold"))
        time_zone_Label.place(relx = 0.52, y = 15, anchor = tk.CENTER)

        date_Label = tk.Label(self, text = datetime.now(pytz.timezone(time_zone)).strftime("%d/%m/%Y"), bg = COL_THEME["fg_col"], fg = COL_THEME["txt_col"], font = ("Arial", 10))
        date_Label.place(relx = 0.52, y = 35, anchor = tk.CENTER)

        #will only be viable for TimeBar.place(relx = 0.5, rely = 0.5, width = 600, anchor = tk.CENTER) in WorldClockApp
        deleteimg_image = ctk.CTkImage(light_image = Image.open("C:\\Users\\pc\\Desktop\\Python-World-Clock\\images\\delete.png"), dark_image = Image.open("C:\\Users\\pc\\Desktop\\Python-World-Clock\\images\\delete.png"), size = (20, 20))
        delete_Button = ctk.CTkButton(self, image = deleteimg_image, text = "", corner_radius = 10, height = 20, width = 20)
        delete_Button.place(x = 590, y = 25, anchor = tk.E)

