from telethon import TelegramClient,events
from controllers.telegram_event_handler import TelegramMessage
from dotenv import load_dotenv
from os import getenv
import asyncio

load_dotenv()

class TelegramService:
    session_name:str
    target:str
    client:TelegramClient
    client_name:str
    target_name:str
    api_id:str
    api_hash:str
    
    def __init__(self)->None:
        self.session_name=getenv("SESSION_NAME")
        self.target=getenv("TARGET")
        self.api_id=getenv("API_ID")
        self.api_hash=getenv("API_HASH")
        self.client=TelegramClient(self.session_name,self.api_id,self.api_hash)
        self.client_name="unknown"
        self.app=None

    async def start_and_listen(self):
        await self.client.start()
        client_obj = await self.client.get_me()
        self.client_name=client_obj.username
        target_obj = await self.client.get_entity(self.target)
        self.target_name = target_obj.username
        
        #This is an event handler which listens for the new message of the target
        self.client.add_event_handler(self.on_new_message,events.NewMessage(self.target_name))

        await self.client.run_until_disconnected()
    
    async def send_message(self,message_str:str):
        message_status = await self.client.send_message(self.target,message_str)    
    
    async def get_username_by_message(self,message):
        message_sender = await message.get_sender()
        message_sender_username = getattr(message_sender,'username','unknown')
        return message_sender_username

    async def read_messages(self):
        previous_messages = []
        async for message in self.client.iter_messages(self.target,limit=5):
            if not message or not message.text or message.media:
                continue
            username = await self.get_username_by_message(message)
            print(username)
            previous_messages.append({"sender":username,"message":message.text})
        return previous_messages
    
    async def on_new_message(self,event):
        if not event.message.text or event.message.media:
            return
        
        sender = await event.get_sender()
        username = getattr(sender,"username","unknown")
        text = event.message.text
        print(text)
        if self.app:
           await self.app.post_message(TelegramMessage(username,text))
    

