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

        wid = NewCreatureButton(self.mainwid)
        self.ids.conteiner.add_widget(wid)


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