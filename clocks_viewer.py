# Copyright (c) 2023 Saiyam Jain

import tkinter as tk
import customtkinter as ctk
import os
import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pandas as pd
import clock

class ClockAdder(tk.Toplevel):
    def __init__(self, master, parent, COL_THEME, map_widget):
        super().__init__(master)
        self.title("Add a Timebar")
        self.iconbitmap(".\\images\\icon.ico")
        self.resizable(False, False)
        self.config(background = COL_THEME["bg_col"], padx = 20, pady = 20)

        self.map_widget = map_widget

        self.parent = parent

        tabview = ctk.CTkTabview(self, fg_color = COL_THEME["fg_col"], text_color = COL_THEME["txt_col"], corner_radius = 10)
        tabview.pack()

        tabview.add("Timezone")
        tabview.add("Coordinates")
        tabview.set("Timezone")

        #----------Timezone Tab----------#

        timezones_Label = tk.Label(tabview.tab("Timezone"), text = "Timezones:", bg = COL_THEME["fg_col"], fg = COL_THEME["txt_col"], font = ("Arial", 10, "bold"))
        timezones_Label.place(relx = 0.34, rely = 0.17, anchor = tk.E)
        
        self.timezones_OptionMenu = ctk.CTkOptionMenu(tabview.tab("Timezone"), values = pytz.common_timezones, width = 250, fg_color = COL_THEME["bg_col"], button_color = "#404258", button_hover_color = "#0F0E0E", dropdown_fg_color = COL_THEME["bg_col"], text_color = COL_THEME["txt_col"], dropdown_text_color = COL_THEME["txt_col"], font = ("Arial", 15), corner_radius = 10, dynamic_resizing = False)
        self.timezones_OptionMenu.place(relx = 0.5, rely = 0.3, anchor = tk.CENTER)
        self.timezones_OptionMenu.set("Select Timezone")

        timezones_button = ctk.CTkButton(tabview.tab("Timezone"), text = "OK", font = ("Arial", 20, "bold"), text_color = COL_THEME["txt_col"], fg_color = COL_THEME["bg_col"], corner_radius = 10, command = lambda: self.timebar_via_timezone(COL_THEME))
        timezones_button.place(relx = 0.5, rely = 0.8, anchor = tk.CENTER)

        #----------Coordinates Tab----------#

        coordinates_latitude_Label = tk.Label(tabview.tab("Coordinates"), text = "Latitude:", bg = COL_THEME["fg_col"], fg = COL_THEME["txt_col"], font = ("Arial", 10, "bold"))
        coordinates_latitude_Label.place(relx = 0.23, rely = 0.17, anchor = tk.E)

        self.coordinates_latitude_Entry = ctk.CTkEntry(tabview.tab("Coordinates"), placeholder_text = "Enter Latitude", corner_radius = 10, width = 125, fg_color = COL_THEME["bg_col"], text_color = COL_THEME["txt_col"], placeholder_text_color = COL_THEME["txt_col"])
        self.coordinates_latitude_Entry.place(relx = 0.45, rely = 0.3, anchor = tk.E)

        coordinates_longitude_Label = tk.Label(tabview.tab("Coordinates"), text = "Longitude:", bg = COL_THEME["fg_col"], fg = COL_THEME["txt_col"], font = ("Arial", 10, "bold"))
        coordinates_longitude_Label.place(relx = 1 - 0.185, rely = 0.17, anchor = tk.E)

        self.coordinates_longitude_Entry = ctk.CTkEntry(tabview.tab("Coordinates"), placeholder_text = "Enter Longitude", corner_radius = 10, width = 125, fg_color = COL_THEME["bg_col"], text_color = COL_THEME["txt_col"], placeholder_text_color = COL_THEME["txt_col"])
        self.coordinates_longitude_Entry.place(relx = 1, rely = 0.3, anchor = tk.E)   

        coordinates_button = ctk.CTkButton(tabview.tab("Coordinates"), text = "OK", font = ("Arial", 20, "bold"), text_color = COL_THEME["txt_col"], fg_color = COL_THEME["bg_col"], corner_radius = 10, command = lambda: self.timebar_via_coordinates(COL_THEME))
        coordinates_button.place(relx = 0.5, rely = 0.8, anchor = tk.CENTER)

    def timebar_via_timezone(self, COL_THEME):
        if self.timezones_OptionMenu.get() != "Select Timezone":
            timezone = self.timezones_OptionMenu.get()
            num_of_underscores = 0
            for i in timezone:
                if i == "_":
                    num_of_underscores += 1
            geolocator = Nominatim(user_agent = "geoapiExercises")
            loc = timezone.replace("_", " ", num_of_underscores)
            loc = loc[loc.find("/") + 1:]

            try:
                #Trying to get coordinates from the given timezone
                loc = geolocator.geocode(timezone)
                lat = loc.latitude
                long_ = loc.longitude
                        
                timebar_details = {
                    "timezone": timezone,
                    "lat": lat,
                    "long": long_
                }

                self.destroy()

                timebar = clock.TimeBar(self.parent, timebar_details, COL_THEME, self.map_widget)
                timebar.append()
                timebar.mark()

            except AttributeError:
                tk.messagebox.showerror("Software's Error", f"Error: 'Python World Clock' is unable to detect the coordinates for '{timezone}'.\n\nRemedy: Try creating timebar using coordinates instead for '{timezone}'.")

        else:
            tk.messagebox.showerror("User's Error", "Error: Tried creating a timebar without selecting a timezone.\n\nRemedy: Select a timezone or optionally any valid coordinates")

    def timebar_via_coordinates(self, COL_THEME):
        try:
            lat = float(self.coordinates_latitude_Entry.get())
            long_ = float(self.coordinates_longitude_Entry.get())

            tz_f = TimezoneFinder()
            timezone = tz_f.timezone_at(lng = long_, lat = lat)

            timebar_details = {
                "timezone": timezone,
                "lat": lat,
                "long": long_
            }

            self.destroy()

            timebar = clock.TimeBar(self.parent, timebar_details, COL_THEME, self.map_widget)
            timebar.append()
            timebar.mark()

        except ValueError:
            tk.messagebox.showerror("User's Error", "Error: Entered invalid input in the coordinates entry boxes.\n\nRemedy: Enter valid coordinate values(eg: 28.613939).")


class ClocksFrame(tk.Frame):
    def __init__(self, master, COL_THEME, map_widget):
        super().__init__(master, height = 275, bg = COL_THEME["bg_col"])

        self.add_clock_button = ctk.CTkButton(self, text = "➕", font = ("Arial", 20, "bold"), width = 40, height = 40, corner_radius = 10, fg_color = COL_THEME["fg_col"], text_color = COL_THEME["txt_col"], command = lambda: ClockAdder(master, self, COL_THEME, map_widget))
        self.add_clock_button.place(relx = 0.965, rely = 0.08, anchor = tk.E)

        if os.path.exists(".\\registered_timebars.csv"):
            #if registered_timebar.csv file exits
            if os.stat(".\\registered_timebars.csv").st_size == 0:
                #if that csv file exists and is empty
                ClockAdder(master, self, COL_THEME, map_widget)

            else:
                self.updateClocksFrame(None, COL_THEME, map_widget)

        else:
            #if that csv file does not exist
            ClockAdder(master, self, COL_THEME, map_widget)

    def updateClocksFrame(self, deleted_timebar_details, COL_THEME, map_widget):
        df = pd.read_csv(".\\registered_timebars.csv", header = None)

        if deleted_timebar_details != None:
            for i in self.winfo_children()[1:]:
                if type(i) == clock.TimeBar:
                    i.marker.delete()
                    i.time_Label.stop_clock()
                    i.destroy()

            deleted_timebar_index = df.index[df.apply(tuple, axis=1) == tuple(deleted_timebar_details)].tolist()
            df = df.drop(deleted_timebar_index)

        with open(".\\registered_timebars.csv", "w") as csvfile:
            pass

        for index, row in df.iterrows():
            keys = ["timezone", "lat", "long"]
            values = row.tolist()
            timebar_details = dict(zip(keys, values))

            timebar = clock.TimeBar(self, timebar_details, COL_THEME, map_widget)
            timebar.append()
            timebar.mark()