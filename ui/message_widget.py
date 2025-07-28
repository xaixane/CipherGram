from datetime import datetime 
from textual.widgets import Static
from controllers.user import UserMessage

class MessageWidget(Static):
    def __init__(self,user_obj:dict,isUser:bool,**kwargs):
        super().__init__(**kwargs)
        self.user_obj=user_obj
        self.isUser = isUser

    def on_mount(self):
        self.add_class("messageWidget")
        userObject = UserMessage(self.user_obj["sender"],self.user_obj["message"],self.isUser,datetime.now()) 
        self.update(userObject.returnMessage())
