import urllib.request
import urllib.parse
import json

serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'

while True :
	address = input('Enter geo location: ')
	if len(address) < 1 : break
	
	url = serviceurl+urllib.parse.urlencode({'sensor':'false','address':address})
	print('Retrieving  {}', url)
	data = urllib.request.urlopen(url).read()
	print('Get % characters',str(len(data)))
	print(data)
	try:
		js=json.loads(str(data))
	except:
		js = None
	if 'status' not in js or js['status'] != 'OK' :
		print('==== failure ===== ')
		print(data)
		continue
	print(json.dumps(js,indent=4))
	lat=js["results"][0]["geometry"]["location"]["lat"]
	long=js["results"][0]["geometry"]["location"]["lng"]
	print(' {} {} ',lat,long)
	print(js["results"][0]["formatted_address"])
