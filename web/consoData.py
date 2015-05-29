from cgi import parse_qs, escape
import MySQLdb

quart = "SELECT  idCompteur, captureDate, conso FROM conso where captureDate > DATE_SUB(now(), INTERVAL 1 MONTH) AND idCompteur=1 order by captureDate"
day = "SELECT  idCompteur, captureDate, conso FROM consoByDay where captureDate > DATE_SUB(now(), INTERVAL 3 MONTH) AND idCompteur=1 order by captureDate"
month = "SELECT  idCompteur, month, conso FROM consoByMonth where idCompteur=1"

def application(environ, start_response):

   db = MySQLdb.connect("localhost","ric","coincoin","conso" )
   cursor = db.cursor()
   parameters = parse_qs(environ.get('QUERY_STRING', ''))
   if 'by' in parameters:
      param = escape(parameters['by'][0])
      if param=='quart':
         sql=quart
      elif param=='day':
         sql=day
      elif param=='month':
         sql=month
      else:
         sql=month

   try:
      cursor.execute(sql)
      results = cursor.fetchall()
      jsonString = []
      for row in results:
         idCompteur = row[0]
         captureDate = row[1]
         conso = row[2]
         jsonString.append("{\"id\":%s,\"date\":\"%s\",\"mwh\":%s},\n" % (idCompteur, captureDate, conso))
      response_body = '[' + ''.join(jsonString)[:-2] + ']'
   except:
      response_body = '[]'

   db.close();

   status = '200 OK'
   response_headers = [('Content-Type', 'application/json'),
                       ('Content-Length', str(len(response_body)))]

   start_response(status, response_headers)

   return [response_body]
