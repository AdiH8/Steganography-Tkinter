from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os 
from stegano import lsb
from tkinter import messagebox

root= Tk()
root.title("Steganography - Hide a Secret Text Message in Image")
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="#2f4155")

def open_image():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                       title="Select Image File",
                                        filetype=(("PNG file","*.png"),
                                                  ("JPG file","*jpg"),
                                                  ("All files","*.*")))
   
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    
    lbl.configure(image=img,width=340,height=280)
    lbl.image=img 


def hide():
    global secret
    message=text1.get(1.0,END)
    secret=lsb.hide(str(filename),message)
    text1.delete(1.0,END)
    messagebox.showinfo("Success", "Message encoded successfully")

def show():
    try:
        clear_message=lsb.reveal(filename)   
        text1.delete(1.0,END)
        text1.insert(END,clear_message)
    except:
        messagebox.showinfo("Error","No message detected!")

def save():
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                              filetypes=(("PNG files", "*.png"), ("All files", "*.*")),
                                              title="Save Image As")
    if save_path:
        secret.save(save_path)         

def clear():
    text1.delete(1.0, END)
    lbl.configure(image=None)
    filename = None  
    lbl.image=None


Label(root,text="STEGANOGRAPHY",bg="#2d4155",fg="white",font="arial 25 bold").place(x=100,y=20)

#first Frame
f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)
lbl=Label(f,bg="black")
lbl.place(x=0,y=0)

#second frame
frame2=Frame(root,bd=3,width=340,height=280, bg="white",relief=GROOVE)
frame2.place(x=350,y=80)

text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#third frame
frame3=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=370)

Button(frame3,text="Open Image",width=10,height=2,font="arial 14 bold",command=open_image).place(x=20,y=20)
Button(frame3,text="Save Image",width=10,height=2,font="arial 14 bold",command=save).place(x=180,y=20)

#4 frame
frame4=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame4.place(x=360,y=370)

Button(frame4,text="Hide Data",width=10,height=2,font="arial 14 bold",command=hide).place(x=20,y=20)
Button(frame4,text="Show Data",width=10,height=2,font="arial 14 bold",command=show).place(x=180,y=20)

Button(root, text="Clear", width=9, height=2, font="arial 14 bold", command=clear).place(x=460, y=10)

root.mainloop()