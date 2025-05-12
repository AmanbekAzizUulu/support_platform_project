import datetime

class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text
        self.timestamp = datetime.datetime.now().isoformat()

    def to_dict(self):
        return {
            'sender': self.sender,
            'text': self.text,
            'timestamp': self.timestamp
        }