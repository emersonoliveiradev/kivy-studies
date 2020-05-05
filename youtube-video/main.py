from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


from kivy.uix.label import Label
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import ListProperty, StringProperty, NumericProperty




class Manager(ScreenManager):
    pass

class Login(Screen):
    pass

class Menu(Screen):
    pass

class Botao(ButtonBehavior, Label):
    cor = ListProperty([0.1, 0.5, 0.7, 1])
    def __init(self, **kwargs):
        super(Botao, self).__init__(**kwargs)

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()

    def atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.cor)
            Ellipse(size=(self.height, self.height), pos=self.pos)
            Ellipse(size=(self.height, self.height), pos=(self.x + self.width - self.height, self.y))
            Rectangle(size=(self.width - self.height, self.height), pos=(self.x + self.height / 2.0, self.y))




class Tasks(Screen):
    def __init__(self, tasks=[], **kwargs):
        super().__init__(**kwargs)
        for tarefa in tasks:
            self.ids.box_scroll.add_widget(Task(text=tarefa))

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        # print(key)
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box_scroll.add_widget(Task(text=texto))
        self.ids.texto.text = ''

class Task(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class MainApp(App):
    def build(self):
        return Manager()

MainApp().run()

"""
<Botao@ButtonBehavior+Label>:
    canvas.before:
        Color:
            rgba: 0.1, 0.5, 0.7, 1
        Ellipse:
            pos: self.pos
            size: self.height, self.height
        Ellipse:
            pos: self.x + self.width - self.height, self.y
            size: self.height, self.height
        Rectangle:
            pos: self.x + self.height / 2.0, self.y
            size: self.width - self.height, self.height"""