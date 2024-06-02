"""
Given an integer x, return true if x is a 
palindrome, and false otherwise.

palindrome a number or string that can be read from both direction.

Could you solve it without converting the integer to a string?
"""
import math
def length(n: int) -> int:
    l=1
    if (n < 0):
        n=-n
    while n >= 10:
        n=n//10
        l+=1
    return l

def is_palindrome(n: int) -> bool:
    if n < 0: 
        return False
    l = []
    nb_digits : int = length(n)
    z=n
    e=nb_digits-1
    while len(l) < nb_digits:
        div = math.pow(10,e)
        r = z % div
        a = z // div
        l.append(a)
        z=r
        e-=1
        print(div, a, r) 
    print(l)
    i=0
    j=nb_digits-1
    while i<=j:
        if l[i] != l[j]:
            return False
        i+=1
        j-=1
    return True

def better_sol(n: int) -> bool:
    """
    reverse the number and reversed and n should be the same.
    To reverse the number add the rest of div / 10 to current reversed number * 10
    t=121  reversed = 1
    t=12   reversed = 12
    t=1    reversed = 121
    """
    if n < 0:
        return False
    reversed = 0
    temp = n
    while temp != 0:
        r = temp % 10
        reversed = reversed * 10 + r
        temp //=10
    return reversed == n

assert length(1) == 1
assert length(12) == 2
assert length(212) == 3
assert length(-212) == 3
assert length(3142) == 4

assert is_palindrome(1)
assert is_palindrome(11)
assert is_palindrome(121)
assert not is_palindrome(-121)
assert not is_palindrome(1341)
assert is_palindrome(1234321)
assert better_sol(1234321)



