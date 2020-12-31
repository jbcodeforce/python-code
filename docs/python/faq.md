# Python FAQ

### Why pipenv

pipenv resolves the problem of dependencies management, that is not perfectly done in the requirements.txt, which leads to underterministic build process. Given the same input (the requirements.txt file), pip doesn’t always produce the same environment. `pip freeze` helps to freeze the dependencies and update your requirements.txt. But any dependency change needs to be done manually, and you need to track the dependent package version, for bug fix, or mandatory security fixes.

A second problem is the system wide repository used by pip. When developing multiple different projects in parallele that could become a real issue. `pipenv` use a per project environment.
pipenv acts as pip + virtual environment. It uses Pipfile to replace requirements.txt and pipfile.lock for determnistic build. See [this guide](https://realpython.com/pipenv-guide/) for command examples.

### How to get program arguments?

```python
  import sys,getopt
  USER="boyerje@us.ibm.com"
  FILE="./data/export-questions.json"
  try:
    opts, args = getopt.getopt(argv,"hi:u:",["inputfile=","user="])
  except getopt.GetoptError:
    print(usage())
    sys.exit(2)


  for opt, arg in opts:
    if opt == '-h':
      usage()
      sys.exit()
    elif opt in ("-u", "--user"):
      USER = arg
    elif opt in ("-i", "--inputfile"):
      FILE = arg
```

### How to get program dependencies generated?

```shell
pip freeze > requirements.txt
```

###  How to sort unit tests?

Use TestSuite and TestRunner. See TestPerceptron.py for usage.

```python
class TestPerceptron(unittest.TestCase):
  # ....
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestPerceptron('testLoadIrisData'))
    suite.addTest(TestPerceptron('testPlotIrisData'))

if __name__ == "__main__":
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())
```

### How to traverse a directory hierarchy?

```python
import osfor
root, dirs, files in os.walk("/mydir"):    
  for file in files:        
    if file.endswith(".txt"):             
      print(os.path.join(root, file))
```

### How to select a random item from a list?

```python
import random
move=random.choice(possibleMoves)
```

### Read json file

```python
g = open('critics.json','r')
d = json.load(g)
```

### Read csv file

```python
f = open('fn.csv','r')
for line in f:
  record = line.split(',')

# or with unicode:
  changedLine=u''.join(line).encode('utf-8').strip()
```

### Read file with specific encoding

```python
 with open('../data/movielens/u.item',  encoding='ISO-8859-1') as f:
```

### Skip the first row of a file

```python
f = open('fn.csv','r')
f.readline()
for line in f:
```

### How to get execution time

```python
import time
start = time.perf_counter()
# potentially slow computation
end = time.perf_counter() - start
```

### Example of memory consumption for object

```python
import sys

a = 3
b = 3.123
c = [a, b]
d = []
for obj in [a, b, c, d]:
  print(obj, sys.getsizeof(obj))
```

### What is zip?

Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterable:

```python
dataset
[[1, 20, 0], [2, 21, 1], [3, 22, 0]]
for a in zip(*dataset): print(a)
(1, 2, 3)
(20, 21, 22)
(0, 1, 0)
```

### How to use some math

```python
# modulo
8 % 2
0
#
```
### What is a package?

A package is nothing more than a folder, which must contain a special file, __init__.py. (not needed anymore with python3.3+)

### What are namespace and scope?

A namespace is a mapping from names to objects. They are the built-in names, the global names in a module, and the local names in a function.
A scope is a textual region of a Python program, where a namespace is directly accessible. There are four different scopes that Python makes accessible:

* The local scope, which is the innermost one and contains the local names.
* The enclosing scope, that is, the scope of any enclosing function. It contains non-local names and also non-global names.
* The global scope contains the global names.
* The built-in scope contains the built-in names.
