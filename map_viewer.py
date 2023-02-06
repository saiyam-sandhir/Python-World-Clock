# Copyright (c) 2023 Saiyam Jain

import tkinter as tk
import customtkinter as ctk
import tkintermapview as tkmap

class MapFrame(tk.Frame):
    def __init__(self, master, COL_THEME):
        super().__init__(master, height = 425, bg = COL_THEME["bg_col"])

        self.map_widget = tkmap.TkinterMapView(self, corner_radius = 10)
        self.map_widget.place(relx = 0.5, rely = 0.5, relheight = 0.8, relwidth = 0.93, anchor = tk.CENTER)

        #setting default map position
        self.map_widget.set_position(28.613939, 77.209023) #New Delhi, India
        self.map_widget.set_zoom(16)

        self.servers = {
            "OpenStreetMap (Default)": "https://a.tile.openstreetmap.org/{z}/{x}/{y}.png",
            "Google Normal": "https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
            "Painting Style": "http://c.tile.stamen.com/watercolor/{z}/{x}/{y}.png",
            "Black and White": "http://a.tile.stamen.com/toner/{z}/{x}/{y}.png"
        }
        self.server_menu = ctk.CTkOptionMenu(self, values = list(self.servers.keys()), fg_color = COL_THEME["fg_col"], button_color = "#404258", button_hover_color = "#0F0E0E", dropdown_fg_color = COL_THEME["fg_col"], text_color = COL_THEME["txt_col"], dropdown_text_color = COL_THEME["txt_col"], font = ("Arial", 15), corner_radius = 10, command = self.change_tile_server)
        self.server_menu.place(relx = 0.034, rely = 0.95, anchor = tk.W)
        self.server_menu.set("Tile Servers")

    def change_tile_server(self, choice):
        selected_server = self.servers[choice]
        self.map_widget.set_tile_server(selected_server)