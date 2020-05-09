from tkinter import *
from PIL import Image, ImageTk


class RoomOptions:
    active_room = None
    alarm_off = None
    alarm_on = None
    blinds_down = None
    blinds_up = None
    door_locked = None
    door_unlocked = None
    lights_off = None
    lights_on = None
    heat_up = None
    heat_down = None

    alarm_img = None
    blinds_img = None
    door_img = None
    lights_img = None

    alarm_ison = False
    blinds_aredown = False
    door_islocked = False
    lights_areoff = False

    def __init__(self):
        self.alarm_off = ImageTk.PhotoImage(Image.open("img/alarm_off.png").resize((64, 64), Image.ANTIALIAS))
        self.alarm_on = ImageTk.PhotoImage(Image.open("img/alarm_on.png").resize((64, 64), Image.ANTIALIAS))
        self.blinds_down = ImageTk.PhotoImage(Image.open("img/blinds_down.png").resize((64, 64), Image.ANTIALIAS))
        self.blinds_up = ImageTk.PhotoImage(Image.open("img/blinds_up.png").resize((64, 64), Image.ANTIALIAS))
        self.door_locked = ImageTk.PhotoImage(Image.open("img/door_locked.png").resize((64, 64), Image.ANTIALIAS))
        self.door_unlocked = ImageTk.PhotoImage(Image.open("img/door_unlocked.png").resize((64, 64), Image.ANTIALIAS))
        self.lights_off = ImageTk.PhotoImage(Image.open("img/lights_off.png").resize((64, 64), Image.ANTIALIAS))
        self.lights_on = ImageTk.PhotoImage(Image.open("img/lights_on.png").resize((64, 64), Image.ANTIALIAS))
        self.alarm_img = self.alarm_off
        self.blinds_img = self.blinds_down
        self.door_img = self.door_unlocked
        self.lights_img = self.lights_on

        self.heat_down = ImageTk.PhotoImage(Image.open("img/heat_down.png").resize((64, 64), Image.ANTIALIAS))
        self.heat_up = ImageTk.PhotoImage(Image.open("img/heat_up.png").resize((64, 64), Image.ANTIALIAS))

    def change_alarm(self):
        if self.alarm_ison:
            self.alarm_ison = False
            self.alarm_img = self.alarm_off
        else:
            self.alarm_ison = True
            self.alarm_img = self.alarm_on

    def change_blinds(self):
        if self.blinds_aredown:
            self.blinds_aredown = False
            self.blinds_img = self.blinds_down
        else:
            self.blinds_aredown = True
            self.blinds_img = self.blinds_up

    def change_door(self):
        if self.door_islocked:
            self.door_islocked = False
            self.door_img = self.door_unlocked
        else:
            self.door_islocked = True
            self.door_img = self.door_locked

    def change_lights(self):
        if self.lights_areoff:
            self.lights_areoff = False
            self.lights_img = self.lights_on
        else:
            self.lights_areoff = True
            self.lights_img = self.lights_off









