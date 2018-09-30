import urllib
import json

serviceurl='http://python-data.dr-chuck.net/geojson?'

while True :
	address = raw_input('Enter location: ')
	if len(address) < 1 : break
	
	url = serviceurl+urllib.urlencode({'sensor':'false','address':address})
	print 'Retrieving ',url
	data = urllib.urlopen(url).read()
	print 'Get ',len(data),' characters'
	
	try:
		js=json.loads(str(data))
	except:
		js = None
	if 'status' not in js or js['status'] != 'OK' :
		print '==== failure ===== '
		print data
		continue


	placeid=js["results"][0]["place_id"]
	print placeid
	print js["results"][0]["formatted_address"]
