from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
import os
from stegano import lsb
from tkinter import messagebox

root=Tk()
root.title("Image Steganography - Message Securely")
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="#222233")

#Defining Functions for Buttons
#For Browsing Image
def Browseimage():
    global filename,base_filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title="Select Image File",
                                        filetype=(("PNG file","*.png"),
                                                 ("JPG file","*.jpg"),("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img
    base_filename= os.path.splitext(os.path.basename(filename))

#For Encrypting text
def Encrypt():
    global secret
    message=text1.get(1.0,END)
    secret=lsb.hide(str(filename),message)

#For Decrypting text
def Decrypt():
    show_message=lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,show_message)

#For Saving Image
def SaveImage():
    global base_filename
    count = 1
    while os.path.exists(f"Encrypted_Image_{count}.png"):
        count += 1
    save_path = (f"Encrypted_Image_{count}.png")
    secret.save(save_path)
    messagebox.showinfo("Image Saved", f"The encrypted image has been saved at:\n{os.path.abspath(save_path)}")


#For icon
image_icon=PhotoImage(file="10001.png")
root.iconphoto(False,image_icon)

#For logo
logo=PhotoImage(file="10002.png")
Label(root,image=logo,bg="#222233").place(x=10,y=0)
Label(root,text="Digital Image Processing",bg="#222233",fg="white",font="arial 25 bold").place(x=100,y=20)

#First Frame(For Image)
f1=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f1.place(x=10,y=80)

lbl=Label(f1,bg="black")
lbl.place(x=40,y=10)

#Second Frame(For Text)
f2=Frame(root,bd=3,bg="white",width=340,height=280,relief=GROOVE)
f2.place(x=350,y=80)

#Text box for Encrypting message
text1=Text(f2,font="Robote 20",bg="white",fg="black",relief=GROOVE)
text1.place(x=0,y=0,width=320,height=295)

#Scroll bar for Encrypting text box
Scrollbar1=Scrollbar(f2)
Scrollbar1.place(x=320,y=0,height=300)

Scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar1.set)

#Third frame(For Browsing and Saving Image)
f3=Frame(root,bd=3,bg="#222233",width=330,height=100,relief=GROOVE)
f3.place(x=10,y=370)

#Buttons For Browsing and Saving Image
Button(f3,text="Browse Image",width=12,height=2,font="arial 14 bold",command=Browseimage).place(x=20,y=30)
Button(f3,text="Save Image",width=10,height=2,font="arial 14 bold",command=SaveImage).place(x=180,y=30)
Label(f3,text="*Upload the Image here",bg="#222233",fg="orange").place(x=20,y=5)

#Fourth frame(for Encrypting and Decrypting text)
f4=Frame(root,bd=3,bg="#222233",width=330,height=100,relief=GROOVE)
f4.place(x=360,y=370)

#Buttons For Encrypting and Decrypting text
Button(f4,text="Encrypt Image",width=12,height=2,font="arial 14 bold",command=Encrypt).place(x=12,y=30)
Button(f4,text="Decrypt Image",width=11,height=2,font="arial 14 bold",command=Decrypt).place(x=173,y=30)
Label(f4,text="*Encrypt/Decrypt Image from here",bg="#222233",fg="orange").place(x=20,y=5)

root.mainloop()



