import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.config import Config
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)

class MainWid(ScreenManager):
    pass

class MainApp(App):
    title = "Loot Monster Hunter"
    def build(self):
        return MainWid()

if __name__=='__main__':
    MainApp().run()