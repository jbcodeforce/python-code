import urllib
fhandler = urllib.urlopen('http://www.agileitarchitecture.com')
for line in fhandler:
	print(line.strip())
