import os
# Importacion de Kivy
import kivy
# Modulos de Kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

# Dimensiones de la ventana:
from kivy.config import Config
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)

from vistas.menu import MenuWid



class MainWid(ScreenManager):
    def __init__(self, *args, **kwargs):
        super(MainWid, self).__init__()
        # Control de Path
        self.APP_PATH = os.getcwd()
        self.DB_PATH = self.APP_PATH + '/database.db'

        self.MenuWid = MenuWid(self)


        wid = Screen(name='menu')
        wid.add_widget(self.MenuWid)
        self.add_widget(wid)

        self.goto_menu()

    def goto_menu(self):
        self.current = 'menu'

class MainApp(App):
    title = "Loot Monster Hunter"
    def build(self):
        return MainWid()

if __name__=='__main__':
    MainApp().run()