import os
import sqlite3

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from db import db_create

# Cargamos el Archivo KV, donde esta el formato de la wid
Builder.load_file(os.getcwd()+'/vistas/menu.kv')

# Coneccion y Creacion de la db
def conectar_db(path):
    try:
        db_create(path)
    except Exception as e:
        print(e)

class MenuWid(BoxLayout):
    def __init__(self, mainwid, *args, **kwargs):
        super(MenuWid, self).__init__()
        self.mainwid = mainwid
    
    def regen_database(self):
        conectar_db(self.mainwid.DB_PATH)