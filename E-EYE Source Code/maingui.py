import Tkinter
from Tkinter import *
import tkMessageBox
import passreset
from tkFont import BOLD
import tkFont
import mainframe
from PIL import Image, ImageTk
from Tkinter import Tk, Frame, BOTH


class guiclass():

    def guifun(self):
    
        resetobj = passreset.resetclass()
        mainobj = mainframe.guiclass()
        
        root = Tk()
        frame = Frame(root)
        root.configure(bg='light grey')
        root.geometry('1000x500+150+100')
        
        im = Image.open('sas111.jpg')
        tkimage = ImageTk.PhotoImage(im)
        myvar=Tkinter.Label(root,image = tkimage)
        myvar.place(x=0, y=0, relwidth=1, relheight=1)
        
       
        oldpass = Entry(root, show="*", width=40, bd =10, relief=RAISED,cursor="pencil", highlightthickness = 9, highlightcolor = 'gray', bg='black', fg='white')
        oldpass.pack(side=TOP,padx=200,pady=200)
        
        
        def oncl():
            
            file = open('pass.txt', 'r')
            mypass = file.read()
            file.close()
        
            if(mypass == oldpass.get()):
                
                root.destroy()
                mainobj.guifun()
                    
            else:
                tkMessageBox.showinfo( "Pass Info", "Please enter the correct password")
                
        def resetpass():
            
            root.destroy()
            resetobj.resetfun()
                            
            
        Button(root, text='  CLOSE  ', activebackground='red', bg='gray', fg='black', relief=RAISED,cursor="hand2", highlightthickness = 9, command=root.destroy).pack(side=LEFT)
        
        Button(root, text=' Reset Password ', activebackground='yellow', bg='gray', fg='black', relief=RAISED,cursor="hand2", highlightthickness = 9, command=resetpass).pack(side=LEFT)
        
        Button(root, text='   Login   ', activebackground='green', bg='gray', fg='black', relief=RAISED,cursor="hand2", highlightthickness = 9, command=oncl).pack(side=LEFT)
        
        
        
        root.mainloop()