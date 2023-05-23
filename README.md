# Python modules example

This repository houses an example of using a Python file as a module that can be imported and used in another file.

The `fibonacci.py` file contains code that will print the first N numbers of the Fibonacci sequence. The first lines
of `main.py` import the `fib()` function defined in `fibonacci.py`, and then call that function using input from the
user. Some validation is included in `main.py` to verify the input supplied by the user.

## Examples
```
% python main.py 1
0

% python main.py 8
0 1 1 2 3 5 8 13

% python main.py hello
Error: You must enter an integer as argument.
```

## Resources
* **For more on Python modules:** https://docs.python.org/3/tutorial/modules.html
* **For a refresher on the Fibonacci sequence:** https://www.mathsisfun.com/numbers/fibonacci-sequence.html
