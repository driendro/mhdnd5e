import sqlite3  # importamos sqllite3 para conectar con la db
from os import remove  # importasmos el remove de os para borrar archivos

# Este archivo regenera la db
# Borra la actual
remove("database.db")

# Crea una nueva, y crea las tablas vacias
# creamos la coneccion
con = sqlite3.connect('./database.db')
# Creamos el cursor para realizar secuancias sql
cursorObj = con.cursor()
#cursorObj.execute("CREATE DATABASE main")
#print('DB main ----> OK')
cursorObj.execute('CREATE TABLE "main"."loot_criatura" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(50) NOT NULL, "carves" integer NOT NULL, "capture" integer NOT NULL, "cr" integer NOT NULL)')
print('Tabla Creature ---> OK')
cursorObj.execute('CREATE TABLE "main"."loot_item" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(50) NOT NULL, "descripcion" text NOT NULL, "arma" bool NOT NULL, "armadura" bool NOT NULL, "otro" bool NOT NULL)')
print('Tabla item ---> OK')
cursorObj.execute('CREATE TABLE "main"."loot_loot" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "val_min" integer NOT NULL, "val_max" integer NOT NULL, "criatura_id" integer NOT NULL REFERENCES "loot_criatura" ("id") DEFERRABLE INITIALLY DEFERRED, "item_id" integer NOT NULL REFERENCES "loot_item" ("id") DEFERRABLE INITIALLY DEFERRED)')
print('Tabla loot ---> OK')
con.commit()
con.close()
