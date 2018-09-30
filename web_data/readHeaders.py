import urllib
import json

url='http://www.pythonlearn.com/code/intro-short.txt'
connection=urllib.urlopen(url)
data=connection.read()
print data
print connection.info()
