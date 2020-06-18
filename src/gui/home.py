# author: Tomasz Rosiek
# e-mail: trosiek@student.agh.edu.pl

from tkinter import ttk

from src.gui.room_frame import RoomFrame


class Home(ttk.Notebook):
    rooms = []
    opts = None
    active_room = None
    active_room_name = None
    active_room_label = None

    def __init__(self, master, rooms):
        ttk.Notebook.__init__(self, master)
        self.master = master
        self.rooms = rooms
        self.init_window()

    def init_window(self):
        self.master.title("SH Control")
        for room in self.rooms:
            self.add(RoomFrame(self, room), text=room.name)
        self.pack(expand=1, fill='both')

