# Read folder content
import os

# Defining function

# List a folder content
start_path = '.' # current directory
for path,dirs,files in os.walk(start_path):
    for filename in files:
        print(os.path.join(path,filename))


# first create a text file
f = open('atext.txt','w' )
f.write('A first line\n')
f.write('A second line\n')
f.close()

f = open('atext.txt', 'r')
print(f.readline())
# 'A first line\n'
print(f.readline())
# 'A second line\n'
print(f.readline())
# no more line is '' empty string

# read all lines and build a list: 2 ways
lines=f.readlines()

# read line by line: very efficient as use limited memory. f is an iterator over the lines
for line in list(f):
    print(line)

# a dictionary persisted as json in text file
import json
critics = {}  # a dictionary
f = open('critics.txt', 'w')
json.dump(critics,f)
f.close()
# reload it
g = open( 'critics.txt','r' )
d = json.load(g )
print(d[' Toby'])

