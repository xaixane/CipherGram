from textual.message import Message

class UserSubmitted(Message,bubble=True):
    def __init__(self, sender, submitted_value:str)->None:
        super().__init__()
        self.sender = sender
        self.submitted_value=submitted_value


