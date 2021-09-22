__version__ = '0.0.1'

import kivy
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.theming import ThemeManager
from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivymd.uix.textfield import MDTextField
from os import walk
# from myfirebase import MyFirebase
from datetime import datetime
import kivy.utils
from kivy.utils import platform
import requests
import json
import traceback
from kivy.graphics import Color, RoundedRectangle
import random

theme = 'Light'

class LoginScreen(Screen):
    pass

class LoginType(Screen):
    pass

class HomeScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        # Window.clear_color = (1,1,171/255,1)
        self.theme_cls.theme_style = theme
        self.theme_cls.primary_palette = 'Amber'
        return Builder.load_file('main.kv')

    def change_screen(self, screen_name, direction='forward', mode=""):
        # Get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager']
        # print(direction, mode)
        # If going backward, change the transition. Else make it the default
        # Forward/backward between pages made more sense to me than left/right
        if direction == 'forward':
            mode = "push"
            direction = 'left'
        elif direction == 'backwards':
            direction = 'right'
            mode = 'pop'
        elif direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return

        screen_manager.transition = CardTransition(direction=direction, mode=mode)
        screen_manager.current = screen_name


if __name__ == '__main__':
    MainApp().run()
