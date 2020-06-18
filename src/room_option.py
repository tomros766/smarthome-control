# author: Tomasz Rosiek
# e-mail: trosiek@student.agh.edu.pl

class RoomOption:
    name = None
    position = -1
    topic = None
    binary = False
    commands = None
    curr_val = None
    client = None

    def __init__(self, opts, initial, client):
        self.name = opts['name']
        self.position = opts['position']
        self.topic = opts['topic']
        self.binary = opts['binary']
        self.commands = [opts['message_one'], opts['message_two']]
        self.curr_val = initial[1]
        self.client = client

    def call(self, on_up):
        if on_up:
            self.client.publish(self.topic, self.commands[0], retain=self.binary)
        else:
            self.client.publish(self.topic, self.commands[1], retain=self.binary)
        if self.binary:
            self.curr_val = on_up
