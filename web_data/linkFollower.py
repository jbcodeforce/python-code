# The program will use urllib to read the HTML from URLs, extract the href= values
# from the anchor tags, scan for a tag that is in a particular position relative to
# the first name in the list, follow that link and repeat the process a number of
# times and report the last name you find.

import urllib
from BeautifulSoup import *

#url='https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
url='https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Aedyn.html'
#
count=int(raw_input("Enter count:"))
position=int(raw_input("Enter position:") )

for c in range(0,count+1):
	print("Retrieving: {}".format(url))
	page = urllib.urlopen(url).read()
	soup=BeautifulSoup(page)
	tags=soup('a')
	url=tags[position-1].get('href',None)
