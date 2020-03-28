import os
import sqlite3

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


# Cargamos el Archivo KV, donde esta el formato de la wid
Builder.load_file(os.getcwd()+'/vistas/creature/createview.kv')

class CreatureCreateWid(BoxLayout):
    '''
    Esta Vista, muestra el formulario para crear una criatura, y agregarla a
    la db
    '''
    def __init__(self, mainwid, *args, **kwargs):
        super(CreatureCreateWid, self).__init__()
        self.mainwid = mainwid

    def insert_data(self):
        d1 = self.ids.ti_nombre.text
        d2 = self.ids.ti_carve.text
        d3 = self.ids.ti_capture.text
        d4 = self.ids.ti_cr.text
        s1= 'INSERT INTO "main"."loot_criatura"(nombre, carves, capture, cr)'
        s2= 'VALUES("%s", %s, %s, %s)' %(d1, d2, d3, d4)
        try:
            con = sqlite3.connect(self.mainwid.DB_PATH)
            cursor = con.cursor()
            cursor.execute(s1+' '+s2)
            con.commit()
            con.close()
            self.mainwid.goto_creturelist()
        except Exception as e:
            print(e)

    
    def back_to_dbw(self):
        self.mainwid.goto_creturelist()