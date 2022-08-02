# Python Summary
 
See this good [tutorial from Programiz](https://www.programiz.com/python-programming#tutorial)

Python is an interpreted Object Oriented & functional language. It organizes the code in modules.
Use blank to indent code block. The coding style is known as PEP8.

[3.9 release Product documentation](https://docs.python.org/3.9/library/index.html)

## Getting started

Start a python interpreter: `python3` and start entering python code, develop a progname.py file and use `python3 progname.py`, or add `#!/usr/bin/env python3` to make it self runnable.

The code can be structured with function `def name():`  and then with our without a main part:

```python
if __name__ == "__main__":
```

Better to use main statement when using objects and classes.

## Concepts

### Datatypes

* `list`:

    * concat lists: a = [1,2,3,4]    then a = a + [5,6]  or a + list("789") -> [1,2,3,4,5,6,'7','8','9']. Lists are mutable.
    * len(a)
    * slicing: all elements except first and last: `a[1:-1]`, all from index 3: `a[3:]` 
    * `list.append(a_record)` modifies a list by adding an item to the end
    * `list.pop()` removes and returns the last element of a list
    *  Get one object index using the `list.index(object)` 
    * `in list` to assess if element in the list
* list comprehensions:

    * `squares = [n**2 for n in range(10)]`
    * `short_planets = [planet for planet in planets if len(planet) < 6]`

* `dictionary` is like json object, with key-value list. The main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pair with del. If you store using a key that is already in use, the old value associated with that key is forgotten.

```python
cols={}
cols("column_name_1") = np.random.normal(2,1,10)
```

* A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it. `squares = [x**2 for x in range(10)]`
* Queues: do not use list for queue but collections.deque

```python
from collections import deque
    queue = deque([23,56,78,44])
    queue.append(55)
print(queue)

> deque([23, 56, 78, 44, 55])
twentythree=queue.popleft()
```

#### Tuples

tuples: a = (1,2,3,4,5) are iterable. Tuple does not support item assignment: t[3] = 5 --> error.

```python
tup1 = ('physics', 'chemistry', 1997, 2000);
print ("tup1[0]: ", tup1[0]);
# iteration
for a in tup1:
  print(a)
```

They are immutable. Need to create new tuples from existing one. Removing individual tuple elements is not possible.

Transform a tuple into array:
```python
a=(2, 2.6496666666666666, -30.463416666666667)
b=np.asarray(a)
# b array([  2.        ,   2.64966667, -30.46341667])
```

### String

```python
# get the last four chars
dirname[:len(dirname) - 4]
# split string to get the last folder name of a path
folders = path.split('/') 
name= folders[len(folders)-1]
name.lower()
name.upper()
name.index('substr')
claim.startswith(planet)
claim.endswith(planet)
```

See [string tutorial](https://www.tutorialspoint.com/python/python_strings.htm)

```python
def word_search(documents, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    # list to hold the indices of matching documents
    indices = [] 
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(documents):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices
```
### Control flow

`if condition: elsif condition: else`

* For statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence
* Range() to iterate over a sequence of numbers. (e.g. for i in range(5):). The given end point is never part of the generated sequence. It is possible to let the range start at another number, or to specify a different increment (from 0 to 10, increment 3:   range(0, 10, 3)). It returns an object which returns the successive items of the desired sequence when you iterate over it
* list(range(5)) build a list like: [0, 1, 2, 3, 4]
* Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement
* The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.

* See [Control Flow Statement Tutorial](https://www.scaler.com/topics/python/control-flow-statements-in-python/)

### Exception

```python
try:
  dosomething()
Except ValueError:
  pass
```

### Regular Expressions

[How to regex](https://docs.python.org/3.8/howto/regex.html)

Specialize in string pattern matching from string. It is a language by itself.

```python
import re
p = re.compile('ab*')
```

| Char | Note |
|:---:|:---|
| ^ | Matches the beginning of a line |
| $ | Matches the end of the line |
| . | Matches any character |
| \s | Matches whitespace |
| \S | Matches any non-whitespace character
| * | Repeats a character zero or more times
| *? | Repeats a character zero or more times (non-greedy)
| + | Repeats a character one or more times
| +? | Repeats a character one or more times (non-greedy)
| [aeiou] | Matches a single character in the listed set
| [^XYZ] | Matches a single character not in the listed set
| [a-z0-9] | The set of characters can include a range
| ( | Indicates where string extraction is to start
| ) | Indicates where string extraction is to end
| ‘@([^ ]*)' | extract the domain name from the email. Use () to specify what to extract, from the @. [^ ] math non-blank character
|  re.findall(‘[0-9]+’,s) | find all occurrence of number in string. [0-9] is one digit


### Functions

Python supports OOD and functional programming like Scala. Function can be defined in a scope of a module file outside of a class, or as method of a class.

* The keyword `def` introduces a function definition. It must be followed by the function name and the parenthesized list of formal parameters. The statements that form the body of the function start at the next line, and must be indented.
* The first statement of the function body can optionally be a string literal used as `docstring`.
* local variables cannot be directly assigned a value within a function (unless named in a global statement), although they may be referenced
* The return statement returns with a value from a function. return without an expression argument returns `None`.
* functions can have a variable number of arguments `def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):`
* Functions can also be called using keyword arguments of the form `kwarg=value` instead of using the positional arguments.  keyword arguments must follow positional arguments.
Arguments could have default value so becomes optional. Attention the default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls

```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
[1]
print(f(2))
[1,2]
print(f(3))
[1,2,3]
```

* A function can be called with an arbitrary number of arguments. The syntax is
`def (formalArg,formalArg2,*args,kwarg=value):`

* lambda is a keyword to define an anonymous function

```
def make_incrementor(n):
      return lambda x: x + n
f = make_incrementor(42)
f(2)
44
```
This can be used for specifying a sort method anonymously: use the second element of a tuple to sort a list of tuples

```
collection.sort(key=lambda collection : collection[1])
```

variable scope in function: when there is a need to access variable defined at the module level use the keyword global

### Namespaces

A namespace is a mapping from names to objects.
Examples of namespaces are:

* the set of built-in names (containing functions such as abs(), and built-in exception names), loaded when interpreter starts
* the global names in a module, created when module is loaded, and kept until interpreter quits
* the local names in a function invocation, created when the functions is called, deleted when function returns or raises an exception.
When searching of reference the interpreter starts by the innermost scope (current block) then enclosing functions, modules and built-in names
It is important to realize that scopes are determined textually: the global scope of a function defined in a module is that module’s namespace, no matter from where or by what alias the function is called.
If no global statement is in effect – assignments to names always go into the innermost scope.
Assignments do not copy data — they just bind names to objects.

```python
# reference a non local variable in a function
     nonlocal spam
# or a global
    global spam
```

### Object

Python is a OOP, with polymorphism and inheritance.

A class construction is a method declare as `def __init__(self):`
A destructor is `def __del__(self):`.
A toString is `def _str__():`

Class definitions, like function definitions (def statements) must be executed before they have any effect. When a class definition is entered, a new namespace is created, and used as the local scope — thus, all assignments to local variables go into this new 'class' namespace.

```python
class Complex:
    """ Represents mathematical Complex number
    """
    # called once instance is created to initialize internal attributes (like java constructor)
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


# creating an instance
x=Complex(3,2)
# attribute reference ; class.attname
x.i
```

The only operations understood by instance objects are attribute references. There are two kinds of valid attribute names, data attributes and methods.

```python
class MyClass(object):
    '''
    classdocs
    '''

    def __init__(self, p:str):
        '''
        Constructor
        '''
        self.a=p
        self.n=1
    def f(self):
        return self.n+1

c=MyClass('an object')
# can add attribute dynamically into object even if class did not define it...
c.b="a new attribute"
print(c.a)
# an object
print(c.b)
# a new attribute
print(c.f())
# 2
```

Clients should use data attributes with care — clients may mess up invariants maintained by the methods by stamping on their data attributes.
Python supports inheritance and search for attributes is done using a depth-first, left to right approach.

```
class DerivedClassName(Base1, Base2, Base3):
```

There is no private instance variables inside an object. The naming convention using _ before the name should be treated as non-public part of the API.

### Module 

A **module** is a file containing python definitions and statements. The filename = module name. 
Definitions from a module can be imported into other modules or into the main module. 
Be sure to take the folder hierarchy as package hierarchy.
A module can contain executable statements as well as function definitions. These statements are 
intended to initialize the module. They are executed only the first time the module name is 
encountered in an import statement.

```python
# To see the variables and function of a module
import math
print(dir(math))
# give combined documentation for all the functions and values in the module 
help(math)
```
Always import only the specific things we'll need from each module.

To make a module executable we need a main statement

```
if __name__ == "__main__":
```

The directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path: scripts in that directory will be loaded instead of modules of the same name in the library directory. The interpreter first searches for a built-in module then it searches for a file named spam.py in a list of directories given by the variable sys.path (current directory + PYTHONPATH).
To speed up loading modules, Python caches the compiled version of each module in the __pycache__ directory under the name module.version.pyc, where the version encodes the format of the compiled file; it generally contains the Python version number.

### File I/O

You open a file in different mode with the open . Files are text or binary
```python
# first create a text file
f = open('atext .txt','w' )
f.write('A first line\n')
f.write('A second line\n')
f.close()

f = open('atext.txt', 'r')
f.readline()
# 'A first line\n'
f.readline()
# 'A second line\n'
f.readline()
# no more line is '' empty string

# read all lines and build a list: 2 ways
lines=f.readlines()
list(f)
# read line by line: very efficient as use limited memory. f is an iterator over the lines
for line in f

# a dictionary persisted as json in text file
import json
f = open('critics.txt', 'w')
json.dump(critics,f)
f.close()
# reload it
g = open( 'critics.txt','r' )
d=json.load(g)
print(d[' Toby'])
```

Python doesn't flush the buffer—that is, write data to the file—until it's sure you're done writing. One way to do this is to close the file.
File objects contain a special pair of built-in methods: `__enter__()` and `__exit__()`.

See code `python-bible/readAssetFromFolder.py` which uses [Git client](https://gitpython.readthedocs.io/en/stable/tutorial.html#examining-references) to get origin URL.

## Date

See the [datetime module](https://docs.python.org/3/library/datetime.html)

```python
import datetime

print ('Current date/time: {}'.format(datetime.datetime.now()))

 d= datetime.date(2018,9,23)
 d= datetime.date.today()
 datetime.datetime.today()

datetime.datetime(2019, 9, 23, 18, 34, 26, 856722)


date_time_str = 'Jun 28 2018  7:40AM'
date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')

# transform to a string
d.strftime("%Y-%m-%d %H:%M:%S")
```


## Unit testing

[unittest](https://docs.python.org/3/library/unittest.html) is based on Kent Beck's work on unit testing like the `junit` library.

* define a module with a class which extends TestCase, use the setUp and tearDown methods to set context before each test method.

* Add test method and use assert* to validate test results.

Consider [pytest](https://docs.pytest.org/en/latest/) as another modern tool to do testing in python. 

## Reading command line arguments

```python
import sys
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))
```

## Doing HTTP requests

See code under [web_data](https://github.com/jbcodeforce/python-code/web_data), but with python 3 the approach is to use [request](https://requests.readthedocs.io/en/master/).

* [urllib](https://docs.python.org/3/library/urllib.html)
* [The request library](http://docs.python-requests.org/en/master/user/quickstart/#response-content)

## Python Flask WebApp

The project [python-code](https://github.com/jbcodeforce/python-code) includes the `angular-flask` folder to present some simple examples of how to use Flask with Angular. 

See [this note for details.](../flask/readme.md)

## Data management

### Pandas

Create a data frame with two columns

```
data = DataFrame({'message': [], 'class': []})
```

Create n records with timestamp from one start time:

```
start_time = datetime.datetime.today() 
c=pd.date_range(start_time, periods=nb_records, freq=METRIC_FREQUENCY)
```

Transforming to string
```
c.strftime("%Y-%m-%d %H:%M:%S")
```

### Split data into training and test sets

```
splitIndex = np.random.rand(len(data)) < 0.8
train = data[splitIndex]
test = data [~splitIndex]
```
