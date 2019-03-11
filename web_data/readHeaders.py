import urllib.request
import json

url='http://www.agileitarchitecture.com'
connection=urllib.request.urlopen(url)
data=connection.read()
print(data)
print(connection.info())
