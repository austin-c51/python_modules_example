# refresher on fibonacci sequence: https://www.mathsisfun.com/numbers/fibonacci-sequence.html

import sys

def fib(n):
    if (n <= 0):
        sys.exit('Error: The argument supplied to fib() must be a positive integer')

    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=' ')
        a, b = b, a+b
        count += 1
    print()
