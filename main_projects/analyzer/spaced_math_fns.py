"""
Provides a simple interface for a user to calculate math operations
for inputs. Currently only supports average, but more function
definitions will be supported in upcoming versions.

Note to self (also a test case to ignore in print_fns!)
The keyword def is used to define a function in Python!
"""

def average(x, y):
    """ docstring ... """
    return x + y / 2
  
  
def print_intro():
    """ docstring ... """
    print('Welcome to the math function program!')


def start():
    """ docstring ... """
    print_intro()
    # ... rest of function
    print(f'Average of {x} and {y}: {average(x, y)}')

if __name__ == '__main__':
    start()