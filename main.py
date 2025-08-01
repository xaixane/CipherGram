from textual.app import App, ComposeResult
from textual.widgets import Static,Header
from textual.containers import Vertical,Container
from ui.message_widget import MessageWidget
from ui.custom_input import CustomInput 
from controllers.messages import UserSubmitted
from services.telegram_service import TelegramService 
from controllers.telegram_event_handler import TelegramMessage
from ui.MessageScreen import MessageScreen
import asyncio

class CipherGram(App):
    CSS_PATH = "assets/main.tcss"
    def __init__(self,telegram_service,**kwargs):
        super().__init__(**kwargs)
        self.telegram_service = telegram_service
        self.message_screen = MessageScreen(id="MessageDisplay")

    def compose(self)->ComposeResult:
        yield Container(
            Header(show_clock=True),
            self.message_screen,
            CustomInput()
            ,id="main-container"
        )
    
    def on_mount(self):
        print("App mounted")
        self.title="󰏩 CipherGram v1"
        self.subtitle="Send and Recieve"
        self.telegram_service.app=self
        self.query_one("#MessageDisplay",Vertical).scroll_end(animate=False)
        asyncio.create_task(self.telegram_service.start_and_listen())

    async def on_user_submitted(self,event:UserSubmitted):
        await self.telegram_service.send_message(event.submitted_value)
        self.message_screen.add_message(sender=self.telegram_service.client_name,message=event.submitted_value,isUser=True)

    def on_telegram_message(self,event:TelegramMessage):
        self.message_screen.add_message(sender=event.sender,message=event.message,isUser=False)


async def main():
    telegram_service = TelegramService()
    await telegram_service.ensure_login()
    await CipherGram(telegram_service).run_async()


if __name__ == "__main__":
   asyncio.run(main()) 
