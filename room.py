from tkinter import *
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()


class Room:

    def __init__(self, root):
        self.root = root
        self.root.title("Rooms")
        self.canvas = Canvas(root, width=600, height=500, bg='grey')
        self.canvas.pack()
        self.floor = Label(self.canvas, text="Floor No", font='italic 12 bold', fg='black', bg='grey')
        self.floor.place(x=0, y=150)

        self.floor_entrty = Entry(self.canvas, width=30)
        self.floor_entrty.place(x=150, y=150)
        self.sumbit_add_room = Button(root, text="Add Room", width=20, height=2, fg='steelblue',
                                      command=self.add_rooms)
        self.sumbit_add_room.place(x=10, y=200)

        self.sumbit_show_rooms = Button(root, text="Show Rooms", width=20, height=2, fg='steelblue',
                                        command=self.show_rooms)
        self.sumbit_show_rooms.place(x=150, y=200)

    def add_rooms(self):
        floor = self.floor_entrty.get()

        if floor == 'Ground' or floor == 'Top' or floor == 'Second' or floor == 'Third':
            sql = "INSERT INTO room(floor) VALUES(?)"
            c.execute(sql, (floor,))
            conn.commit()
            tkinter.messagebox.showinfo("A Room has bee set...!!")
        else:
            tkinter.messagebox.showinfo("No Such Floor")

    def show_rooms(self):
        floor = Label(self.canvas, text="Room Floor", font='italic 8 bold', fg='black')
        floor.place(x=1, y=280)
        box = Text(self.canvas, width=70, height=10)
        box.place(x=3, y=310)
        c.execute("SELECT floor FROM room")
        for row in c.fetchall():
            box.insert(END, str(row) + '\n')


