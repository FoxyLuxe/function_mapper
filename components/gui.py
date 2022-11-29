
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


import os
import pyglet
from PIL import Image as ImgPIL
from PIL import ImageTk as ImgTK
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from tkinter.ttk import Combobox
from ctypes import windll, byref, create_unicode_buffer, create_string_buffer
from components.controller import init_setup, set_data, clean_plot, update_curve
from components.generator import download_zip

FR_PRIVATE  = 0x10
FR_NOT_ENUM = 0x20
FONT = "VT323 Regular"
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(f"{os.path.abspath(os.getcwd())}/assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def loadfont(fontpath, private=True, enumerable=False):
    '''
    Makes fonts located in file `fontpath` available to the font system.

    `private`     if True, other processes cannot see this font, and this 
                  font will be unloaded when the process dies
    `enumerable`  if True, this font will appear when enumerating fonts

    See https://msdn.microsoft.com/en-us/library/dd183327(VS.85).aspx

    '''
    # This function was taken from
    # https://github.com/ifwe/digsby/blob/f5fe00244744aa131e07f09348d10563f3d8fa99/digsby/src/gui/native/win/winfonts.py#L15
    # This function is written for Python 2.x. For 3.x, you
    # have to convert the isinstance checks to bytes and str
    if isinstance(fontpath, bytes):
        pathbuf = create_string_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExA
    elif isinstance(fontpath, str):
        pathbuf = create_unicode_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExW
    else:
        raise TypeError('fontpath must be of type str or unicode')

    flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
    numFontsAdded = AddFontResourceEx(byref(pathbuf), flags, 0)
    return bool(numFontsAdded)


loadfont(str(relative_to_assets('VT323-Regular.ttf')))
window = Tk()

window.geometry("1000x600")
window.configure(bg = "#131626")

# Desktop
canvas = Canvas(
    window,
    bg = "#131626",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

# Settings
canvas.create_rectangle(
    15.0,
    17.0,
    180.0,
    255.0,
    fill="#131626",
    outline="#FFE6EA",
    width = 5
)


## Algo
algo_img = ImgTK.PhotoImage(ImgPIL.open(relative_to_assets('algo.png')))
canvas.create_image(
    60.0,
    60,
    image=algo_img
)

canvas.create_text(
    85.0,
    25,
    anchor="nw",
    text="ALGO",
    fill="#E6A1CF",
    font=("VT323 Regular", 48 * -1)
)

algo = Combobox(
    state = "readonly", 
    values = ["newton", "lagrange", "linear"],
    font = (FONT, 22 * -1),
    width=10,
)
algo.set("linear")
algo.place(x=40, y=90)

## Deg
deg_img = ImgTK.PhotoImage(ImgPIL.open(relative_to_assets('deg.png')))
canvas.create_image(
    60,
    170,
    image=deg_img
)

canvas.create_text(
    95,
    135,
    anchor="nw",
    text="DEG",
    fill="#E6A1CF",
    font=("VT323 Regular", 48 * -1)
)

deg = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=(FONT, 32* -1),
    
)
deg.place(
    x=40,
    y=210.0,
    width=30.0,
    height=30.0
)

# Buttons
ax, chart, fig, data_file = init_setup(window)

canvas.create_rectangle(
    15.0,
    280,
    180,
    586,
    fill = "#131626",
    outline = "#FFE6EA",
    width = 5
)

img_point = ImgTK.PhotoImage(ImgPIL.open(relative_to_assets('point.png')))
button_point = Button(
    image=img_point,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_data(ax, chart, data_file),
    relief="flat"
)
button_point.place(
    x=55,
    y=290,
    width=80,
    height=38
)

img_plot = ImgTK.PhotoImage(ImgPIL.open(relative_to_assets('plot.png')))
button_plot = Button(
    image=img_plot,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_curve(ax, chart, data_file, algo.get(), deg.get()),
    relief="flat"
)
button_plot.place(
    x=55,
    y=350,
    width=80,
    height=38
)

img_clean = ImgTK.PhotoImage(ImgPIL.open(relative_to_assets('clean.png')))
button_clean = Button(
    image=img_clean,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: clean_plot(ax, chart),
    relief="flat"
)
button_clean.place(
    x=55,
    y=410,
    width=80,
    height=38
)

#--icons--

img_down = ImgTK.PhotoImage(ImgPIL.open(relative_to_assets('download.png')))
button_down = Button(
    image=img_down,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: download_zip(fig),
    relief="flat",
    background = "#131626",
)
button_down.place(
    x=68,
    y=500,
    width=50,
    height=40
)

# Plot
canvas.create_rectangle(
    200.0,
    17.0,
    983.0,
    586.0,
    fill="#131626",
    outline="#FFE6EA",
    width = 5
)

canvas.create_rectangle(
    498.0,
    51.0,
    950.0,
    452.0,
    fill="#131626",
    outline="")
window.resizable(False, False)


