# The program will prompt for a URL, read the XML data from that URL using urllib 
# and then parse and extract the comment counts from the XML data, compute the sum
# of the numbers in the file. 
import xml.etree.ElementTree as ET
import urllib.request


url=input("Enter location:  <http://python-data.dr-chuck.net/comments_42.xml>")
url='http://python-data.dr-chuck.net/comments_42.xml'
print("Retrieving " + url)
xmlDoc = urllib.request.urlopen(url).read()
print("Retrieved ",len(xmlDoc), " characters")
commentInfo = ET.fromstring(xmlDoc)
count=0
sum=0
for comment in commentInfo.find('comments'):
	value=int(comment.find('count').text)
	sum+=value
	count+=1
print("Count: " + str(count))
print("Sum: " + str(sum))