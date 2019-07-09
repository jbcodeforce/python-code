# Python FAQ

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
```
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
