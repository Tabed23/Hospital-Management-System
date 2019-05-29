from patient import Patient
from tkinter import *


class Emergency:

    def __init__(self, root):
        self.root = root
        self.root.title('Emergency Watt')
        self._canvas = Canvas(root,  width=500, height=420, bg='grey')
        self._canvas.pack()

        self.heading = Label(self._canvas, text="Emergency Watt", font='italic 20 bold', fg='black', bg='grey')
        self.heading.place(x=40, y=0)

        self.patinet = Button(self._canvas, text="Add Emergency Patient",fg='black', bg='white',command=self.add_patient)
        self.patinet.place(x=40, y=100)

    def add_patient(self):
        self._canvas.destroy()
        self.heading.destroy()
        Patient(self.root)