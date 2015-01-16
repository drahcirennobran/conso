#!/usr/bin/python

import MySQLdb
import urllib

db = MySQLdb.connect("localhost","ric","coincoin","conso" )
cursor = db.cursor()

link = "http://192.168.0.102:31415/mwh"
f = urllib.urlopen(link)
conso = f.read()

sql = "insert into conso (idCompteur , conso) VALUES (1, " + conso + ");"
try:
    cursor.execute(sql)
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
