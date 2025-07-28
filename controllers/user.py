from datetime import datetime
from textual.app import App, ComposeResult
from textual.widgets import Static

class UserMessage:
    username:str
    message_str:str
    isUser:bool
    timestamp_str:datetime

    def __init__(self,username:str,message_str:str,isUser:bool,timestamp_str:datetime):
        self.username=username
        self.message_str=message_str
        self.timestamp_str=timestamp_str
        self.isUser=isUser

    def returnMessage(self)->str:        
        timestamp = self.timestamp_str.strftime("%H:%M %p")
        color = 'cyan' if self.isUser else '#E048A5'
        return f"[gray][{timestamp}][/][{color}] {self.username}[/]: {self.message_str}"


