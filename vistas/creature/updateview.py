import os
import sqlite3

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder

# Cargamos el Archivo KV, donde esta el formato de la wid
Builder.load_file(os.getcwd()+'/vistas/creature/updateview.kv')

class CreatureUpdateWid(BoxLayout):
    '''
    Esta Vista es para actualizr los datos de la Criatura
    '''
    def __init__(self, mainwid, data_id, *args, **kwargs):
        super(CreatureUpdateWid, self).__init__()
        self.mainwid = mainwid
        self.data_id = data_id
        self.check_memory()

    def check_memory(self):
        '''
        Esta funcion busta en la db, la creature, por el id
        '''
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        s =  'select nombre, carves, capture, cr from main.loot_criatura where id='
        cursor.execute(s+self.data_id)
        for i in cursor:
            self.ids.ti_nombre.text = i[0]
            self.ids.ti_carve.text = str(i[1])
            self.ids.ti_capture.text = str(i[2])
            self.ids.ti_cr.text = str(i[3])
        con.close()
    
    def update_creature(self):
        '''
        Funciuon encargada de conectars y actualizar la db
        '''
        d1 = self.ids.ti_nombre.text
        d2 = self.ids.ti_carve.text
        d3 = self.ids.ti_capture.text
        d4 = self.ids.ti_cr.text
        s1 = 'UPDATE "main"."loot_criatura" SET'
        s2 = 'nombre= "%s", carves=%s, capture=%s, cr=%s' %(d1, d2, d3, d4)
        s3 = 'WHERE id=%s' %(self.data_id)
        try:
            con = sqlite3.connect(self.mainwid.DB_PATH)
            cursor = con.cursor()
            cursor.execute(s1+' '+s2+' '+s3)
            con.commit()
            self.mainwid.goto_creturelist()
        except Exception as e:
            print(e)
            '''
            message = self.mainwid.Popup.ids.message
            self.mainwid.Popup.open()
            self.mainwid.Popup.title = 'DB Error'
            if '' in (d1, d2, d3, d4):
                message.text = 'Uno o mas campos estan vacios'
            else:
                message.text = str(e)
            '''
        con.close()

    def delete_creature(self):
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        s = 'delete from "main"."loot_criatura" where id='
        cursor.execute(s + self.data_id)
        con.commit()
        con.close()
        self.mainwid.goto_creturelist()

    def backto_creaturelist(self):
        self.mainwid.goto_creturelist()
