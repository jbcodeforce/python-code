# ' and " may be used to define a String. \ as escape char. Strings are immutable.
# If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the
# first quote

text = ('Put several strings within parentheses ' +
            'to have them joined together.')
print(text)

# string can be indexed
word = 'Python'
print(word[1])
# > y
print(word[-1])  # last char
# string comparaison
print('test' == 'test')
# string slicing
print(word[2:4])
# > th
# to remember how slices work is to think of the indices as pointing between characters,
# with the left edge of the first character numbered 0

# triming a string
text.strip()
# test a substring is in a string
print('substring' in 'string')
# > False
print('string' in 'biggerstring')
# >True
#integer value from a string
int("1")

#split: The method split() returns a list of all the words in the string, using str as the separator
fname='/Users/jeromeboyer/Code/jbcodeforce/python-sandbox/basics/playwithstring.py'
filePath=fname.split('/')
newfname=filePath[len(filePath)-1]
print(newfname)
