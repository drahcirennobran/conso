#!/usr/bin/python

import MySQLdb
import urllib

db = MySQLdb.connect("localhost","ric","coincoin","conso" )
cursor = db.cursor()

link1 = "http://192.168.0.102:31415/cumulusmwh"
link2 = "http://192.168.0.102:31415/chauffagemwh"

f1 = urllib.urlopen(link1)
f2 = urllib.urlopen(link1)

conso1 = f1.read()
conso2 = f2.read()


sql1 = "insert into conso (idCompteur , conso) VALUES (1, " + conso1 + ");"
sql2 = "insert into conso (idCompteur , conso) VALUES (2, " + conso2 + ");"

try:
    cursor.execute(sql1)
    cursor.execute(sql2)
    db.commit()
except:
    db.rollback()

#data = cursor.fetchone()
#println " %s " % data

db.close()



#sql = "SELECT * FROM EMPLOYEE \
#       WHERE INCOME > '%d'" % (1000)
#try:
#   # Execute the SQL command
#   cursor.execute(sql)
#   # Fetch all the rows in a list of lists.
#   results = cursor.fetchall()
#   for row in results:
#      fname = row[0]
#      lname = row[1]
#      age = row[2]
#      sex = row[3]
#      income = row[4]
#      # Now print fetched result
#      print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
#             (fname, lname, age, sex, income )
#except:
#   print "Error: unable to fecth data"
