import urllib
link = "http://localhost:1234"
f = urllib.urlopen(link)
response = f.read()

