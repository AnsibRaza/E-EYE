import Tkinter
from Tkinter import *
import tkMessageBox
import passreset
from tkFont import BOLD
import tkFont
import act2
import act1
import act3
import maingui
from PIL import Image, ImageTk
from Tkinter import Tk, Frame, BOTH

class guiclass():

    def guifun(self):
        
    
        playobj = act2.mainclass()
        playobj1 = act1.mainclass()
        mantrackobj = act3
        guiobj = maingui.guiclass()
        
        root = Tk()
        frame = Frame(root)
        root.configure(bg='light grey')
        root.geometry('1000x500+150+100')
        
        im = Image.open('sas333.jpg')
        tkimage = ImageTk.PhotoImage(im)
        myvar=Tkinter.Label(root,image = tkimage)
        myvar.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        
        def oncl():
            
            file = open('pass.txt', 'r')
            mypass = file.read()
            file.close()
        
            if(mypass == oldpass.get()):
                
                tkMessageBox.showinfo( "Pass Info", "Password is correct")
                    
            else:
                tkMessageBox.showinfo( "Pass Info", "Please enter the correct password")
                
        def mainmenu():
            root.destroy()
            guiobj.guifun()
            
                            
        B1a = Button(root, text='', bg='black', fg='black')
        B1a.pack(side="top", padx=55, pady=55)
        
        
        B1 = Button(root, text='      Play sample video 1     ', activebackground='green', bg='gray', fg='black', relief=RAISED,cursor="hand2", highlightthickness = 9, command=playobj.mainfun)
        B1.pack(side="top", expand=False, padx=10, pady=10)
        
        B2 = Button(root, text='      Play sample video 2     ', activebackground='green', bg='gray', fg='black', relief=RAISED,cursor="hand2", highlightthickness = 9, command=playobj1.mainfun)
        B2.pack(side="top", expand=False, padx=10, pady=10)
        
        
        B3 = Button(root, text='        Manual Tracking        ', activebackground='green', bg='gray', fg='black', relief=RAISED,cursor="hand2", highlightthickness = 9, command=mantrackobj.main)
        B3.pack(side="top", expand=False, padx=10, pady=10)
        
        
        
        B4 = Button(root, text='', bg='black', fg='black', relief=RAISED)
        B4.pack(side="top", padx=30, pady=30)
        
        
        labelhed1 = Label( root, text="\n", font='10', bg='black', fg='black')
        labelhed1.pack()
        
        
        Button(root, text='  CLOSE  ', activebackground='red', bg='gray', fg='black', relief=RAISED,cursor="hand2", highlightthickness = 9, command=root.destroy).pack(side=LEFT)
        
        Button(root, text='    Logout    ', activebackground='yellow', bg='gray', fg='black', relief=RAISED,cursor="hand2", highlightthickness = 9, command=mainmenu).pack(side=LEFT)
        
        
        
        root.mainloop()