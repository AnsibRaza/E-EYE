import Tkinter
from Tkinter import *
import tkMessageBox
import passreset
from tkFont import BOLD
import tkFont
import mainframe
from PIL import Image, ImageTk
from Tkinter import Tk, Frame, BOTH

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=10, column=10)
e2.grid(row=1, column=1)

mainloop( )