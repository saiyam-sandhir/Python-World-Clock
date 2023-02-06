# Copyright (c) 2023 Saiyam Jain

import customtkinter as ctk
import tkinter as tk
from tkinter import tix
from datetime import datetime
import time
import threading
import pytz
from PIL import Image
import csv
import pandas as pd
import random
import os

class Time(tk.Label):
    def __init__(self, master, time_zone: str, COL_THEME):
        super().__init__(master, text = datetime.now(pytz.timezone(time_zone)).strftime("%H:%M:%S"), bg = COL_THEME["fg_col"], fg = COL_THEME["txt_col"], font = ("Arial", 20, "bold"))
        self.start_clock = True
        self.thread = threading.Thread(target = self.update_timebar, args = (time_zone,))

    def update_timebar(self, time_zone):
        #Try an except to stop the return of runtime error on closing the main window
        try:
            while(self.start_clock):
                self.configure(text = datetime.now(pytz.timezone(time_zone)).strftime("%H:%M:%S"))
                time.sleep(0.1)
        except RuntimeError:
            pass

    def stop_clock(self):
        self.start_clock = False
        self.thread.join()


class TimeBar(ctk.CTkFrame):
    def __init__(self, master, timebar_details: dict, COL_THEME, map_widget):
        self.register(timebar_details)
        self.details = timebar_details
        self.map_widget = map_widget

        super().__init__(master, height = 50, corner_radius = 20, bg_color = COL_THEME["bg_col"], fg_color = COL_THEME["fg_col"])

        self.timezone = timebar_details["timezone"]

        self.time_Label = Time(self, self.timezone, COL_THEME)
        self.time_Label.place(x = 10, y = 25, anchor = tk.W)
        self.time_Label.thread.start()

        coordinates_balloon = tix.Balloon(master)

        time_zone_Label = tk.Label(self, text = self.timezone, bg = COL_THEME["fg_col"], fg = COL_THEME["txt_col"], font = ("Arial", 13, "bold"))
        time_zone_Label.place(relx = 0.52, y = 15, anchor = tk.CENTER)

        coordinates_balloon.bind_widget(time_zone_Label, balloonmsg = f"Coordinates:\n>Latitude: {self.details['lat']}{chr(176)}\n>Longitude: {self.details['long']}{chr(176)}")

        date_Label = tk.Label(self, text = datetime.now(pytz.timezone(self.timezone)).strftime("%d/%m/%Y"), bg = COL_THEME["fg_col"], fg = COL_THEME["txt_col"], font = ("Arial", 10))
        date_Label.place(relx = 0.52, y = 35, anchor = tk.CENTER)

        locatorimg_image = ctk.CTkImage(light_image = Image.open(".\\images\\locator.png"), dark_image = Image.open(".\\images\\locator.png"), size = (20, 20))
        locator_Button = ctk.CTkButton(self, image = locatorimg_image, text = "", corner_radius = 10, height = 20, width = 20, command = lambda: [map_widget.set_position(self.details["lat"], self.details["long"]), map_widget.set_zoom(15)])
        locator_Button.place(x = 540, y = 25, anchor = tk.E)

        deleteimg_image = ctk.CTkImage(light_image = Image.open(".\\images\\delete.png"), dark_image = Image.open(".\\images\\delete.png"), size = (20, 20))
        delete_Button = ctk.CTkButton(self, image = deleteimg_image, text = "", corner_radius = 10, height = 20, width = 20, command = lambda: [master.updateClocksFrame(list(timebar_details.values()), COL_THEME, map_widget), self.time_Label.stop_clock()])
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

    def mark(self):      
        def get_random_color():
            r = lambda: random.randint(0, 255)
            return ("#%02X%02X%02X" % (r(), r(), r()))

        self.marker = self.map_widget.set_marker(self.details["lat"], self.details["long"], marker_color_circle = get_random_color(), marker_color_outside = get_random_color())