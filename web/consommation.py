from string import Template

def application(environ, start_response):

   tplFile = open('/var/www/webpy-app/code.py/conso.tpl')
   tplContent = tplFile.read()

   #template = Template("<html><body><h1>Hello ${name}</h1></body></html>")
   template = Template(tplContent)
   response_body = template.substitute(dict(name='Ric'))

   status = '200 OK'
   response_headers = [('Content-Type', 'text/html'),
                       ('Content-Length', str(len(response_body)))]

   start_response(status, response_headers)

   return [response_body]
