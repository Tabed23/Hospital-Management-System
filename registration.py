from patient import Patient
from Doctor import Doctor
from nurse import Nurse
from room import Room
from tkinter import *
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()


class Registraction:

    def __init__(self, root):
        self.root = root
        self.root.title("Registrations")
        self._canvas = Canvas(root, width=400, height=520, bg='grey')
        self._canvas.pack()

        self.patinet_ = Button(self._canvas, text="Paitent ", width=10, height=1, fg='black', bg='white',
                               command=self.patient)
        self.patinet_.place(x=5, y=5)
        self.doctor_ = Button(self._canvas, text="Doctor ", width=10, height=1, fg='black', bg='white',
                              command=self.doctor)
        self.doctor_.place(x=90, y=5)
        self.nurse_ = Button(self._canvas, text="Nurse ", width=10, height=1, fg='black', bg='white',
                             command=self.nurse)
        self.nurse_.place(x=180, y=5)

        self.room_ = Button(self._canvas, text="Rooms ", width=10, height=1, fg='black', bg='white',
                            command=self.room)
        self.room_.place(x=280, y=5)
        self.appoitment_doc = Button(self._canvas, text="Appointed Doctor", width=14, height=1, fg='black', bg='white',
                                     command=self.doctor_appointed)
        self.appoitment_doc.place(x=0, y=50)
        self.appoitment_nur = Button(self._canvas, text="Appointed Nurse", width=14, height=1, fg='black', bg='white',
                                     command=self.nurse_appointed)
        self.appoitment_nur.place(x=110, y=50)
        self.appoitment_room = Button(self._canvas, text="Appointed Rooms", width=14, height=1, fg='black', bg='white',
                                      command=self.room_appointed)
        self.appoitment_room.place(x=240, y=50)

    def patient(self):
        self._canvas.destroy()
        Patient(self.root)

    def doctor(self):
        self._canvas.destroy()
        Doctor(self.root)

    def nurse(self):
        self._canvas.destroy()
        Nurse(self.root)

    def room(self):
        self._canvas.destroy()
        Room(self.root)

    def doctor_appointed(self):
        box = Text(self._canvas, width=70, height=10)
        box.place(x=3, y=180)
        c.execute("SELECT p.P_name, p.gender , d.D_name FROM patient as p join doctor as d on d.D_id=p.P_id")
        for row in c.fetchall():
            box.insert(END, str(row) + '\n')

    def nurse_appointed(self):
        box = Text(self._canvas, width=70, height=10)
        box.place(x=3, y=180)
        c.execute("SELECT p.P_name, p.gender , n.N_name,n.Shift  FROM patient as p join nurse as n on n.N_id=p.P_id")
        for row in c.fetchall():
            box.insert(END, str(row) + '\n')

    def room_appointed(self):
        box = Text(self._canvas, width=70, height=10)
        box.place(x=3, y=180)
        c.execute("SELECT p.P_name , n.N_name,n.Shift, r.floor  FROM patient as p join nurse as n join room "
                  "as r on "
                  "n.N_id=p.P_id  and  n.N_id = r.R_id")
        for row in c.fetchall():
            box.insert(END, str(row) + '\n')
