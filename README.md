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

## Code in the order of review
### Basics
* [firstinput.py](python-bible/firstinput.py) for reading user input
* [travis.py](python-bible/travis.py) to play with lists, for in range and condition
* [cinema.py](python-bible/cinema.py) for dictionary
* [Play with data structures](python-bible/datastructure.py)

### Graphics
* [use a simple graphics](graphics/)

## Python shell tricks
* placing cursor to previous line and enter will copy the line to a new line

## Python quick summary

* to get a type of a variable: type(a) as python is a dynamic type
* convert float to int using casting `a = int(66/45)`
* Ap math.pi is not a complete pi, to get real zero for sinus(pi) use floor function: `math.floor(math.sin(math.pi))`
* Extends a string assignment on multiple lines: use """ a long string on multiple lines """
* To assess input, string work see program [python-bible/firstinput.py](python-bible/firstinput.py)
* concat lists: a = [1,2,3,4]    then a = a + [5,6]  or a + list("789") -> [1,2,3,4,5,6,'7','8','9']. Lists are mutable.
* tuples: a = (1,2,3,4,5). Are iterable. Tuple does not support item assignment: t[3] = 5 -->error.
* dictionary is like json object a key- value list.

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
