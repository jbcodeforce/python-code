import urllib
import json

url='http://python-data.dr-chuck.net/comments_42.json'
url='http://python-data.dr-chuck.net/comments_204840.json'
print('Retrieving ',url)
data = urllib.request.urlopen(url).read()
print ('Get ',len(data),' characters')
try:
	js=json.loads(str(data))
except:
	js = None

count=0
sum=0
for comment in js['comments']:
	value=int(comment['count'])
	sum+=value
	count+=1
print ("Count: ",count)
print ("Sum: ",sum)
