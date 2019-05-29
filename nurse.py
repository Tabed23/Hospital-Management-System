from tkinter import *
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()


class Nurse:

    def __init__(self, root):
        self.root = root
        self.root.title("Nurse")
        self.canvas = Canvas(root, width=600, height=500, bg='grey')
        self.canvas.pack()
        self.heading = Label(self.canvas, text="Nurse Detail", font='italic 40 bold', fg='black', bg='grey')
        self.heading.place(x=0, y=0)

        self.name = Label(self.canvas, text="Nurse Name", font='italic 12 bold', fg='black', bg='grey')
        self.name.place(x=0, y=100)
        self.shift = Label(self.canvas, text="Nurse Shift", font='italic 12 bold', fg='black', bg='grey')
        self.shift.place(x=0, y=150)

        self.name_entry = Entry(self.canvas, width=30)
        self.name_entry.place(x=150, y=100)

        self.shift_entry = Entry(self.canvas, width=30)
        self.shift_entry.place(x=150, y=150)

        self.sumbit_add_nurse = Button(root, text="Add a new Nurse", width=20, height=2, fg='steelblue',
                                       command=self.add_nurse)
        self.sumbit_add_nurse.place(x=10, y=200)

        self.sumbit_show_nurse = Button(root, text="Show Nurse", width=20, height=2, fg='steelblue',
                                        command=self.show_nurse)
        self.sumbit_show_nurse.place(x=150, y=200)
        self.delete_ = Button(root, text='Fire a Nurse', width=20, height=2, fg='steelblue',
                              command=self.del_nurse)
        self.delete_.place(x=290, y=200)

    def add_nurse(self):
        name = self.name_entry.get()
        shift = self.shift_entry.get()

        if name and shift:
            sql = "INSERT INTO nurse(N_name,Shift) VALUES(?,?)"
            c.execute(sql, (name, shift))
            conn.commit()
            tkinter.messagebox.showinfo("A New Doctor has bee set...!!")
        else:
            tkinter.messagebox.showinfo("Warning ", "Please Fill The the Requirements")

    def show_nurse(self):
        name = Label(self.canvas, text="Nurse Name", font='italic 8 bold', fg='black')
        name.place(x=1, y=280)
        shift = Label(self.canvas, text="Nurse Shuft", font='italic 8 bold', fg='black')
        shift.place(x=90, y=280)
        box = Text(self.canvas, width=70, height=10)
        box.place(x=3, y=310)
        c.execute("SELECT N_name, Shift FROM nurse")
        for row in c.fetchall():
            box.insert(END, str(row) + '\n')

    def del_nurse(self):
        self.shift.destroy()
        self.shift_entry.destroy()
        name = self.name_entry.get()
        if name:
            c.execute("DELETE FROM nurse WHERE N_name = ?", (name,))
            conn.commit()
            tkinter.messagebox.showinfo("Nurse has Been Fired...!!")


