import math

def exponential(base,exp):
    if base == 0:
        return 0
    if exp == 0:
        return 1
    else:
        if exp > 0:
            return base * exponential(base,exp-1)
        else:
            return 1/base * exponential(base,exp+1)
    

if __name__ == "__main__":
    print(exponential(0,2))
    print(exponential(2,3))
    assert exponential(2,-3) == math.pow(2,-3)
    print(exponential(5,-5))