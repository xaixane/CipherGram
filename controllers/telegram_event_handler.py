from textual.message import Message

class TelegramMessage(Message):
    sender:str
    message:str

    def __init__(self,sender:str,message:str):
        super().__init__()
        self.sender=sender
        self.message=message
