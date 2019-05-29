from tkinter import *
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()


class Doctor:

    def __init__(self, root):
        root.title("Doctor")
        self.left = Canvas(root, width=900, height=500, bg='grey')
        self.left.pack()
        self.heading = Label(self.left, text="Doctor Detail", font='italic 40 bold', fg='black', bg='grey')
        self.heading.place(x=0, y=0)

        self.heading = Label(self.left, text="Doctor Detail", font='italic 40 bold', fg='black', bg='grey')
        self.heading.place(x=0, y=0)
        self.dname = Label(self.left, text="Doctor's Name", font='italic 12 bold', fg='black')
        self.dname.place(x=0, y=100)

        self.phone = Label(self.left, text="Phone", font='italic 12 bold', fg='black')
        self.phone.place(x=0, y=140)

        self.Specialization = Label(self.left, text="Specialization", font='italic 12 bold', fg='black')
        self.Specialization.place(x=0, y=180)
        self.salary = Label(self.left, text="salary", font='italic 12 bold', fg='black')
        self.salary.place(x=0, y=220)

        self.dname_entry = Entry(self.left, width=30)
        self.dname_entry.place(x=150, y=100)

        self.phone_entry = Entry(self.left, width=30)
        self.phone_entry.place(x=150, y=140)

        self.Specialization_entry = Entry(self.left, width=30)
        self.Specialization_entry.place(x=150, y=180)

        self.salary_entry = Entry(self.left, width=30)
        self.salary_entry.place(x=150, y=220)
        self.sumbit_add_doc = Button(root, text="Add a new Doctor", width=20, height=2, fg='steelblue',
                                     command=self.add_doctor)
        self.sumbit_add_doc.place(x=10, y=300)

        self.sumbit_show_doc = Button(root, text="Show Doctor", width=20, height=2, fg='steelblue',
                                      command=self.show_doctor)
        self.sumbit_show_doc.place(x=150, y=300)
        self.delete_ = Button(root, text='Doctor Leave', width=20, height=2, fg='steelblue',
                              command=self.del_doctor)
        self.delete_.place(x=290, y=300)

    def add_doctor(self):
        dname = self.dname_entry.get()
        phone = self.phone_entry.get()
        Specialization = self.Specialization_entry.get()
        salary = self.salary_entry.get()
        if dname and phone and Specialization and salary:
            sql = "INSERT INTO doctor(D_name,Phone,Specialization,salary) VALUES(?,?,?,?)"
            c.execute(sql, (dname, phone, Specialization, salary))
            conn.commit()
            tkinter.messagebox.showinfo("A New Doctor has bee set...!!")

        else:
            tkinter.messagebox.showinfo("Warning ", "Please Fill The the Requirements")

    def show_doctor(self):
        self.sumbit_add_doc.destroy()
        self.sumbit_show_doc.destroy()
        self.delete_.destroy()
        name = Label(self.left, text="Doctor Name", font='italic 8 bold', fg='black')
        name.place(x=1, y=280)
        phone = Label(self.left, text="Doctor Phone no", font='italic 8 bold', fg='black')
        phone.place(x=90, y=280)
        Specialization = Label(self.left, text="Specialization", font='italic 8 bold', fg='black')
        Specialization.place(x=220, y=280)
        salary = Label(self.left, text="salary", font='italic 8 bold', fg='black')
        salary.place(x=345, y=280)
        box = Text(self.left, width=70, height=10)
        box.place(x=3, y=310)
        c.execute("SELECT D_name, Phone, Specialization,salary FROM doctor")
        for row in c.fetchall():
            box.insert(END, str(row) + '\n')

    def del_doctor(self):

        self.phone.destroy()
        self.phone_entry.destroy()
        self.Specialization.destroy()
        self.Specialization_entry.destroy()
        self.salary_entry.destroy()
        self.salary.destroy()

        name_ = self.dname_entry.get()
        if name_:
            c.execute("DELETE FROM doctor WHERE D_name = ?", (name_,))
            conn.commit()
            tkinter.messagebox.showinfo("Doctor has Leave...!!")
