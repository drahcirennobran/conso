#!/usr/bin/python

import MySQLdb
import urllib
import sys

db = MySQLdb.connect("localhost","ric","coincoin","conso" )
cursor = db.cursor()

link1 = "http://192.168.0.102:31415/cumulusmwh"
link2 = "http://192.168.0.102:31415/chauffagemwh"

f1 = urllib.urlopen(link1)
conso1 = f1.read()
sys.stdout.write(link1 + "   : " + conso1)

f2 = urllib.urlopen(link2)
conso2 = f2.read()
sys.stdout.write(link2 + " : " + conso2)

sql1 = "insert into conso (idCompteur , conso) VALUES (1, " + conso1 + ");"
sql2 = "insert into conso (idCompteur , conso) VALUES (2, " + conso2 + ");"

try:
    cursor.execute(sql1)
    db.commit()
except:
    db.rollback()

try:
    cursor.execute(sql2)
    db.commit()
except:
    db.rollback()

db.close()
