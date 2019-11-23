# Python Studies

Read in [book format](http://jbcodeforce.github.io/python-code)

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
* [Plotting normal curve with matplotlib](mapplotlib/PlotGaussian.py)

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
