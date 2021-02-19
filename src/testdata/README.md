# Test Creation Guide

So, you want to make a new ATMOS test routine?

We (the ATMOS team) have tried to keep it nice and simple so that you can test and test
to your heart's delight and never grow tired of it. Here's how it's done:

## 1. Create the file
In the `/src/testdata` directory or a subfolder (organize however),
create a new Python file (`.py` file extension). This file should be named
clearly so it is obvious what kind of test it is. Since the name of this
file will determine the name of the test class in Step 3, it must follow
Python's naming rules. Basically:

* Must begin with a letter or underscore
* No special characters except underscore
* Don't use reserved Python keywords

## 2. Import stuff
One of the first lines of the file should be (excluding any other `import` statements you may need/want):
```python
from .test_module import Test
```
This lets you make use of the `Test` base class which comes with a bunch
of (hopefully) helpful utility functions so that you can focus on how your
test will execute and worry less about writing lots of lines of Python
(leave that part to us).

## 3. Make a test class
ATMOS tests are structured as classes that inherit from the `Test` abstract
base class. **Please don't make any changes to** `Test` **directly, and**
**please don't override any methods other than** `execute()`, **thanks!**

"What shall I name my super-cool ATMOS test class?" you wonder aloud. The
class name ***must*** have the same name as the Python file it lives in,
but with the first letter of each **word** (i.e. anything separated by underscores) capitalized, followed by the word `Test`. For
example:
```python
# File: example.py
from .test_module import Test
class ExampleTest(Test):
    # ...
```
```python
# File: my_super_cool_test.py
from .test_module import Test
class My_Super_Cool_TestTest(Test):
    # this super cool name turned out to be super weird looking
    # ...
```
## 4. Override the `execute()` method
This method is where you put the body of your test code. Note that keyword
arguments are permitted, but positional arguments are not. This overridden
method basically just needs to follow one rule: return `True` if it is able
to execute to the end with no exceptions, `False` if there is an error,
even if it is handled in a `try...except` block (which it should be so
that ATMOS doesn't crash).

A complete (but useless) example follows:
```python
# File: something.py
from .test_module import Test

class SomethingTest(Test):
    """ This is my amazing test of... something """

    def execute(self, length=1, width=2, height=3):
        """ A better docstring is needed """

        volume = length * width * height
        print(f"Volume: {volume}")

        return True
```