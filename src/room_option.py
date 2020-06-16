class RoomOption:
    name = None
    position = -1
    topic = None
    binary = False
    commands = None
    curr_val = None
    client = None

    def __init__(self, opts, client):
        self.name = opts['name']
        self.position = opts['position']
        self.topic = opts['topic']
        self.binary = opts['binary']
        self.commands = [opts['message_one'], opts['message_two']]
        self.client = client
        self.client.on_message = self.on_message

    def on_message(self, client, user_data, message):
        if message.retain:
            msg = str(message.payload.decode("utf-8"))
            if msg == self.commands[0]:
                self.curr_val = True
            elif msg == self.commands[1]:
                self.curr_val = False

