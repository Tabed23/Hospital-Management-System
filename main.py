from tkinter import *
import tkinter
import sqlite3
from registration import Registraction
from Emergency import Emergency
from PIL import ImageTk,Image

conn = sqlite3.connect('database.db')


def emergency():
    root = Tk()

    app = Emergency(root)


def register():
    root = Tk()
    app = Registraction(root)


def main():
    # creating the object of tkinter
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("front.jpg"))
    root.title("Hospital Management System")
    canvas = Canvas(root, bg='grey')
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW, image=img)
    main_Lable = Label(canvas,image=img, text="Welcome to Hospital Management System", font='arial 10 bold', bg='grey')
    main_Lable.pack()
    main_Lable.place(x=0, y=0)

    em = Button(canvas, text='Add Emergency', width=20, height=1, command=emergency, fg='red', bg='white')
    em.place(x=0, y=100)
    rg = Button(canvas, text='Add Registrations', width=20, height=1, command=register, fg='red', bg='white')
    rg.place(x=0, y=200)
    # resolution of the window
    root.geometry('370x270+0+0')
    # preventing the resize feature
    root.resizable(False, False)
    # end the loop
    root.mainloop()


if __name__ == '__main__':
    main()