from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.label import Label

from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '640')

import cv2

class Manager(ScreenManager):
    pass


class Menu(Screen):
    pass

class MyDetection(Screen):
    pass


class MainApp(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    MainApp().run()