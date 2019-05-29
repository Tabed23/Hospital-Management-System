import tkinter.messagebox
from tkinter import *
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()


class Patient:

    def __init__(self, root):
        self.root = root
        # create a frame
        self.left = Canvas(root, width=700, height=720, bg='grey')
        self.left.pack(side=LEFT)

        self.right = Canvas(root, width=1300, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        # Heading of the window
        self.heading = Label(self.left, text="Patient Detail", font='italic 40 bold', fg='black', bg='grey')
        self.heading.place(x=0, y=0)
        # PATIENT NAME LABEL
        self.name = Label(self.left, text="Patient's Name", font='italic 12 bold', fg='black')
        self.name.place(x=0, y=100)

        # PATIENT AGE LABEL
        self.age = Label(self.left, text="Patient's Age", font='italic 12 bold', fg='black')
        self.age.place(x=0, y=140)

        # PATIENT GENDER LABEL
        self.gender = Label(self.left, text="Gender", font='italic 12 bold', fg='black')
        self.gender.place(x=0, y=180)

        # entry for all the Label
        # entry of name
        self.name_entry = Entry(self.left, width=30)
        self.name_entry.place(x=150, y=100)

        # entry of age
        self.age_entry = Entry(self.left, width=30)
        self.age_entry.place(x=150, y=140)

        # entry of gender
        self.gender_entry = Entry(self.left, width=30)
        self.gender_entry.place(x=150, y=180)

        # to make a sumbit button
        self.sumbit = Button(root, text="Add Patient", width=20, height=3, bg='steelblue', fg='white',
                             command=self.add_appointment)
        self.sumbit.place(x=160, y=340)

        # adding a display box
        self.box = Text(self.right, width=600, height=20)
        self.box.place(x=1, y=30)

        self.detail = Button(root, text='Show patients', width=20, height=3, bg='steelblue', fg='white',
                             command=self.show_patient)
        self.detail.place(x=310, y=340)

        self.delete_ = Button(root, text='Discharged  Patient', width=20, height=3, bg='steelblue', fg='white',
                              command=self.del_patient)
        self.delete_.place(x=20, y=340)

    def add_appointment(self):

        """
         check the input if valid also
        """
        # getting User Input
        Name = self.name_entry.get()
        Age = self.age_entry.get()
        Gender = self.gender_entry.get()

        # check if the input is empty
        if Name and Age and Gender:
            sql = "INSERT INTO patient(P_name,age,gender) VALUES(?,?,?)"
            c.execute(sql, (Name, Age, Gender))
            conn.commit()
            tkinter.messagebox.showinfo("appointment has bee set...!!")
        else:
            tkinter.messagebox.showinfo("Warning ", "Please Fill The the Requirements")

    def show_patient(self):

        self.name = Label(self.right, text="Name", font='italic 10 bold', fg='black', bg='steelblue')
        self.name.place(x=0, y=0)

        self.age = Label(self.right, text=" Age", font='italic 10 bold', fg='black', bg='steelblue')
        self.age.place(x=70, y=0)

        self.gender = Label(self.right, text="Gender", font='italic 10 bold', fg='black', bg='steelblue')
        self.gender.place(x=110, y=0)

        c.execute("SELECT P_name, age, gender FROM patient")
        for row in c.fetchall():
            self.box.insert(END, str(row) + '\n')

    def del_patient(self):

        self.gender_entry.destroy()
        self.age_entry.destroy()
        self.gender.destroy()
        self.age.destroy()
        self.heading = Label(self.left, text='Enter Patient Name', font='italic 40 bold', fg='black')
        self.heading.place(x=0, y=0)
        name_ = self.name_entry.get()
        if name_:
            c.execute("DELETE FROM patient WHERE P_name = ?", (name_,))
            conn.commit()
            tkinter.messagebox.showinfo("Patient has bee Discharged...!!")
