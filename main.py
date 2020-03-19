#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, font
import sqlite3


class Aplicacion():
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("App de loot")
        self.raiz.resizable(0, 0)
        fuente = font.Font(weight='bold')

        #################Creature Section#################################
        self.marcoCreature = ttk.Frame(self.raiz, borderwidth=2,
                                       relief="raised", padding=(10, 10))
        self.etiqCreature = ttk.Label(
            self.marcoCreature, text="Criatura", font=fuente, padding=(5, 5))

        self.btnCreateCreature = ttk.Button(self.marcoCreature, text='Crear',
                                            command=self.Crate_Creature)
        self.btnUpdateCreature = ttk.Button(self.marcoCreature, text='Modificar',
                                            command=self.Update_Creature)
        self.btnDeleteCreature = ttk.Button(self.marcoCreature, text='Borrar',
                                            command=self.Delete_Creature)
        self.btnSearchCreature = ttk.Button(self.marcoCreature, text='Buscar',
                                            command=self.Search_Creature)

        self.marcoCreature.grid(column=0, row=0)
        self.etiqCreature.grid(column=0, row=0)
        self.btnCreateCreature.grid(column=0, row=1)
        self.btnUpdateCreature.grid(column=0, row=2)
        self.btnDeleteCreature.grid(column=0, row=3)
        self.btnSearchCreature.grid(column=0, row=4)

        #################Personaje Section#################################

        self.marcoPJ = ttk.Frame(self.raiz, borderwidth=2,
                                 relief="raised", padding=(10, 10))

        self.etiqPJ = ttk.Label(
            self.marcoPJ, text="Personajes", font=fuente, padding=(5, 5))

        self.btnCreatePJ = ttk.Button(self.marcoPJ, text='Crear',
                                      command=self.Crate_Creature)
        self.btnUpdatePJ = ttk.Button(self.marcoPJ, text='Modificar',
                                      command=self.Update_Creature)
        self.btnDeletePJ = ttk.Button(self.marcoPJ, text='Borrar',
                                      command=self.Delete_Creature)
        self.btnSearchPJ = ttk.Button(self.marcoPJ, text='Buscar',
                                      command=self.Search_Creature)

        self.marcoPJ.grid(column=1, row=0)
        self.etiqPJ.grid(column=0, row=0)
        self.btnCreatePJ.grid(column=0, row=1)
        self.btnUpdatePJ.grid(column=0, row=2)
        self.btnDeletePJ.grid(column=0, row=3)
        self.btnSearchPJ.grid(column=0, row=4)
        self.raiz.mainloop()

    def Crate_Creature(self):

        self.crateCreature = tk.Toplevel()
        self.crateCreature.resizable(0, 0)
        self.crateCreature.title('Crear Criatura Nueva')
        fuente = font.Font(weight='bold')

        self.marco = ttk.Frame(
            self.crateCreature, borderwidth=2, relief="raised", padding=(10, 10))

        self.etiq1 = ttk.Label(
            self.marco, text="Nombre de la Criatura:", font=fuente, padding=(5, 5))
        self.etiq2 = ttk.Label(
            self.marco, text="CR de la Criatura:", font=fuente, padding=(5, 5))
        self.etiq3 = ttk.Label(
            self.marco, text="Carve (cantidad):", font=fuente, padding=(5, 5))
        self.etiq4 = ttk.Label(
            self.marco, text="Capture (Cantidad):", font=fuente, padding=(5, 5))

        self.nombre = tk.StringVar()
        self.cr = tk.DoubleVar()
        self.carve = tk.IntVar()
        self.capture = tk.IntVar()

        self.ctext1 = ttk.Entry(
            self.marco, textvariable=self.nombre, width=30)
        self.ctext2 = ttk.Entry(
            self.marco, textvariable=self.cr, width=30)
        self.ctext3 = ttk.Entry(
            self.marco, textvariable=self.carve, width=30)
        self.ctext4 = ttk.Entry(
            self.marco, textvariable=self.capture, width=30)

        self.separ1 = ttk.Separator(self.marco, orient=tk.HORIZONTAL)
        self.boton1 = ttk.Button(
            self.marco, text="Aceptar", padding=(5, 5), command=self.createCreature_Aceptar)
        self.boton2 = ttk.Button(self.marco, text="Cancelar", padding=(
            5, 5), command=self.crateCreature.destroy)

        self.marco.grid(column=0, row=0)
        self.etiq1.grid(column=0, row=0)
        self.ctext1.grid(column=1, row=0, columnspan=2)
        self.etiq2.grid(column=0, row=1)
        self.ctext2.grid(column=1, row=1, columnspan=2)
        self.etiq3.grid(column=0, row=2)
        self.ctext3.grid(column=1, row=2, columnspan=2)
        self.etiq4.grid(column=0, row=3)
        self.ctext4.grid(column=1, row=3, columnspan=2)

        self.separ1.grid(column=0, row=5, columnspan=3)
        self.boton1.grid(column=1, row=6)
        self.boton2.grid(column=2, row=6)

        self.raiz.wait_window(self.crateCreature)

    def Update_Creature(self):
        self.updateCreature = tk.Toplevel()
        self.updateCreature.resizable(0, 0)
        self.updateCreature.title('Modificar Criatura')
        fuente = font.Font(weight='bold')

        self.marco = ttk.Frame(
            self.crateCreature, borderwidth=2, relief="raised", padding=(10, 10))

        self.etiqName = ttk.Label(
            self.marco, text="Nombre de la Criatura:", font=fuente, padding=(5, 5))
        self.etiqCR = ttk.Label(
            self.marco, text="CR de la Criatura:", font=fuente, padding=(5, 5))
        self.etiqCarve = ttk.Label(
            self.marco, text="Carve (cantidad):", font=fuente, padding=(5, 5))
        self.etiqCapture = ttk.Label(
            self.marco, text="Capture (Cantidad):", font=fuente, padding=(5, 5))

        print('Update')

    def Delete_Creature(self):
        print('Borrar')

    def Search_Creature(self):
        print('Buscar')

    def createCreature_Aceptar(self):
        nombre = self.nombre.get()
        cr = self.cr.get()
        carve = self.carve.get()
        capture = self.capture.get()
        con = sqlite3.connect('./database.db')
        cursorObj = con.cursor()
        cursorObj.execute(
            'INSERT INTO "main"."loot_criatura"(nombre, carves, capture, cr) VALUES(?, ?, ?, ?)', (nombre, carve, capture, cr))
        print('Creature Creada y Guardad en la db')
        con.commit()
        con.close()


def main():
    mi_app = Aplicacion()
    if mi_app:
        return 0


if __name__ == '__main__':
    main()
