"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
matching values 1,5,10,50,100,500,1000
Roman numerals are usually written largest to smallest from left to right.

Some rules to respect:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Approach: parse roman number representation char by char and match the char read
to a k in a dict to get matching value.
"""

symbols = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}


def roman_to_int(roman: str) -> int:
    n=0
    i = 0
    previous = ''
    while i < len(roman):
        c = roman[i]
        if (c == 'V' or c == 'X') and previous == 'I':
            n=n+symbols[c]-2
        elif (c == 'L' or c == 'C') and previous == 'X':
            n=n+symbols[c]-20
        elif (c == 'D' or c == 'M') and previous == 'C':
            n=n+symbols[c]-200
        else:
            n=n+symbols[c]
        previous=c
        i+=1
    return n


def better_sol(roman: str) -> int:
    ans = 0
    
    for i in range(len(roman)):
        if i < len(roman) - 1 and symbols[roman[i]] < symbols[roman[i+1]]:
            ans -= symbols[roman[i]]
        else:
            ans += symbols[roman[i]]
    
    return ans

assert roman_to_int("III") == 3
assert roman_to_int("IV") == 4
assert roman_to_int("IX") == 9
assert roman_to_int("XL") == 40
assert roman_to_int("XC") == 90
assert roman_to_int("LVII") == 57
assert better_sol("MCMXCIV") == 1994
