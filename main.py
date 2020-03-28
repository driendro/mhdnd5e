import os
# Importacion de Kivy
import kivy
# Modulos de Kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

# Dimensiones de la ventana:
from kivy.config import Config
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)

from vistas.menu import MenuWid
from vistas.creature.listview import CreatureListWid
from vistas.creature.createview import CreatureCreateWid



class MainWid(ScreenManager):
    def __init__(self, *args, **kwargs):
        super(MainWid, self).__init__()
        # Control de Path
        self.APP_PATH = os.getcwd()
        self.DB_PATH = self.APP_PATH + '/database.db'

        self.MenuWid = MenuWid(self) #Screen: menu
        self.CreatureListWid = CreatureListWid(self) #Screen: creaturelist
        self.CreatureCreateWid = BoxLayout() #Screen : creaturecreate


        wid = Screen(name='menu')
        wid.add_widget(self.MenuWid)
        self.add_widget(wid)

        wid = Screen(name='creaturelist')
        wid.add_widget(self.CreatureListWid)
        self.add_widget(wid)

        wid = Screen(name='creaturecreate')
        wid.add_widget(self.CreatureCreateWid)
        self.add_widget(wid)

        self.goto_menu()

    def goto_menu(self):
        self.current = 'menu'

    def goto_creturelist(self):
        self.CreatureListWid.check_memory()
        self.current = 'creaturelist'
    
    def goto_creaturecreate(self):
        self.CreatureCreateWid.clear_widgets()
        wid = CreatureCreateWid(self)
        self.CreatureCreateWid.add_widget(wid)
        self.current = 'creaturecreate'
    
class MainApp(App):
    title = "Loot Monster Hunter"
    def build(self):
        return MainWid()

if __name__=='__main__':
    MainApp().run()