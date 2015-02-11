import urllib

def application(environ, start_response):

   link = "http://192.168.0.102:31415/cumulus_i"
   f = urllib.urlopen(link)
   conso = f.read()

   response_body = conso;

   status = '200 OK'
   response_headers = [('Content-Type', 'application/json'),
                       ('Content-Length', str(len(response_body)))]

   start_response(status, response_headers)

   return [response_body]
