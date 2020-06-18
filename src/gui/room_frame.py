# author: Tomasz Rosiek
# e-mail: trosiek@student.agh.edu.pl

import tkinter as tk
from tkinter import ttk


class RoomFrame(ttk.Frame):
    room = None
    buttons = []

    def __init__(self, master, room):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.room = room
        self.init_window()

    def init_window(self):
        self.set_icons()

    def set_icons(self):
        self.buttons = []
        row = 0
        col = -1
        for opt in self.room.opts:
            if opt.binary:
                flag = True
            else:
                flag = False

            col = (col + 1) % 2
            if col == 0:
                row += 1
            if flag:
                label = f'{opt.name}\n'
                on_up = True
                if opt.curr_val:
                    on_up = False
                    label += opt.commands[1]
                elif opt.binary:
                    label += opt.commands[0]
                self.buttons.append(tk.Button(self, text=label,
                                              command=lambda name=opt.name, on=on_up: self.callback(name, on),
                                              width=8, height=4))
                self.buttons[-1].grid(row=row, column=col)
            else:
                if col == 1:
                    col = 0
                    row += 1
                self.buttons.append(tk.Button(self, text='\u25B2',
                                              command=lambda name=opt.name: self.room.call(name, True),
                                              width=8, height=4))
                self.buttons[-1].grid(row=row, column=col)
                row += 1
                self.buttons.append(tk.Button(self, text='\u25BC',
                                              command=lambda name=opt.name: self.room.call(name, False),
                                              width=8, height=4))
                self.buttons[-1].grid(row=row, column=col)
                tk.Label(self, text=opt.name).grid(row=row-1, column=1, rowspan=2)

    def callback(self, name, on_up):
        self.room.call(name, on_up)
        self.set_icons()

