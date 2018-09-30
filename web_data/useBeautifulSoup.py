import urllib
from BeautifulSoup import *
import re

#page = urllib.urlopen('http://python-data.dr-chuck.net/comments_42.html').read()
page = urllib.urlopen('http://python-data.dr-chuck.net/comments_204839.html ').read()
# retrieve all the td
soup=BeautifulSoup(page)
tags=soup('span')
sum=0
count=0
for tag in tags:
	s=re.findall('([0-9]+)',tag.contents[0])
	sum+=int(s[0])
	count+=1
print('Count ',count)
print('Sum ',sum)
