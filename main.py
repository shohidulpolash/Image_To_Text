from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import cv2
import numpy as np
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Polash\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

root = Tk()
root.geometry('580x360')
root.title("Shohidul Polash Dictionary")
root.configure(background="#cca8f0")


text=StringVar()
address =StringVar()
def clk():
    output.delete(0.0,END)
    global address
    file1 = filedialog.askopenfilename()
    global text
    text = open(file1, 'r')
    address = (str(file1))
    tkinter.messagebox.showinfo("Image to Text", 'Image is selected !')
    img = Image.open(address)
    text = tess.image_to_string(img)
    output.insert(0.0, text)



#button = Button(root, text="Select an Image", command=mfileopen, bg='powder blue',font="Times 12", width=25)
but = Button(root, width=15, text='Select a picture', command=clk, bg='powder blue', font="Times 12",height=0)
but.place(x=210, y=35)

labb = Label(root, text='Text in the picture:', bg="#cca8f0", font='Times 18 bold')
labb.place(x=180, y=85)

output = Text(root, width=40, height=8, font='Times 18 bold', fg="black")
output.place(x=45, y=120)

root.mainloop()