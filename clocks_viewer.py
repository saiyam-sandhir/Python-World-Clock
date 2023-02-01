import tkinter as tk
import customtkinter as ctk
import os
import pytz

class ClockAdder(tk.Toplevel):
    def __init__(self, master, COL_THEME):
        super().__init__(master)
        self.title("Add a Timebar")
        self.iconbitmap(".\\images\\icon.ico")
        self.resizable(False, False)
        self.config(background = COL_THEME["bg_col"], padx = 20, pady = 20)

        tabview = ctk.CTkTabview(self, fg_color = COL_THEME["fg_col"], text_color = COL_THEME["txt_col"], corner_radius = 10)
        tabview.pack()

        tabview.add("Timezone")
        tabview.add("Coordinates")
        tabview.set("Timezone")

        #----------Timezone Tab----------#

        timezones_Label = tk.Label(tabview.tab("Timezone"), text = "Timezones:", bg = COL_THEME["fg_col"], fg = COL_THEME["txt_col"], font = ("Arial", 10, "bold"))
        timezones_Label.place(relx = 0.34, rely = 0.17, anchor = tk.E)
        
        timezones_OptionMenu = ctk.CTkOptionMenu(tabview.tab("Timezone"), values = pytz.common_timezones, width = 250, fg_color = COL_THEME["bg_col"], button_color = "#404258", button_hover_color = "#0F0E0E", dropdown_fg_color = COL_THEME["bg_col"], text_color = COL_THEME["txt_col"], dropdown_text_color = COL_THEME["txt_col"], font = ("Arial", 15), corner_radius = 10, dynamic_resizing = False)
        timezones_OptionMenu.place(relx = 0.5, rely = 0.3, anchor = tk.CENTER)
        timezones_OptionMenu.set("Select Timezone")

        timezones_button = ctk.CTkButton(tabview.tab("Timezone"), text = "OK", font = ("Arial", 20, "bold"), text_color = COL_THEME["txt_col"], fg_color = COL_THEME["bg_col"], corner_radius = 10)
        timezones_button.place(relx = 0.5, rely = 0.8, anchor = tk.CENTER)

        #----------Coordinates Tab----------#

        coordinates_latitude_Label = tk.Label(tabview.tab("Coordinates"), text = "Latitude:", bg = COL_THEME["fg_col"], fg = COL_THEME["txt_col"], font = ("Arial", 10, "bold"))
        coordinates_latitude_Label.place(relx = 0.23, rely = 0.17, anchor = tk.E)

        coordinates_latitude_Entry = ctk.CTkEntry(tabview.tab("Coordinates"), placeholder_text = "Enter Latitude", corner_radius = 10, width = 125, fg_color = COL_THEME["bg_col"], text_color = COL_THEME["txt_col"], placeholder_text_color = COL_THEME["txt_col"])
        coordinates_latitude_Entry.place(relx = 0.45, rely = 0.3, anchor = tk.E)

        coordinates_longitude_Label = tk.Label(tabview.tab("Coordinates"), text = "Longitude:", bg = COL_THEME["fg_col"], fg = COL_THEME["txt_col"], font = ("Arial", 10, "bold"))
        coordinates_longitude_Label.place(relx = 1 - 0.185, rely = 0.17, anchor = tk.E)

        coordinates_latitude_Entry = ctk.CTkEntry(tabview.tab("Coordinates"), placeholder_text = "Enter Latitude", corner_radius = 10, width = 125, fg_color = COL_THEME["bg_col"], text_color = COL_THEME["txt_col"], placeholder_text_color = COL_THEME["txt_col"])
        coordinates_latitude_Entry.place(relx = 1, rely = 0.3, anchor = tk.E)   

        coordinates_button = ctk.CTkButton(tabview.tab("Coordinates"), text = "OK", font = ("Arial", 20, "bold"), text_color = COL_THEME["txt_col"], fg_color = COL_THEME["bg_col"], corner_radius = 10)
        coordinates_button.place(relx = 0.5, rely = 0.8, anchor = tk.CENTER) 

class ClocksFrame(tk.Frame):
    def __init__(self, master, COL_THEME):
        super().__init__(master, height = 275, bg = COL_THEME["bg_col"])

        self.add_clock_button = ctk.CTkButton(self, text = "➕", font = ("Arial", 20, "bold"), width = 40, height = 40, corner_radius = 10, fg_color = COL_THEME["fg_col"], text_color = COL_THEME["txt_col"], command = lambda: ClockAdder(master, COL_THEME))
        self.add_clock_button.place(relx = 0.965, rely = 0.08, anchor = tk.E)

        if os.path.exists(".\\registered_timebars.csv"):
            if os.stat(".\\registered_timebars.csv").st_size == 0:
                print("empty")

            else:
                print("not empty")

        else:
            print("does not exist")