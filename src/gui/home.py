from tkinter import *

from src.gui.room_options import RoomOptions


def change_door(room, button):
    room.opts.change_door()
    button['image'] = room.opts.door_img


def change_alarm(room, button):
    room.opts.change_alarm()
    button['image'] = room.opts.alarm_img


def change_blinds(room, button):
    room.opts.change_blinds()
    button['image'] = room.opts.blinds_img


def change_lights(room, button):
    room.opts.change_lights()
    button['image'] = room.opts.lights_img


def heat_up(room, label):
    room.temperature += 0.5
    label['text'] = str(room.temperature)+"\u00b0" + "C"


def heat_down(room, label):
    room.temperature -= 0.5
    label['text'] = str(room.temperature)+"\u00b0" + "C"


class Home(Frame):
    rooms = []
    opts = None
    active_room = None
    active_room_name = None
    active_room_label = None
    alarm = None
    blinds = None
    door = None
    lights = None

    def __init__(self, master, rooms):
        Frame.__init__(self, master)
        self.master = master
        self.rooms = rooms
        self.opts = RoomOptions()
        self.init_window()

    def init_window(self):
        self.master.title("SH Control")
        logout = Button(self, text="Logout", command=self.master.logout)
        logout.grid(row=0, column=1, sticky="NE")
        self.active_room_name = StringVar()
        self.active_room_name.set(self.rooms[0].name)
        rooms_dropdown = OptionMenu(self, self.active_room_name, *[room.name for room in self.rooms])
        self.active_room_name.trace("w", callback=self.callback)
        rooms_dropdown.grid(row=0, column=0)

        self.active_room = self.rooms[0]
        self.active_room_label = Label(self, text=self.active_room.name)
        self.active_room_label.grid(row=1, column=0, columnspan=3)
        self.set_icons()

    def change_room(self, room_num):
        print("clicked", self.rooms[room_num].name)
        self.active_room = self.rooms[room_num]
        self.active_room_label['text'] = self.rooms[room_num].name

    def callback(self, *args):
        self.active_room_label.configure(text=self.active_room_name.get())
        self.active_room = [room for room in self.rooms if room.name == self.active_room_name.get()][0]
        self.set_icons()

    def set_icons(self):
        lights = Button(self, image=self.active_room.opts.lights_img,
                        command=lambda: change_lights(self.active_room, lights))
        lights.grid(row=2, column=0)

        blinds = Button(self, image=self.active_room.opts.blinds_img,
                        command=lambda: change_blinds(self.active_room, blinds))
        blinds.grid(row=2, column=1)
        door = Button(self, image=self.active_room.opts.door_img, command=lambda: change_door(self.active_room, door))
        door.grid(row=3, column=1)

        alarm = Button(self, image=self.active_room.opts.alarm_img,
                       command=lambda: change_alarm(self.active_room, alarm))
        alarm.grid(row=3, column=0)

        temperature = Label(self, text=(str(self.active_room.temperature)+"\u00b0" + "C"), font=("System", 25))
        temperature.grid(row=4, rowspan=2, column=1)

        heat_plus = Button(self, image=self.active_room.opts.heat_up,
                           command=lambda: heat_up(self.active_room, temperature))
        heat_plus.grid(row=4, column=0)
        heat_minus = Button(self, image=self.active_room.opts.heat_down,
                            command=lambda: heat_down(self.active_room, temperature))
        heat_minus.grid(row=5, column=0)

