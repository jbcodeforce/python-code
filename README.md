# Python Code

A bench of python code from training and studies and raspberry work. For python summary see [this site](https://jbcodeforce.github.io/#/studies)

## Development environment with docker

While developing on Mac which uses python for its own OS, it is important to isolate the development from the operation of the OS and avoiding compromising the integrity of the whole system. So virtualenv can be used, but docker presents a lot of advantages too:
* avoid installing software not used often on the native OS
* describe the dependencies on library so programs developed 5 years ago will still run
* easy to switch laptop
* quicker provisioning than a VM running with Vagrant, still offering mounting host folder, running under localhost
* use docker compose for each project to manage component dependencies
* still use virtual environment to isolate per project

## Execution

There are two ways to do isolation: docker or virtual env, and in fact it is recommended to combine both:

### Use docker image

The Dockerfile in the current project define an image for running python 3.7 with Flask, and virtual environment.

` docker run -e DISPLAY=192.168.1.89:0 --name jbcodeforcepython -v $(pwd):/home/jbcodeforce/work -it --rm -p 5000:5000 jbcodeforce/python3.7 /bin/bash `

### Virtual env

**virtualenv** is a tool for isolating your application in what is called a virtual environment. A virtual environment is a directory that contains the software on which your application depends. A virtual environment also changes your environment variables to keep your development environment contained. Instead of downloading packages, like Flask, to your system-wide — or user-wide — package directories, we can download them to an isolated directory used only for our current application.

You could install virtualenv with `pip install virtualenv`virtualenv -p /Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 .venv

Create virtual environment under your project folder with the command:
`virtualenv -p /Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 .venv`

### Activate the virtual environment

The angular-flask project includes a start.sh script to prepare the virtual env.
```
source .venv/bin/activate

python3 programname.py

deactivate
```

## Code in the order of knowledge acquisition

### Basics
* [firstinput.py](python-bible/firstinput.py) for reading user input
* [Variable scope](python-bible/scope.py)
* [travis.py](python-bible/travis.py) to play with lists, for in range and conditions
* [cinema.py](python-bible/cinema.py) for dictionary
* [Play with data structures](python-bible/datastructure.py)
* [Reverse a word and add aye](python-bible/pig.py), use loops, break, in voyals...
* [Object Oriented Python](python-bible/coins.py)
* [modules, import, and packages](python-bible)
* [Flask web app](angular-flask/helloworld/firstApp.py) then firstRESTApp.py and staticApp.py
* [Flask serving a simple angular App](angular-flask/angularApp)

### Algorithms

* [Binary Tree with InOrderTraversal, PreOrderTraversal, PostOrderTraversal](algorithms/traversalbinarytree.py).
* [Binary search within a sorted array](algorithms/binarySearch.py) which is a divide and conquer algorithm.
* [DFS, graph, BFS](algorithms/Graph.py) DFS: explores the highest-depth nodes first before being forced to backtrack and expand shallower nodes. BFS: explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

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

### Tuples
```
tup1 = ('physics', 'chemistry', 1997, 2000);
print ("tup1[0]: ", tup1[0]);
# iteration
for a in tup1:
  print(a)
```
They are immutable. Need to create new tuples from existing one. Removing individual tuple elements is not possible.

### To share code with people
You can use gist.github.com


## References
* http://docs.python.org/3/tutorial/index.html
* http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/
* http://www.secnetix.de/olli/Python/
* http://www.brunningonline.net/simon/python/quick-ref2_0.html#LexEnt
