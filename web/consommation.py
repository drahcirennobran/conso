from string import Template
import MySQLdb
db = MySQLdb.connect("localhost","ric","coincoin","conso" )
cursor = db.cursor()
sql = "SELECT  idCompteur, captureDate, conso FROM conso"
try:
   cursor.execute(sql)

   results = cursor.fetchall()
   jsonString = []
   for row in results:
      idCompteur = row[0]
      captureDate = row[1]
      conso = row[2]
      jsonString.append("{\"id\":%s,\"date\":\"%s\",\"mwh\":%s},\n" % (idCompteur, captureDate, conso))
except:
   print "Error: unable to fecth data"

db.close();

def application(environ, start_response):

   tplFile = open('/var/www/webpy-app/code.py/conso.tpl')
   tplContent = tplFile.read()

   #template = Template("<html><body><h1>Hello ${name}</h1></body></html>")
   template = Template(tplContent)
   response_body = template.substitute(dict(data=''.join(jsonString)[:-2]))

   status = '200 OK'
   response_headers = [('Content-Type', 'text/html'),
                       ('Content-Length', str(len(response_body)))]

   start_response(status, response_headers)

   return [response_body]
