###############################################
# CS 21B Intermediate Python Programming Lab #6
# Topics: gui
# Description: This program creates a simple app
#              that allows the user to convert
#              kilometers to miles - the output
#              of which will show up as an analog
#              message.
# Input: kilometers
# Output: miles
# Version: 3.7.0
# Development Environment:  IDLE
# Developer:  Aadithya Anumala
# Student ID: 20365071
# Date:  05/28/19
###############################################

from tkinter import *
from tkinter import messagebox

KILO_TO_MILE = 0.621371192

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.entrythingy = Entry()
        
        # here is the application variable
        self.contents = StringVar()
        # set it to some value
        self.contents.set("Enter number of kilometers")
        # tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents

        self.hi_there = Button(self)
        self.hi_there["text"] = "Calculate to miles"
        self.hi_there["command"] = self.compute
        self.hi_there.pack(side = "bottom")

        self.quit = Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        self.entrythingy.pack()

    def compute(self):
        kilo = self.contents.get()
        fail = False
        try:
            kilo = float(kilo)
            mile = kilo*KILO_TO_MILE
        except:
            fail = True
            messagebox.showinfo("Answering your request",
                                "improper input - please enter a float")
        if not fail:
            messagebox.showinfo("Answering your request", '%.2f'%(mile) +
                                str(" miles"))

root = Tk()
app = App(master=root)
app.mainloop()
