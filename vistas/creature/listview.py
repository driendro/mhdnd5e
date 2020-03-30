import os
import sqlite3

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder

# Cargamos el Archivo KV, donde esta el formato de la wid
Builder.load_file(os.getcwd()+'/vistas/creature/listview.kv')

class CreatureListWid(BoxLayout):
    '''
    En esta vista, se enlistaran las criaturas en un ScrollView, agregando al
    fianl un button para agregar elementos a la DB.
    '''
    def __init__(self, mainwid, *args, **kwargs):
        super(CreatureListWid, self).__init__()
        self.mainwid = mainwid

    def check_memory(self):
        '''
        Esta funcion, limpiara lois widgets que esten en al memoria, para luego
        regenerarlos desde la db
        '''
        self.ids.conteiner.clear_widgets()
        # Obtenemos los datos de la db
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        cursor.execute('select id, nombre, carves, capture, cr from main.loot_criatura')
        # Recorremos los datos, y los mostramos en el DetaileWid()
        for i in cursor:
            wid = DetaileWid(self.mainwid)
            r1 = i[1]+'(CR: '+str(i[4])+')'+'\n'
            r2 = 'Capture: '+str(i[3])+'        '+'Carves: '+str(i[2])
            wid.data_id = str(i[0])
            wid.data = r1+r2
            self.ids.conteiner.add_widget(wid)

        wid = NewCreatureButton(self.mainwid)
        self.ids.conteiner.add_widget(wid)
        con.close()


class NewCreatureButton(Button):
    '''
    En este Button, estara siempre al final de CreatureListWid, y apuntra a 
    CreatureCreateWid
    '''
    def __init__(self, mainwid, *args, **kwargs):
        super(NewCreatureButton, self).__init__()
        self.mainwid = mainwid
    
    def creature_new(self):
        print('cabezadegoma')
        self.mainwid.goto_creaturecreate()

class DetaileWid(BoxLayout):
    '''
    Widget donde se muestra los detalles de la creatura, y el boton de edit
    '''
    def __init__(self, mainwid, *args, **kwargs):
        super(DetaileWid, self).__init__()
        self.mainwid = mainwid

    def creature_update(self, data_id):
        self.mainwid.goto_creatureupdate(data_id)