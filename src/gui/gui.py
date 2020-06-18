# author: Tomasz Rosiek
# e-mail: trosiek@student.agh.edu.pl

from tkinter import *

from src.gui.home import Home
from src.gui.login import Login
from src.room import Room
import paho.mqtt.client as mqtt


class App(Tk):
    loginFrame = None
    homeFrame = None
    dict = {}
    client = None
    current_state = {}

    def __init__(self, dict):
        Tk.__init__(self)
        self.dict = dict
        self.current_state = {r['name']: {o['topic']: ([o['message_one'], o['message_two']], False) for o in r['buttons']} for r in self.dict}
        self.init_window()
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        self.mainloop()

    def init_window(self):
        self.loginFrame = Login(self)
        self.loginFrame.pack(padx=10, pady=10)

    def login(self, id, address):
        self.client = mqtt.Client(id)
        self.client.on_message = self.on_message
        self.client.connect(address)
        self.client.loop_start()
        self.client.subscribe('#')
        self.loginFrame.pack_forget()
        self.update_state()

    def logout(self):
        self.homeFrame.pack_forget()
        self.loginFrame.pack()

    def on_closing(self):
        self.client.loop_stop()
        self.destroy()

    def on_message(self, client, userdata, message):
        print(message.topic, str(message.payload.decode("utf-8")))
        for r, t in self.current_state.items():
            for topic in t:
                if topic == message.topic:
                    option_commands = self.current_state[r][topic][0]
                    if message.retain:
                        msg = str(message.payload.decode("utf-8"))
                        if msg == option_commands[0]:
                            tmp = {topic: (option_commands, True)}
                            self.current_state[r].update(tmp)
                            self.update_state()

    def update_state(self):
        rooms = [Room(r['name'], r['buttons'], self.current_state[r['name']], self.client) for r in self.dict]
        if self.homeFrame is not None:
            self.homeFrame.pack_forget()
        self.homeFrame = Home(self, rooms)
        self.homeFrame.pack(padx=10, pady=10)
