from src.room_option import RoomOption
import paho.mqtt.client as mqtt


class Room:
    name = ""
    opts = None
    client = None

    def __init__(self, name, opts, client):
        self.name = name
        self.opts = [RoomOption(opt, client) for opt in opts]
        self.client = client

    def find_opt(self, name):
        print(name)
        return list(filter(lambda o: o.name == name, self.opts))[0]

    def subscribe(self, name):
        option = self.find_opt(name)
        self.client.subscribe(option.topic)

    def call(self, name, on_up: bool):
        option = self.find_opt(name)
        print(option.topic)
        self.client.publish(option.topic, option.commands[0], retain=option.binary)
        if option.curr_val is not None and option.binary:
            option.curr_val = on_up

