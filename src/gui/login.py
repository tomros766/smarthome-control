# author: Tomasz Rosiek
# e-mail: trosiek@student.agh.edu.pl

from tkinter import *


class Login(Frame):
    id = None
    address = None
    login = None

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.id = StringVar()
        self.address = StringVar()
        self.master.title("Connect")

        idlabel = Label(self, text="ClientID: ")
        id = Entry(self, textvariable=self.id)
        addresslabel = Label(self, text="Broker address: ")
        address = Entry(self, textvariable=self.address)
        self.login = Button(self, text="Connect", command=self.click, state="disabled")

        self.id.trace("rw", callback=self.check)
        self.address.trace("rw", callback=self.check)

        idlabel.grid(row=0, column=0, sticky='W')
        id.grid(row=0, column=1, sticky='W')
        addresslabel.grid(row=1, column=0, pady=10, sticky='W')
        address.grid(row=1, column=1, sticky='W')
        self.login.grid(row=2, column=0, columnspan=2)
        self.pack(padx=10, pady=10)

    def click(self):
        self.master.login(self.id.get(), self.address.get())

    def check(self, *args):
        if self.id.get() != "" and self.address.get() != "":
            self.login['state'] = 'active'
        else:
            self.login['state'] = 'disabled'




