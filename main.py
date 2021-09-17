from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout

class LoginLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.loginButton = Button(
            text= 'Login',
            size_hint= (0.3,0.1),
            pos_hint= {'x': 0.35, 'y': 0.4}
        )
        self.signupButton = Button(
            text= 'Sign Up',
            size_hint= (0.3,0.1),
            pos_hint= {'x': 0.35, 'y': 0.25}
        )
        self.mainTitle = Label(
            text= 'School Bus Mate',
            font_size= (72),
            pos_hint= {'x': 0, 'y': 0.27}
        )
        self.add_widget(self.loginButton)
        self.add_widget(self.signupButton)
        self.add_widget(self.mainTitle)


class MainApp(App):
    def build(self):
        return LoginLayout()

MainApp().run()
