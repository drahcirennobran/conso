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

   response_body = '[' + ''.join(jsonString)[:-2] + ']'

   status = '200 OK'
   response_headers = [('Content-Type', 'application/json'),
                       ('Content-Length', str(len(response_body)))]

   start_response(status, response_headers)

   return [response_body]
