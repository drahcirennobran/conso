from cgi import parse_qs, escape
import MySQLdb
import logging

quart = "SELECT  idCompteur, captureDate, conso FROM conso where captureDate > DATE_SUB(now(), INTERVAL 1 MONTH) AND idCompteur=%s order by captureDate"
day = "SELECT  idCompteur, captureDate, conso FROM consoByDay where captureDate > DATE_SUB(now(), INTERVAL 3 MONTH) AND idCompteur=%s order by captureDate"
month = "SELECT  idCompteur, month, conso FROM consoByMonth where idCompteur=%s"

def application(environ, start_response):
   try:
      logging.basicConfig(filename='/tmp/consoweb.log', level=logging.INFO)
      logging.info("coincoin")
   except:
      status = '500 KO'
      response_body="prout"
      response_headers = [('Content-Type', 'application/json'),('Content-Length', str(len(response_body)))]
      start_response(status, response_headers)
      return [response_body]

   logging.info("requete quete")
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
   else:
      sql=month

   if 'id' in parameters:
      param = escape(parameters['id'][0])
      if param=='1':
         equipement=1
      elif param=='2':
         equipement=2
      else:
         equipement=1
   else:
      equipement=1
   print 'XXX-'
   print sql
   print equipement
   try:
      cursor.execute(sql, equipement)
      results = cursor.fetchall()
      jsonString = []
      for row in results:
         idCompteur = row[0]
         captureDate = row[1]
         conso = row[2]
         jsonString.append("{\"id\":%s,\"date\":\"%s\",\"mwh\":%s},\n" % (idCompteur, captureDate, conso))
      response_body = '[' + ''.join(jsonString)[:-2] + ']'
   except Exception as myex:
      response_body = str(myex)

   db.close();

   status = '200 OK'
   response_headers = [('Content-Type', 'application/json'),
                       ('Content-Length', str(len(response_body)))]

   start_response(status, response_headers)

   return [response_body]
