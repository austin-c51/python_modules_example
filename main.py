import sys
from fibonacci import fib

if __name__ == '__main__':
    if (len(sys.argv) < 2 or not sys.argv[1].isdigit()):
        sys.exit('Error: You must enter an integer as argument.')

    fib(int(sys.argv[1]))
