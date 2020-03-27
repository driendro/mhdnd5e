import os
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Cargamos el Archivo KV, donde esta el formato de la wid
Builder.load_file(os.getcwd()+'/vistas/menu.kv')

class MenuWid(BoxLayout):
    def __init__(self, mainwid, *args, **kwargs):
        super(MenuWid, self).__init__()
        self.mainwid = mainwid