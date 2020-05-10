from tkinter import *

from src.gui.home import Home
from src.gui.login import Login
from src.room import Room
from src.gui.room_options import RoomOptions


class App(Tk):
    loginFrame = None
    homeFrame = None

    def __init__(self):
        Tk.__init__(self)
        self.init_window()
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        self.mainloop()

    def init_window(self):
        self.loginFrame = Login(self)
        self.homeFrame = Home(self, [Room("pokoj", RoomOptions()), Room("pokoj1", RoomOptions()), Room("pokoj2", RoomOptions()), Room("Pokoj3", RoomOptions())])
        self.loginFrame.pack(padx=10, pady=10)

    def login(self):
        self.loginFrame.pack_forget()
        self.homeFrame.pack(padx=10, pady=10)

    def logout(self):
        self.homeFrame.pack_forget()
        self.loginFrame.pack()


