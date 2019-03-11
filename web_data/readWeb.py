import urllib.request
fhandler = urllib.request.urlopen('http://www.agileitarchitecture.com')
for line in fhandler:
	print(line.strip())
