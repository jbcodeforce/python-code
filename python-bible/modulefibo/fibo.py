
def print_fib(n) :
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def serie_fib(n) :
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a,b = b,a+b
    return result
