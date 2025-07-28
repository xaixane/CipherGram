from textual.containers import Vertical
from ui.message_widget import MessageWidget
class MessageScreen(Vertical):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.messageHistory = []

    def add_message(self, sender:str, message:str,isUser:bool):
        msg_obj={"sender":sender,"message":message}
        chat_message = MessageWidget(msg_obj,isUser)
        chat_message.add_class("message")
        self.mount(chat_message)
        self.messageHistory.append(chat_message)
        self.scroll_end(animate=False)
