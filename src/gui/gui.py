from tkinter import *

from src.gui.home import Home
from src.gui.login import Login
from src.room import Room
from src.gui.room_options import RoomOptions
import paho.mqtt.client as mqtt

class App(Tk):
    loginFrame = None
    homeFrame = None
    dict = {}

    def __init__(self, dict):
        Tk.__init__(self)
        self.dict = dict
        self.init_window()
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        self.mainloop()

    def init_window(self):
        self.loginFrame = Login(self)
        self.loginFrame.pack(padx=10, pady=10)

    def login(self, id, address):
        client = mqtt.Client(id)
        client.connect(address)
        client.loop_start()
        rooms = [Room(r['name'], r['buttons'], client) for r in self.dict]
        self.loginFrame.pack_forget()
        self.homeFrame = Home(self, rooms)
        self.homeFrame.pack(padx=10, pady=10)

    def logout(self):
        self.homeFrame.pack_forget()
        self.loginFrame.pack()


