"""Lambda :- Functions or arguements."""
add = lambda a: a + 5
mult = lambda m, n: m*n                                              # Lambda performs as a simple function.
print(add(5), mult(5, 3))                        # [1]

def AM(p, q):
    return p+5, p * q                                                # Function takes 2 lines whilst lambda takes 1.
print(AM(5, 3))                                  # [2]

# Sorted (iterable, key = argument)
cords = [(4, 6), (1, 5), (8, 3)]

srt = sorted(cords, key= lambda o: o[1])                             # Sorting a list by the value of the second item.
print(srt)                                       # [3]

def Srt(p):
    return p[1]
srtF = sorted(cords, key=Srt)                                        # Using a function as an arguement
print(srtF)                                      # [4]

srt_add = sorted(cords, key= lambda a: a[0] + a[1])                  # Sorting the list based on the sum of the elments in the tuple.
print(srt_add)                                   # [5]

# Map (function, iterable)
odd_n = [1, 2, 3, 4, 5, 6, 7]

sqr = map(lambda s: s**2, odd_n)                                       # Carries out certain operation for each content of the iterable.
print(list(sqr))                                  # [6]

odd1 = map(lambda e: e % 2 == 0, odd_n)                                # Prints out bool output.
odd2 = map(lambda e: e % 2, odd_n)                                     # Prints out in 1 and 0.
print(list(odd1), list(odd2))                     # [7]

sqr2 = [s**2 for s in odd_n]                                           # The same can be done by List Comprehension.
print(sqr2)                                       # [8]

# Filter (function, iterable)
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = filter(lambda e: e % 2 == 0, num)                               # Only prints out the elements that satisfy the condition.
odd = filter(lambda e: e % 2, num)                                     # If condition not stated, it'll print those which give out 'True' or '1'.
three = filter(lambda t: t == 3**2, num)
print(list(even), list(odd), list(three))         # [9]

even_lc = [e for e in num if e % 2 == 0]
print(even_lc)                                    # [10]

# Reduce
from functools import reduce
numb = [1, 2, 3, 4, 5]
red = reduce(lambda r, s: r*s, numb)                                   # Carries out the operation from one number to another for the whole list.
print(red)                                        # [11]
