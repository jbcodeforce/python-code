# Python FAQ

## Why pipenv?

pipenv resolves the problem of dependencies management, that is not perfectly done in the requirements.txt, which leads to under deterministic build process. Given the same input (the requirements.txt file), pip doesn’t always produce the same environment. `pip freeze` helps to freeze the dependencies and update the
 requirements.txt. But any dependency change needs to be done manually, and you need to track the dependent package version, for bug fix, or mandatory security fixes.

A second problem is the system wide repository used by pip. When developing multiple different projects in parallele that could become a real issue. `pipenv` use a per project environment.
pipenv acts as pip + virtual environment. It uses Pipfile to replace requirements.txt and pipfile.lock for determnistic build. See [this guide](https://realpython.com/pipenv-guide/) for command examples.

## How to get program arguments?

See [getopt](https://docs.python.org/3/library/getopt.html)

```python
  import sys,getopt
  USER="jbcodeforce"
  FILE="./data/export-questions.json"
  try:
    opts, args = getopt.getopt(sys.argv,"hi:u:",["inputfile=","user="])
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

## Pass a variable number of arguments to a function

We can pass a variable number of arguments to a function using special symbols:

* *args (Non-Keyword Arguments): take in more arguments than the number of formal arguments that you previously defined
* **kwargs (Keyword Arguments):  used to pass a keyworded, variable-length argument list.

```python
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
```


## what `__init__.py` under folder used for?

The `__init__.py` file makes Python treat directories containing it as modules. Furthermore, this is the first file to be loaded in a module, so you can use it to execute code that you want to run each time a module is loaded, or specify the submodules to be exported.

## How to get program dependencies generated?

To be able to run the python program at any time in the future, it is recommended to freeze the dependencies, so the requirements.txt will have the compatible module versions. 

```shell
pip freeze > requirements.txt
```

## Develop a module to be installable with pip

See [this article](https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/), and [Python Packaging User Guide](https://packaging.python.org/en/latest/) summarized as:

1. Create a python package (folder) with the setup.py in it. 

  ```python
  from setuptools import setup, find_packages

  setup(
      name="jb_module",
      version="0.1.0",
      description="The backend to support hybrid AI",
      author="Jerome Boyer",
      packages=find_packages(include=["acme"]),
      install_requires=['uvicorn', 'fastapi', 'langchain-openai','langchain-anthropic','langchain_ibm','langchain_community',
  'pydantic','python-multipart','python-dotenv','markdown','chromadb','pypdf'], 
  )
  ```

1. `pip3 install setuptool`
1. install in current virtual env: `pip install .` or `pip install --upgrade .`. Install with `pip uninstall jb_module`
1. Add a `__init__.py` file under the jb_module folder specify version...

  ```python
  __version__ = "0.1.0"
  __author__ = 'Jerome Boyer'
  __credits__ = ''
  ```
1. Create a source distribution with: `python setup.py sdist`, it contains a compressed archive of the package
1. Install twine to be able to upload to PyPi: `pip install twine`
1. Push the package to test.pypi.org

## Access environment variable

Define environment variables in a `.env` file, use os package:

```python
import os

AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
```

???- question "How to assess the type of an object?"
    '''python
    type(x) == str
    '''

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


Use `TestSuite` and `TestRunner`. See TestPerceptron.py for usage.

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
LOGGER = logging.getLogger(__name__)
LOGGER.info("an interesting string")
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


## How to program web socket server?

See [FastAPI doc](https://fastapi.tiangolo.com/advanced/websockets/) with [testing](https://fastapi.tiangolo.com/advanced/testing-websockets/) and matching code in [websocket_server](https://github.com/jbcodeforce/python-code/tree/master/web_server/websocket_server)

## Using async IO

**Multiprocessing** is ideal for CPU-bound tasks (for-loop code) and uses multiple core to run code in parallel. **Concurrency** is the property to run in an overlapping manner. **Threading** is a concurrent execution model whereby multiple threads take turns executing tasks. Threads are used for IO-bound jobs (waiting on input/output to complete).
The Python aAsync IO is a single-threaded, single-process design: it uses **cooperative multitasking**. [See this tutorial](https://realpython.com/async-io-python/#the-rules-of-async-io): Async io is supported by `async` and `await` language keywords. Asynchronous routines are able to *pause* while waiting on their ultimate result and let other routines run in the meantime. async model is built around concepts such as callbacks, events, transports, protocols, and futures. `await` passes the function control back to the event loop. A **coroutine** is a function that can suspend its execution before reaching return. The `async def` for a function, creates a native **coroutine**, or an asynchronous generator.
See code in [api_stream](https://github.com/jbcodeforce/python-code/tree/master/web_server/api_stream/).
  `async for` and `async with` are generators too. To call a coroutine function, you must await it to get its results.
`test_stream()` is suspended until it got the results from `call_llm_astream()`:

```python
async def test_stream():
  await call_llm_astream()
```

To run a corouting, we need the python asyncio module:

```python
async def main():
  await call_to_an_async_function()

if __name__ == "__main__":
    asyncio.run(main())
```

**yield** keyword in an `async def` block creates an asynchronous generator, which you iterate over with `async for`. A generator defined await and next methods. So it pushes value to calling stack at the yield level, but it also keeps a hold of its local variables when the program resume it by calling next() on it (`async for` calls the next() implicitly as it is a asynchronous iterator). 

By default, an async IO event loop runs in a single thread and on a single CPU core.
       