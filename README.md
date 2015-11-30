# PoC Python

Playground for learning about Python.

[https://www.python.org/](https://www.python.org/)

Current version: 3.5.0

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
* `isinstance(variableName, variableType)` 
* This Python philosophy is known as “batteries included”: there’s enough included with Python to let you do most things well, without having to rely on code from third parties to get going
* Identifiers are names that refer to data objects. The identifiers have no “type,” but the data objects that they refer to do.
  
  
##Chapter 2: Modules of functions
* The Python Package Index (or PyPI for short) provides a centralized repository for third-party Python modules on the Internet. When you are ready, you’ll use PyPI to publish your module and make your code available for use by others.
* Comments: use a triple quote for multiple-line comments, or `#` for a single line.
* Where are the Python modules?:
 * Run the IDLE: `python`
 * `import sys;`
 * `sys.path`
* In order to share your newly created module, you need to prepare a distribution.
 1. Create setup.py under a folder
 2. Build the distribution file: `python3 setup.py sdist`
 3. Install your distribution into your local copy of Python: `python3 setup.py install`
 

**Bookmark Head First Python:** page 40
