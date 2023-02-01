from tkinter import *
from tkinter import ttk
import texts

# Colors
MATTE_BLACK = "#171717"

# Window
wn = Tk()
wn.wm_title(texts.txt_title)
wn.wm_geometry("400x400+780+230")
wn.wm_resizable(False, False)
wn.wm_iconbitmap(r"C:\Users\carlo\PycharmProjects\pomodori-timer\images\icon_ico.ico")
wn.configure(background=MATTE_BLACK)

wn.mainloop()
