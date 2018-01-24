import Tkinter
from Tkinter import *
import tkMessageBox
import maingui
from tkFont import BOLD
from PIL import Image, ImageTk
from Tkinter import Tk, Frame, BOTH

class resetclass():

    def resetfun(self):
        
        guiobj = maingui.guiclass()
    
        root = Tk()
        frame = Frame(root)
        root.configure(bg='light grey')
        root.geometry('1000x500+150+100')
        
        
        im = Image.open('sas22.jpg')
        tkimage = ImageTk.PhotoImage(im)
        myvar=Tkinter.Label(root,image = tkimage)
        myvar.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        
        
        
        
        
        oldpass = Entry(root, show="*", width=40, bd =10, relief=RAISED,cursor="pencil", highlightthickness = 9, highlightcolor = 'gray',  bg='black', fg='white')
        oldpass.pack(side=TOP,padx=85,pady=85)
        
        
        newpass1 = Entry(root, show="*", width=40, bd =10, relief=RAISED,cursor="pencil", highlightthickness = 9, highlightcolor = 'gray',  bg='black', fg='white')
        newpass1.pack(side=TOP,padx=10,pady=10)
        
        
        
        newpass2 = Entry(root, show="*", width=40, bd =10, relief=RAISED,cursor="pencil", highlightthickness = 9, highlightcolor = 'gray',  bg='black', fg='white')
        newpass2.pack(side=TOP,padx=50,pady=50)
        
        
        def oncl():
            
            file = open('pass.txt', 'r')
            mypass = file.read()
            file.close()
        
            if(mypass == oldpass.get()):
                
                if(newpass1.get() == newpass2.get()):
                    file = open("pass.txt", "w")
                    file.write(newpass1.get())
                    file.close()
                    tkMessageBox.showinfo( "Pass Info", "Password changed successfully")
                else:
                    tkMessageBox.showinfo( "Pass Info", "New password does not match")
                    
            else:
                tkMessageBox.showinfo( "Pass Info", "Please enter the correct password")
        
        
        def mainmenu():
            root.destroy()
            guiobj.guifun()
                    
        
        Button(root, text='CLOSE', activebackground='red', bg='gray', fg='black', relief=RAISED,cursor="hand2", highlightthickness = 9, command=root.destroy).pack(side=LEFT)            
                    
        Button(root, text=' Main Menu ', activebackground='yellow', bg='gray', fg='black', relief=RAISED,cursor="hand2", highlightthickness = 9, command=mainmenu).pack(side=LEFT)
        
        Button(root, text='   Reset   ', activebackground='green', bg='gray', fg='black', relief=RAISED,cursor="hand2", highlightthickness = 9, command=oncl).pack(side=LEFT)
        
        
        
        root.mainloop()