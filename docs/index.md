# Python Studies

This repository regroups a bench of python codes from my own self-training and studies for web development, crawling, python best practice, and [raspberry PI](https://www.raspberrypi.org/) work.

## Language Advantages / disadvantages

**Advantages:**

* Interpreted with shell to start quickly, more concise language
* 2nd most used programming language
* A lot of libraries, used a lot by data scientists
* Combines functional and OOP.
* Raspberry PI language of choice

**Disadvantages:**

* Slow, not supporting well multi cpu / threading architecture
* Not great for mobile and 3D game programming

## Code in the order of knowledge acquisition

### Basics

* [firstinput.py](https://github.com/jbcodeforce/python-code/blob/master/python-bible/firstinput.py) for reading user input
* [Variable scope](https://github.com/jbcodeforce/python-code/blob/master/python-bible/scope.py) between global, local,...
* [travis.py](https://github.com/jbcodeforce/python-code/blob/master/python-bible/travis.py) to play with lists, for in range() and conditions
* [cinema.py](https://github.com/jbcodeforce/python-code/blob/master/python-bible/cinema.py) to illustrate how to use for dictionary
* [Play with data structures](https://github.com/jbcodeforce/python-code/blob/master/python-bible/datastructure.py): lists, queues, matrix, sets, and more dictionaries, with how to navigate into those structures
* [Reverse a word and add aye](https://github.com/jbcodeforce/python-code/blob/master/python-bible/pig.py), use loops, break, in voyals...
* [Object Oriented Python](https://github.com/jbcodeforce/python-code/blob/master/python-bible/coins.py): classes and inheritance: using constructor (__init__()) and method with self argument.
* [Modules, import, and packages](https://github.com/jbcodeforce/python-code/blob/master/python-bible/TestFiboModule.py). Do not forget to set PYTHONPATH to the root folder to access any new modules

### Flask 

* [Flask web app hello world](https://github.com/jbcodeforce/python-code/blob/master/Flask/helloworld/firstApp.py) then [REST API end point with Flask](https://github.com/jbcodeforce/python-code/blob/master/firstRESTApp.py) and staticApp.py
* [Flask serving a simple angular App](https://jbcodeforce.github.io/angular-sandbox)
* [TDD with Flask app and docker from testdriven.io course](https://github.com/jbcodeforce/python-code/tree/master/flask-tdd-docker)


### Algorithms

* [Sorting arrays](https://github.com/jbcodeforce/python-code/blob/master/algorithms/sort.py): Bubblesort, selection sort, insertion sort and quicksort.
* [Binary Tree with InOrderTraversal, PreOrderTraversal, PostOrderTraversal](https://github.com/jbcodeforce/python-code/blob/master/algorithms/traversalbinarytree.py).
* [Binary search within a sorted array](https://github.com/jbcodeforce/python-code/blob/master/algorithms/binarySearch.py) which is a divide and conquer algorithm.
* [Depth First Search, graph, Breadth First Search](https://github.com/jbcodeforce/python-code/blob/master/algorithms/Graph.py) DFS: explores the highest-depth nodes first before being forced to backtrack and expand shallower nodes. BFS: explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.


### Graphics

* [Use a simple graphics API](https://github.com/jbcodeforce/python-code/blob/master/graphics/testgraphics.py) to create a window, draw circle and move them.
* [Plotting normal curve with matplotlib](https://github.com/jbcodeforce/python-code/blob/master/matplotlib/PlotGaussian.py)

### Web scrawling

Use urllib and beautiful soup to remove html tags from a web page to get text to parse. See [this note](webcrawling/readme.md) for guidances

* [Use regular expression (re module)](https://github.com/jbcodeforce/python-code/blob/master/web_data/countNumbers.py) to extract number from a text read from a file.

### Astronomy

See [detailed note here](astronomy/README.md) and code is under `astronomy` folder.

### AWS

To get some sample code to use AWS SDK [see this folder](https://github.com/jbcodeforce/python-code/blob/master/aws).

## Unit testing

* [Pytest framework](https://docs.pytest.org/en/7.3.x/#)
* [moto for backend mockup]http://docs.getmoto.org/en/latest/index.html)

## Some tricks

* placing cursor to previous line and enter will copy the line to a new line
