import tkinter as tk

class WorldClockApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Python World Clock")
        self.iconbitmap(".\\images\\icon.ico")
        self.geometry("700x700")

        self.mainloop()

if __name__ == "__main__":
    WorldClockApp()