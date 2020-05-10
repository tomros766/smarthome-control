class Room:
    name = ""
    opts = None
    temperature = 10

    def __init__(self, name, opts):
        self.name = name
        self.opts = opts

    def change_alarm(self):
        self.opts.change_alarm()

    def change_blinds(self):
        self.opts.change_blinds()

    def change_door(self):
        self.opts.change_door()

    def copy(self):
        return Room(self.name, self.opts)

