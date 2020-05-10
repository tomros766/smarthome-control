from tkinter import *


class Login(Frame):
    id = None
    passwd = None
    login = None

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.id = StringVar()
        self.passwd = StringVar()
        self.master.title("Login")

        houseidlabel = Label(self, text="HouseID: ")
        houseid = Entry(self, textvariable=self.id)
        psswdlabel = Label(self, text="Password: ")
        psswd = Entry(self, show='\u2022', textvariable=self.passwd)
        self.login = Button(self, text="Login", command=self.click, state="disabled")

        self.id.trace("rw", callback=self.check)
        self.passwd.trace("rw", callback=self.check)

        houseidlabel.grid(row=0, column=0, sticky='W')
        houseid.grid(row=0, column=1, sticky='W')
        psswdlabel.grid(row=1, column=0, pady=10, sticky='W')
        psswd.grid(row=1, column=1, sticky='W')
        self.login.grid(row=2, column=0, columnspan=2)
        self.pack(padx=10, pady=10)

    def click(self):
        self.master.login()

    def check(self, *args):
        if self.id.get() != "" and self.passwd.get() != "":
            self.login['state'] = 'active'
        else:
            self.login['state'] = 'disabled'




