# This sample illustrates TestCases, module imports: import module from current directory
from modulefibo import fibo 
import unittest

class TestFiboModule(unittest.TestCase):

    def test_printFibo(self):
        fibo.print_fib(10)
    
    def test_fibo(self):
        self.assertEqual(fibo.serie_fib(10), [1,1,2,3,5,8])


if __name__ == '__main__':
    unittest.main()
