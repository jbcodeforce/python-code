'''
Created on Apr 6, 2014

@author: boyerje
'''

''' Lists 
'''
l=[4,6,8,10,12,20]
l.insert(1,5)
print(l)
l.remove(5)
l.append(30)
print(l)
l.reverse()
# lists are also used as stack
last=l.pop()
print(last)   # should be 4 as the list was reversed


from collections import deque
queue = deque([23,56,78,44])
queue.append(55)
print(queue)
twentythree=queue.popleft()

# a collection of n ** 2
squares=[n**2 for n in range(10)]
print(squares)

matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
# transpose rows and columns
m2=[[row[i] for row in matrix] for i in range(4)]
print(m2)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


# sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
d=set('abracadabra')
print(d)
b = set('alacazam')
print(b)
e=d-b
print(e)  # exclusion: letters in d but not in b
u=d|b
print(u)  # union
i=d&b
print (i) # intersection
x=d^b
print (x) # letters in a or b but not both

# dictionaries
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
l=list(tel.keys())
print(l)
cards=dict(chapel=2,witch=4,trone=4)
print(cards)
# looping among data structure
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items() : print(k,v)
for i, v in enumerate(['tic', 'tac', 'toe']): print(i,v)
for i in reversed(range(1, 10, 2)): print(i)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


 

