a = 'dead' # Define three attributes
b = 'parrot' # Exported to other files
c = 'sketch'
print(a, b, c) # Also used in this file (in 2.X: print a, b, c)

"""
❯ python threenames.py
dead parrot sketch

>>> import threenames
dead parrot sketch
>>> from threenames import a,b,c
>>> a,b,c
('dead', 'parrot', 'sketch')
>>> import threenames
>>> threenames.a,threenames.b,threenames.c
('dead', 'parrot', 'sketch')
>>> dir(threenames)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'c']


Built-in Special Attributes Explained:
__builtins__:
What it is: A reference to the built-in module builtins, which contains Python’s built-in functions (like print(), len(), type(), etc.) and exceptions.

Purpose: Ensures that the module has access to these fundamental tools without needing to import them explicitly.

Value: It’s typically a module object (<module 'builtins' (built-in)>).

Example Use: You wouldn’t usually interact with it directly, but it’s there so print() works in your module without extra imports.

__cached__:
What it is: The file path to the cached bytecode file (e.g., a .pyc file) if the module was compiled and cached.

Purpose: Python caches compiled versions of .py files to speed up future imports. This attribute stores that location.

Value: A string (e.g., 'path/to/threenames.cpython-39.pyc') or None if no cached file exists.

Example Use: Rarely used directly, but it’s useful for debugging import behavior.

__doc__:
What it is: The docstring of the module, if one was defined.

Purpose: Provides documentation about the module’s purpose, written as a string at the top of the file.

Value: A string (e.g., 'This module does XYZ') or None if no docstring exists.

Example:
python


"""