# author: Tomasz Rosiek
# e-mail: trosiek@student.agh.edu.pl

from src.room_option import RoomOption


class Room:
    name = ""
    opts = None

    def __init__(self, name, opts, initial, client):
        self.name = name
        self.opts = [RoomOption(opt, initial[opt['topic']], client) for opt in opts]

    def find_opt(self, name):
        return list(filter(lambda o: o.name == name, self.opts))[0]

    def call(self, name, on_up: bool):
        option = self.find_opt(name)
        option.call(on_up)

