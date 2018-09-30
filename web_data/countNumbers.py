import re;

hand = open('regex_sum_204834.txt');
sum=0
numberOfElement=0
for line in hand:
	line = line.rstrip()
	numbers= re.findall('([0-9]+)',line)
	for x in numbers:
		sum+=int(x)
		numberOfElement+=1
		print(x)
print ("There are %d values with a sum=%d" % (numberOfElement, sum))
