# PoC Python

Playground for learning about Python.

[https://www.python.org/](https://www.python.org/)

Current version: 3.5.0

## Python koans
[https://github.com/gregmalcolm/python_koans/wiki](https://github.com/gregmalcolm/python_koans/wiki)



## Head First Python
###Source examples:
* [http://www.headfirstlabs.com/books/hfpython/](http://www.headfirstlabs.com/books/hfpython/)
* [http://programming.itcarlow.ie/](http://programming.itcarlow.ie/)

###Chapter 1: Meet Python
* IDLE: Integrated Development Environment
* The characters `>>>` are called 'triple chevron'.
* Python code needs to be indented (instead of C-like languages which use {}).
* BIF: built-in function
* **Suite:** a block of Python code, which is indented to indicate grouping.
* It is case sensitive!
* Lists can contain anything!
* Lists in Python high-level collections, the are collection objects.
* Python lists can contain data of mixed type.
* `isinstance(variableName, variableType)` 
* This Python philosophy is known as “batteries included”: there’s enough included with Python to let you do most things well, without having to rely on code from third parties to get going
* Identifiers are names that refer to data objects. The identifiers have no “type,” but the data objects that they refer to do.
  
  
##Chapter 2: Modules of functions
* The Python Package Index (or PyPI for short) provides a centralized repository for third-party Python modules on the Internet. When you are ready, you’ll use PyPI to publish your module and make your code available for use by others.
* A module is simply a text file that contains Python code. The main requirement is that the name of the file needs to end in .py.
* Comments: use a triple double-quote for multiple-line comments, or `#` for a single line.
* Where are the Python modules?:
 * Run the IDLE: `python`
 * `import sys;`
 * `sys.path`
* In order to share your newly created module, you need to prepare a distribution.
 1. Create setup.py under a folder
 2. Build the distribution file: `python3 setup.py sdist`
 3. Install your distribution into your local copy of Python: `python3 setup.py install`
* To use a module, simply import it into your programs or import it into the IDLE shell

###Namespaces
All code in Python is associated with a namespace.
Code in your main Python program (and within IDLE’s shell) is associated with a namespace called __main__. 
When you put your code into its own module, Python automatically creates a namespace with the same name as your module.

* Register at [https://pypi.python.org](https://pypi.python.org)
 * For testing [https://wiki.python.org/moin/TestPyPI](https://wiki.python.org/moin/TestPyPI) >> create ~/.pypirc
  1. Modify `~/.pypirc`
  2. `python3 setup.py register -r https://testpypi.python.org/pypi`
  3. `python3 setup.py **sdist** upload -r https://testpypi.python.org/pypi`
  4. `pip install -i https://testpypi.python.org/pypi <packageName>`

**pyc**: When the interpreter executes your module code for the first time, it reads in the code and translates it into an internal bytecode format which is ultimately executed. The Python interpreter is smart enough to skip the translation phase the next time your module is used, because it can determine when you’ve made changes to the original module code file. If your module code hasn’t changed, no translation occurs and the “compiled” code is executed. If your code has changed, the translation occurs (creating a new pyc file) as needed. The upshot of all this is that when Python sees a pyc file, it tries to use it because doing so makes everything go much faster.

`for num in range(4):`

* the BIFs have their very own namespace called (wait for it) __builtins__
* Including end=’’ as a argument to the print() BIF switches off its automatic inclusion of a new-line on output.

##Chapter 3: files and exceptions

**Bookmark Head First Python:** page 75