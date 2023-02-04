import customtkinter as ctk
import tkinter as tk
from datetime import datetime
import pytz
from PIL import Image
import csv
import pandas as pd
import os

class Time(tk.Label):
    def __init__(self, master, time_zone: str, COL_THEME):
        super().__init__(master, text = datetime.now(pytz.timezone(time_zone)).strftime("%H:%M:%S"), bg = COL_THEME["fg_col"], fg = COL_THEME["txt_col"], font = ("Arial", 20, "bold"))
        

class TimeBar(ctk.CTkFrame):
    def __init__(self, master, timebar_details: dict, COL_THEME):
        ##a function that checks if the given details match with any row in the csv file
        ##If yes:
        ##      return Error
        ##else:
        ##      register the timebar

        self.register(timebar_details)

        super().__init__(master, height = 50, corner_radius = 20, bg_color = COL_THEME["bg_col"], fg_color = COL_THEME["fg_col"])

        self.timezone = timebar_details["timezone"]
        self.details = timebar_details

        time_Label = Time(self, self.timezone, COL_THEME)
        time_Label.place(x = 10, y = 25, anchor = tk.W)

        time_zone_Label = tk.Label(self, text = self.timezone, bg = COL_THEME["fg_col"], fg = COL_THEME["txt_col"], font = ("Arial", 13, "bold"))
        time_zone_Label.place(relx = 0.52, y = 15, anchor = tk.CENTER)

        date_Label = tk.Label(self, text = datetime.now(pytz.timezone(self.timezone)).strftime("%d/%m/%Y"), bg = COL_THEME["fg_col"], fg = COL_THEME["txt_col"], font = ("Arial", 10))
        date_Label.place(relx = 0.52, y = 35, anchor = tk.CENTER)

        #will only be viable for TimeBar.place(relx = 0.5, rely = 0.5, width = 600, anchor = tk.CENTER) in WorldClockApp
        deleteimg_image = ctk.CTkImage(light_image = Image.open(".\\images\\delete.png"), dark_image = Image.open("C:\\Users\\pc\\Desktop\\Python-World-Clock\\images\\delete.png"), size = (20, 20))
        delete_Button = ctk.CTkButton(self, image = deleteimg_image, text = "", corner_radius = 10, height = 20, width = 20)
        delete_Button.place(x = 590, y = 25, anchor = tk.E)

    def append(self):
        timebars_df = pd.read_csv(".\\registered_timebars.csv")
        if len(timebars_df) < 4:
            #if less than 4 time bars are created
            num_rows = len(timebars_df) - 1
            self.place(relx = 0.5, rely = 0.47 + 0.2 * num_rows, width = 600, anchor = tk.CENTER)
        
        else:
            #if 4 or more timebars are created
            csvfile = open(".\\registered_timebars.csv", "r")
            file_contents = csvfile.read()
            csvfile.close()
            os.remove(".\\registered_timebars.csv")
            with open(".\\registered_timebars.csv", "w") as csvfile:
                substring = self.details["timezone"]
                last_line_index = file_contents.find(substring)
                csvfile.write(file_contents[: last_line_index])

            tk.messagebox.showerror("Software's Error", "Error: Cannot add more than 4 timebars in the current version of 'Python World Clock'.\n\nRemedy: Try deleting few previously created timebars, then add new ones.")
            self.destroy()

    def register(self, timebar_details: dict):
        with open(".\\registered_timebars.csv", "a+", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(list(timebar_details.values()))

