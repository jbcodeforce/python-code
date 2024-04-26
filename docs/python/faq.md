# Python FAQ

## Why pipenv

pipenv resolves the problem of dependencies management, that is not perfectly done in the requirements.txt, which leads to underterministic build process. Given the same input (the requirements.txt file), pip doesn’t always produce the same environment. `pip freeze` helps to freeze the dependencies and update your requirements.txt. But any dependency change needs to be done manually, and you need to track the dependent package version, for bug fix, or mandatory security fixes.

A second problem is the system wide repository used by pip. When developing multiple different projects in parallele that could become a real issue. `pipenv` use a per project environment.
pipenv acts as pip + virtual environment. It uses Pipfile to replace requirements.txt and pipfile.lock for determnistic build. See [this guide](https://realpython.com/pipenv-guide/) for command examples.

## How to get program arguments?

```python
  import sys,getopt
  USER="jbcodeforce"
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

### Using [arg_parser](https://docs.python.org/3/howto/argparse.html)

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Must specify a file name")
parser.add_argument("--append", help="Append records to existing file",action="store_true")
args = parser.parse_args()
if args.append:
    print("append to file")
    
```

## what `__init__.py` under folder used for?

The `__init__.py` file makes Python treat directories containing it as modules. Furthermore, this is the first file to be loaded in a module, so you can use it to execute code that you want to run each time a module is loaded, or specify the submodules to be exported.

## How to get program dependencies generated?

```shell
pip freeze > requirements.txt
```

## Access environment variable

Define environment variables in a `.env` file, use os package:

```python
import os

AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
```

## List content of folder

```python
import glob

def listOfYaml():
    return glob.glob("./*.yaml")
```

## Change content of yaml

```python
import glob
import yaml

def listOfYaml():
    return glob.glob("./*.yaml")

def processYamlFile(f):
    with open(f) as aYaml:
        listDoc = yaml.safe_load(aYaml)
    print(listDoc)
    listDoc["metadata"]["namespace"]='std-2'
    print(listDoc)
    

f = listOfYaml()
processYamlFile(f[0])

```

## How to sort unit tests?


Use TestSuite and TestRunner. See TestPerceptron.py for usage.

```python
import unittest

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

## How to traverse a directory hierarchy?

```python
import osfor
root, dirs, files in os.walk("/mydir"):    
  for file in files:        
    if file.endswith(".txt"):             
      print(os.path.join(root, file))
```

## How to select a random item from a list?

```python
import random
move=random.choice(possibleMoves)
```

## Logger

```python
import logging
```

Start python with the `--log=INFO` to set the logging level.

## How to get localization in python message

How to make a string translated in another language using GNU gettext.

See the code test_localize.py

* install poedit
* upadte PATH to point to `C:\Program Files (x86)\Poedit\GettextTools\bin`
* get the localizable string from the python program
* xgettext -d app -o localize/app.pot test_localize.py
* then create localize/fr/LC_MESSAGES/app.po from the created app.po under localize
* Compile the po to mo: msgfmt -o localize/fr/LC_MESSAGES/app.mo localize/fr/LC_MESSAGES/app
* export LANG=fr
* python test_localize.py


## Reading Files

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

## How to get execution time

```python
import time
start = time.perf_counter()
# potentially slow computation
end = time.perf_counter() - start
```

## Example of memory consumption for object

```python
import sys

a = 3
b = 3.123
c = [a, b]
d = []
for obj in [a, b, c, d]:
  print(obj, sys.getsizeof(obj))
```

## Using [CloudEvent](https://github.com/cloudevents/sdk-python)

```python
attributes = {
      "type": "com.anycompany.bdcp.user",
      "source": "https://anycompany.com/user-mgr",
}
data = { "eventType": "UserLogin", "username": "bob.the.builder@superemail.com"}
event = CloudEvent(attributes, data)
print(event)
```

## What is zip?

Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterable:

```python
dataset
[[1, 20, 0], [2, 21, 1], [3, 22, 0]]
for a in zip(*dataset): print(a)
(1, 2, 3)
(20, 21, 22)
(0, 1, 0)
```

## How to use some math

```python
# modulo
8 % 2
0
#
```

## What is a package?

A package is nothing more than a folder, which must contain a special file, __init__.py. (not needed anymore with python3.3+)

## What are namespace and scope?

A namespace is a mapping from names to objects. They are the built-in names, the global names in a module, and the local names in a function.
A scope is a textual region of a Python program, where a namespace is directly accessible. There are four different scopes that Python makes accessible:

* The local scope, which is the innermost one and contains the local names.
* The enclosing scope, that is, the scope of any enclosing function. It contains non-local names and also non-global names.
* The global scope contains the global names.
* The built-in scope contains the built-in names.

## customize matplotlib graph

```python
    graph.set_title("Results of 500 slot machine pulls")
    # Make the y-axis begin at 0
    graph.set_ylim(bottom=0)
    # Label the y-axis
    graph.set_ylabel("Balance")
    # Bonus: format the numbers on the y-axis as dollar amounts
    # An array of the values displayed on the y-axis (150, 175, 200, etc.)
    ticks = graph.get_yticks()
    # Format those values into strings beginning with dollar sign
    new_labels = ['${}'.format(int(amt)) for amt in ticks]
    # Set the new labels
    graph.set_yticklabels(new_labels)
```


???- question "How to program web socket server"
      See [FastAPI doc](https://fastapi.tiangolo.com/advanced/websockets/) with [testing](https://fastapi.tiangolo.com/advanced/testing-websockets/) and matching code in [websocket_server](https://github.com/jbcodeforce/python-code/tree/master/web_server/websocket_server)

???- question "Using async IO?"
      async IO is a single-threaded, single-process design: it uses cooperative multitasking. [See this tutorial](https://realpython.com/async-io-python/): concurrency encompasses both multiprocessing (ideal for CPU-bound tasks) and threading (suited for IO-bound tasks). Async io is supported by `async` and `await` language keywords. Asynchronous routines are able to “pause” while waiting on their ultimate result and let other routines run in the meantime.  `await` passes function control back to the event loop
      See code in [api_stream](https://github.com/jbcodeforce/python-code/tree/master/web_server/api_stream/)