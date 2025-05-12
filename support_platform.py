import json
import random
from chatterbox import Chatterbox
 
class SupportPlatform:
    def __init__(self):
        self.operators = []
        self.users = []
        self.chats = []

    def add_operator(self, operator):
        self.operators.append(operator)

    def add_user(self, user):
        self.users.append(user)

    def create_chat(self, user):
        available_ops = [op for op in self.operators if op.active_chats == 0]
        if not available_ops:
            return None
        operator = random.choice(available_ops)
        operator.active_chats += 1
        
        chat = Chatterbox(user, operator)
        self.chats.append(chat)
        return chat

    def export_chats(self):
        data = [chat.to_dict() for chat in self.chats]
        print(json.dumps(data, indent=2, ensure_ascii=False))

    def export_chats_by_operator(self, operator_name):
        data = [c.to_dict() for c in self.chats if c.operator.full_name == operator_name]
        print(json.dumps(data, indent=2, ensure_ascii=False))

    def export_chats_by_user(self, user_name):
        data = [c.to_dict() for c in self.chats if c.user.full_name == user_name]
        print(json.dumps(data, indent=2, ensure_ascii=False))

    def export_profiles(self):
        data = {
            'operators': [op.to_dict() for op in self.operators],
            'users': [usr.to_dict() for usr in self.users]
        }
        print(json.dumps(data, indent=2, ensure_ascii=False))
