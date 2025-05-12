from person import Person

class SupportOperator(Person):
    def __init__(self, *args):
        super().__init__(*args)
        self.active_chats = 0