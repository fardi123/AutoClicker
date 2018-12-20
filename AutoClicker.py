#from PIL import ImageGrab, ImageOps
import pyautogui
import time
import tkinter as tk
from numpy import *


class Coordinates():
#Coordinates can be changed to wherever you want to AutoClick
    replayBtn = (100,350)


# close button (woah)
class YourGUI(tk.Tk):
    def __init__(self):
        # inherit tkinter's window methods
        tk.Tk.__init__(self)

        tk.Label(self, text="ENTER X:").grid(row=0, column=0)
        self.inputX = tk.Entry(self)
        self.inputX.grid(row=0, column=1)

        tk.Label(self, text="ENTER Y:").grid(row=0, column=0)
        self.inputY = tk.Entry(self)
        self.inputY.grid(row=0, column=2)

        tk.Button(self, text="convert", command=self.do_conversion).grid(row=3, column=0, columnspan=2)

        tk.Button(self, text="exit!", command=self.EXITME).grid(row=4, column=0, columnspan=2)

    def EXITME(self):
        exit(0)  # crashed prog so it closes
        # strtoint("crashmE!")

    def do_conversion(self):
        y = self.inputY.get()
        x = self.inputX.get()

        running = True
        try:
            x = int(x)
            y = int(y)
        except:
            print("Invalid point")
            exit(0)
            # strtoint("crashmE!")
        while running:
            pyautogui.click(x, y)


your_gui = YourGUI()
your_gui.mainloop()
