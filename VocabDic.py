python_dictionary = {
    "print": "\n\nDisplays the specified message or value in the console\n\nExample: print('Hello, world!')\n\n",
    "if": "\n\nUsed to test a condition and execute code if the condition is true\n\nExample: if x > 5:\n    print('x is greater than 5')\n\n",
    "else": "\n\nExecutes code if the condition in the if statement is false\n\nExample: if x > 5:\n    print('x is greater than 5')\nelse:\n    print('x is less than or equal to 5')\n\n",
    "for": "\n\nUsed to loop over a sequence of elements\n\nExample: for x in range(5):\n    print(x)\n\n",
    "while": "\n\nExecutes a block of code as long as a specified condition is true\n\nExample: x = 0\nwhile x < 5:\n    print(x)\n    x += 1\n\n",
    "def": "\n\nUsed to define a function\n\nExample: def greet(name):\n    print('Hello, ' + name)\n\n",
    "return": "\n\nUsed to exit a function and return a value\n\nExample: def add(x, y):\n    return x + y\n\n",
    "import": "\n\nUsed to import modules or packages in Python\n\nExample: import math\n\n",
    "try": "\n\nUsed to catch and handle exceptions in code\n\nExample: try:\n    x = int(input('Enter a number: '))\nexcept ValueError:\n    print('That is not a valid number')\n\n",
    "except": "\n\nExecutes code when an exception occurs in a try block\n\nExample: try:\n    x = int(input('Enter a number: '))\nexcept ValueError:\n    print('That is not a valid number')\nelse:\n    print('You entered:', x)\n\n",
    "range": "\n\nReturns a sequence of numbers, starting from 0 by default, and increments by 1 (by default) and stops before a specified number\n\nExample: for x in range(5):\n    print(x)\n\n",
    "break": "\n\nTerminates the loop statement and transfers execution to the statement immediately following the loop\n\nExample: for x in range(5):\n    if x == 3:\n        break\n    print(x)\n\n",
    "continue": "\n\nSkips the rest of the current iteration of the loop and continues with the next iteration\n\nExample: for x in range(5):\n    if x == 3:\n        continue\n    print(x)\n\n",
    "finally": "\n\nExecutes code regardless of the result of the try and except blocks\n\nExample: try:\n    x = int(input('Enter a number: '))\nexcept ValueError:\n    print('That is not a valid number')\nelse:\n    print('You entered:', x)\nfinally:\n    print('Thank you for using the program')\n\n",
    "raise": "\n\nUsed to raise an exception\n\nExample: raise ValueError('Invalid input')\n\n",
    "with": "\n\nUsed to simplify exception handling and clean-up code\n\nExample: with open('file.txt', 'r') as f:\n\n",
    "assert": "\n\nUsed for debugging purposes to check if a condition is True, if not, it raises an AssertionError\n\nExample: assert x > 0, 'x should be greater than 0'\n\n",
    "lambda": "\n\nUsed to create small, anonymous functions\n\nExample: add = lambda x, y: x + y\n\n",
    "map": "\n\nUsed to apply a function to every item in an iterable and return a new iterable\n\nExample: list(map(lambda x: x*2, [1, 2, 3]))\n\n",
    "filter": "\n\nUsed to filter out elements from an iterable based on a condition and return a new iterable\n\nExample: list(filter(lambda x: x > 2, [1, 2, 3, 4]))\n\n",
    "reduce": "\n\nUsed to apply a function to an iterable and reduce it to a single value\n\nExample: from functools import reduce\n         reduce(lambda x, y: x*y, [1, 2, 3, 4])\n\n",
    "concatenate": "\n\nTo combine two or more strings or other objects into one\n\nExample: a = 'Hello'; b = 'World'; c = a + b\n\n",
    "enumerate": "\n\nTo loop over an iterable and keep track of the index of the current item\n\nExample: for index, value in enumerate(['a', 'b', 'c']): print(index, value)\n\n",
    "global": "\n\nA keyword used to access a global variable from within a function\n\nExample: x = 10\ndef myfunc():\n    global x\n    x = 20\nmyfunc()\nprint(x)\n\n",
    "immutable": "\n\nA value or object that cannot be modified after it is created\n\nExample: Strings in Python are immutable, so you cannot change a character in a string once it is created\n\n",
    "mutable": "\n\nA value or object that can be modified after it is created\n\nExample: Lists in Python are mutable, so you can add or remove elements from a list after it is created\n\n",
    "object": "\n\nA data structure that contains data and methods for working with that data\n\nExample: A string in Python is an object, with methods like upper() and lower() that can be used to manipulate the string\n\n",
    "pop": "\n\nA method used to remove and return an element from a list by its index\n\nExample: a = [1, 2, 3]; b = a.pop(1); print(a, b)\n\n",
    "push": "\n\nTo add an element to the end of a list or other data structure\n\nExample: a = [1, 2, 3]; a.append(4); print(a)\n\n",
    "queue": "\n\nA data structure that allows elements to be added to the end and removed from the front\n\nExample: Python's deque class can be used to implement a queue\n\n",
    "recursion": "\n\nA process where a function calls itself to solve a problem\n\nExample: The factorial function can be implemented recursively as factorial(n) = n * factorial(n-1) for n > 1, with a base case of factorial(0) = 1\n\n",
    "set": "\n\nA data structure that contains a collection of unique elements\n\nExample: a = {1, 2, 3}; b = {2, 3, 4}; print(a.intersection(b))\n\n",
    "stack": "\n\nA data structure that allows elements to be added to and removed from the top\n\nExample: A stack can be implemented using a list by using the append() method to add elements and the pop() method to remove elements from the end\n\n",
    "string": "\n\nA sequence of characters\n\nExample: a = 'Hello World'; print(len(a))\n\n",
    "variable": "\n\nA name that refers to a value or object in memory\n\nExample: x = 10; print(x)\n\n",
    "integer": "\n\nA whole number, positive or negative, without decimals\n\nExample: 42\n\n",
    "float": "\n\nA number, positive or negative, containing one or more decimals\n\nExample: 3.14\n\n",
    "boolean": "\n\nA data type that can only have two values: True or False\n\nExample: True\n\n",
    "list": "\n\nA collection of items that are ordered and changeable. Lists are written with square brackets\n\nExample: [1, 2, 3]\n\n",
    "tuple": "\n\nA collection of items that are ordered and unchangeable. Tuples are written with round brackets\n\nExample: (1, 2, 3)\n\n",
    "set": "\n\nA collection of items that are unordered and unindexed. Sets are written with curly braces\n\nExample: {1, 2, 3}\n\n",
    "dictionary": "\n\nA collection of key-value pairs that are ordered and changeable. Dictionaries are written with curly braces and colons\n\nExample: {'name': 'John', 'age': 30}\n\n",
    "index": "\n\nThe position of an item in an ordered collection\n\nExample: my_list = [10, 20, 30]\n          print(my_list.index(20))  # Output: 1\n",
    "iterable": "\n\nAn object that can be iterated over. Examples include lists, tuples, and sets\n\nExample: my_list = [10, 20, 30]\n         for item in my_list:\n             print(item)\n",
    "sequence": "\n\nA type of iterable where the items are ordered and can be indexed. Examples include strings, lists, and tuples\n\nExample: my_string = 'hello'\n         my_list = [10, 20, 30]\n         my_tuple = (40, 50, 60)\n",
    "element": "\n\nAn individual item in an iterable\n\nExample: my_list = [10, 20, 30]\n         print(my_list[1])  # Output: 20\n",
    "function": "\n\nA block of code that performs a specific task, and can be called from anywhere in the program\n\nExample: def add_numbers(a, b):\n             return a + b\n         print(add_numbers(2, 3))  # Output: 5\n",
    "parameter": "\n\nA variable in a function definition that is used to pass data into the function\n\nExample: def add_numbers(a, b):\n             return a + b\n",
    "argument": "\n\nA value that is passed into a function when it is called\n\nExample: def add_numbers(a, b):\n             return a + b\n         print(add_numbers(2, 3))  # Output: 5\n",
    "module": "\n\nA file containing Python code that can be imported and used in another Python program\n\nExample: import math\n         print(math.pi)  # Output: 3.141592653589793\n",
    "package": "\n\nA directory containing multiple modules, along with an __init__.py file that specifies the package structure\n\nExample: In a directory named 'my_package':\n\n             my_package/\n                 __init__.py\n                 module1.py\n                 module2.py\n\n         import my_package.module1\n         print(my_package.module1.some_function())\n",
    "syntax": "\n\nThe rules and structure of a programming language\n\nExample: x = 5\n         if x == 5:\n             print('x is 5')\n",
    "indentation": "\n\nThe spaces or tabs at the beginning of a line of code that determine the scope of the code block\n\nExample: def some_function():\n             print('This is indented')\n         if True:\n             print('This is also indented')\n",
    "comment": "\n\nA line of text in a program that is ignored by the Python interpreter\n\nExample: # This is a comment\n         print('This is not a comment')\n",
    "docstring": "\n\nA multi-line comment used to document a function, module, or package\n\nExample: def some_function():\n             \"\"\"This function does something.\"\"\"\n             return\n",
    "try-except": "\n\nA block of code used to handle exceptions in a program. The code in the try block is executed, and if an exception occurs, the code in the except block is executed instead\n\nExample: try:\n             print(1 / 0)\n",
    "class": "\n\nA blueprint for creating objects, defined using the class keyword\n\n",
    "object": "\n\nAn instance of a class\n\n",
    "inheritance": "\n\nThe ability of a class to inherit methods and attributes from a parent class\n\n",
    "method": "\n\nA function defined within a class that operates on an object of that class\n\n",
}















































    







# to get meaning of a command






