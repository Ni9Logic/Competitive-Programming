from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput


class anchor_layout(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lab = Label(
            text = 'Enter your name: '
        )
        self.add_widget(self.lab)
        self.text_ip = TextInput()
        self.add_widget(self.text_ip)
        

class fbr_generator(App):
    def build(self):
        return anchor_layout()
    
    
if __name__ == '__main__':
    app = fbr_generator()
    app.run()
    