from textual.widgets import Input,Button
from textual.widget import Widget
from textual.containers import Horizontal
from controllers.messages import UserSubmitted 

class CustomInput(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.input=Input(placeholder='Enter your text here')
        self.button=Button("  󰏩 ",id="SubmitButton")

    def compose(self):
        yield Horizontal(
            self.input,
            self.button,
            id="CustomInputContainer"
        )
    def on_input_submitted(self,event:Input.Submitted):
        if event.value.split():
            self.post_message(UserSubmitted(self,event.value))
            self.input.value = ""

    def on_button_pressed(self):
        if self.input.value.split():
            self.post_message(UserSubmitted(self,self.input.value))
            self.input.value = ""
