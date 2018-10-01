# Python Code
A bench of python code from training and studies and raspberry work.

## Execution
It is of vital importance that you never install libraries directly at the system level. Linux for example relies on Python for many different tasks and operations, and if you modify the system installation of Python, you risk compromising the integrity of the whole system.
install virtualenv with `pip install virtualenv`virtualenv -p /Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 .venv

### User local python
### Use docker with mlpython image
start XQuartz
open a socket connection
docker run -e DISPLAY=192.168.1.89:0 --name pysparktf -v $(pwd):/home/jovyan/work -it --rm -p 8888:8888 jbcodeforce/mlpython /bin/bash


#### create virtual environment under your project folder
`virtualenv -p /Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 .venv`
#### Activate environment
```
source .venv/bin/activate

python3 programname.py

deactivate
```
## Python quick summary
Python is an interpreted OO & functional language. It organizes the code in module.
Use blank to indent code block. The coding style is known as PEP8.

* to get a type of a variable: type(a) as python is a dynamic type
* convert float to int using casting `a = int(66/45)`
* String: ' and " may be used to define a String. \ as escape char. Strings are immutable.
If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote
* Ap math.pi is not a complete pi, to get real zero for sinus(pi) use floor function: `math.floor(math.sin(math.pi))`
* Extends a string assignment on multiple lines: use """ a long string on multiple lines """
* To assess input, string work see program [python-bible/firstinput.py](python-bible/firstinput.py)
* concat lists: a = [1,2,3,4]    then a = a + [5,6]  or a + list("789") -> [1,2,3,4,5,6,'7','8','9']. Lists are mutable.
* tuples: a = (1,2,3,4,5). Are iterable. Tuple does not support item assignment: t[3] = 5 -->error.
* dictionary is like json object a key- value list. The main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pair with del. If you store using a key that is already in use, the old value associated with that key is forgotten.
* A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it. `squares = [x**2 for x in range(10)]`
* Queues: do not use list for queue but collections.deque

 ```python
from collections import deque
queue = deque([23,56,78,44])
queue.append(55)
print(queue)
>>deque([23, 56, 78, 44, 55])
twentythree=queue.popleft()
 ```

* Control flow: `if condition: elsif condition: else`
  * for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence
  * Range() to iterate over a sequence of numbers. (e.g. for i in range(5):). The given end point is never part of the generated sequence. It is possible to let the range start at another number, or to specify a different increment (from 0 to 10, increment 3:   range(0, 10, 3)). It returns an object which returns the successive items of the desired sequence when you iterate over it
  * list(range(5)) build a list like: [0, 1, 2, 3, 4]
  * Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement
* The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.

* Regular Expressions:
Specialize in string pattern matching from string. It is a language by itself.

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


### Function
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
* a function can be called with an arbitrary number of arguments. The syntax is
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

`collection.sort(key=lambda collection : collection[1])`

variable scope in function: when there is a need to access variable defined at the module level use the keyword global

### Object
Python is a OOP, with polymorphism and inheritance.

A class construction is a method declare as `def __init__(self):`
A destructor is `def __del__(self):`.
A toString is `def _str__():`

## Code in the order of review
### Basics
* [firstinput.py](python-bible/firstinput.py) for reading user input
* [travis.py](python-bible/travis.py) to play with lists, for in range and condition
* [cinema.py](python-bible/cinema.py) for dictionary
* [Play with data structures](python-bible/datastructure.py)
* [Reverse a word and add aye](python-bible/pig.py), use loops, break, in voyals...

### Graphics
* [use a simple graphics](graphics/testgraphics.py) to create a window, draw circle and move them.

### Web scrawling
Use urllib and beautiful soup to remove html tags from a web page to get text to parse.
* [Use regular expression (re module)](web_data/countNumbers.py) to extract number from a text read from a file.

## Python shell tricks
* placing cursor to previous line and enter will copy the line to a new line



## Idle summary
F1 to get access to all python doc.

## FAQ
### What is a package?
A package is nothing more than a folder, which must contain a special file, __init__.py. (not needed anymore with python3.3+)

### What are namespace and scope?
A namespace is a mapping from names to objects. They are the built-in names, the global names in a module, and the local names in a function.
A scope is a textual region of a Python program, where a namespace is directly accessible. There are four different scopes that Python makes accessible:
* The local scope, which is the innermost one and contains the local names.
* The enclosing scope, that is, the scope of any enclosing function. It contains non-local names and also non-global names.
* The global scope contains the global names.
* The built-in scope contains the built-in names.

### To share code with people
You can use gist.gtihub.com


## References
* http://docs.python.org/3/tutorial/index.html
* http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/
* http://www.secnetix.de/olli/Python/
* http://www.brunningonline.net/simon/python/quick-ref2_0.html#LexEnt
