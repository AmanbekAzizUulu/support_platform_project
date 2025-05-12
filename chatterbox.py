from message import Message

class Chatterbox:
    def __init__(self, user, operator):
        self.user = user
        self.operator = operator
        self.messages = []
        self.closed = False
        self.csat = None

    def add_message(self, sender, text):
        self.messages.append(Message(sender, text))

    def close_chat(self):
        self.closed = True
        self.operator.active_chats -= 1

    def rate_chat(self, score):
        if self.closed:
            self.csat = score

    def to_dict(self):
        return {
            'user': self.user.full_name,
            'operator': self.operator.full_name,
            'messages': [m.to_dict() for m in self.messages],
            'closed': self.closed,
            'csat': self.csat
        }