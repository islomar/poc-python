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
* `data = open('sketch.txt')` 
* `data.readline()`
* `data.seek(0)`: it can be used to “rewind” a file to the beginning.
* `data.close()`
* `each_line.find(':')`
* A **traceback** is a detailed description of the runtime error that has occurred.
* `try: except: finally:`
* A **ValueError** occurs when your data does not conform to an expected format.
* There are two types of list in Python: those that can change (enclosed in square brackets) and those that cannot be changed once they have been created (enclosed in regular brackets). The latter is an **immutable list**, more commonly referred to as a **tuple**. Think of tuples as the same as a list, except for one thing: once created, the data they hold cannot be changed under any circumstances. 
Another way to think about tuples is to consider them to be a constant list. At Head First, we pronounce “tuple” to rhyme with “couple.” Others pronounce “tuple” to rhyme with “rupal.” There is no clear concensus as to which is correct, so pick one and stick to it.
* When you have a situation where you might be expected to provide code, but don’t need to, use Python’s **pass** statement (which you can think of as the
empty or null statement): it does nothing.

## Chapter 4: Persistence, saving data to files
* The “strip()” method removes unwanted whitespace from a string.
* `if: elif:`
* `data = open('sketch.txt', 'w')`` >> open in write mode
 * When you use access mode w, Python opens your named file for writing. If the file already exists, it is cleared of its contents, or
clobbered. To append to a file, use access mode **a**, and to open a file for writing and reading (without clobbering), use **w+**. If you
try to open a file for writing that does not already exist, it is first created for you, and then opened for writing.
* print("Norwegian Blues stun easily.", file=out) >> file=the name of the data file objet to write to
* `out.close()` >> When you’re done, be sure to close the file to ensure all of your data is written to disk. This is known as flushing and is very important:
* Strings in Python are immutable.
* Python variables contain a reference to a data object. All of the number types are immutable.
* The locals() BIF returns a collection of names defined in the current scope:
	`finally:
		if 'data' in locals():
			data.close()`
* `except IOError as err:
		print('File error: ' + str(err))`
* Use **with** to work with files (When you use with, you no longer have to worry about closing any opened files, even when exceptions occure):
`
try:
	with open('its.txt', "w") as data:
		print("It's...", file=data)
except IOError as err:
	print('File error: ' + str(err))
`
 * The with statement takes advantage of a Python technology called **the context management protocol**.
* In Python, standard output is referred to as **sys.stdout**
* Python ships with a standard library called **pickle**, which can save and load almost any Python data object, including lists. Once you pickle your data to a file, it is persistent and ready to be read into another program at some later date/time.
 * You can, for example, store your pickled data on disk, put it in a database, or transfer it over a network to another computer. When you are ready, reversing this process unpickles your persistent pickled data and recreates your data in its original form within Python’s memory
 * Save with pickle.dump()** and restore with **pickle.load()**
 `with open('mydata.pickle', 'wb') as mysavedata:
		pickle.dump([1, 2, 'three'], mysavedata)`
 * `b` tells Python to open the file in binary mode.
* **Pickling** - the process of saving a data object to persistence storage.
* **Unpickling** - the process of restoring a saved data object from persistence storage.


## Chapter 5: Comprehending data
* `data.sort()`: in-place sorting (the list is replaced)
* `data2 = sorted(data, reverse=True)`: copied sorting
* **List comprehension:** specifying the transformation that is to be applied to each of the data items within an existing list.
* Comprehending list: `clean_mikey = [sanitize(each_t) for each_t in mikey]`
* `distances = set(james)`: data items in a set are unordered and duplicates are not allowed. 
* **Factory Function:** A factory function is used to make new data items of a particular type. For instance, “set()” is a factory function because it makes a new set. In the real world, factories make things, hence the name.
* `my_list[3:6]`: a slice.


## Chapter 6: custom data objects
* **dictionary:** it associates data values with keys (like a Map, Hash, associate array, etc.) 
* **Dictionary:** A built-in data structure (included with Python) that allows you to associate data with keys, as opposed to numbers. This lets your in-memory data closely match the structure of your actual data
* In order to create a dictionary: 
 * `cleese = {}`
 * `palin = dict()`
 * `palin['Name']` Use square brackets to index into the dictionary to access data items, but instead of numbers, index with keys.               
 * `cleese['Occupations'][-1]` Use numbers to access a list item stored at a particular dictionary key. Think of this as “index-chaining” and read from right to left: “…the last item of the list associated with Occupations…”.
* **Python classes:**
 * Python uses class to create objects. Every defined class has a special method called `__init__()`, which allows you to control how objects are initialized. Methods within your class are defined in much the same way as functions, that is, using **def**.
 * `class Athlete:
        def __init__(self):`  
 * To create a new class: `a = Athlete()`
 When Python processes this line of code, it turns the factory function call into the following call, which identifies the class, the method (which is automatically  set to __init__()), and the object instance being operated on: `Athlete().__init__(a)`
 * **self** needs to be the first argument to every object method you write.  
 `d.how_big() >> Athlete.how_big(d)`
 * In order to inherite from another class: `class Athlete(superClass):`
 * Every attribute in a class must be prefixed with `self.` in order to associate it data with its instance.
* `dir(objectName)`: show all the attributes of the object
* Python supports multiple inheritance
* If you save your AthleteList class to a file called athletelist.py, you can import the into your code using this line of code: `from athletelist import AthleteList` 
 
 
## Chapter 7: web development
* This dynamic content generation process has been standardized since the early days of the Web and is known
  as the **Common Gateway Interface (CGI)**. Programs that conform to the standard are often referred to as CGI scripts. 
* `from string import Template`: Import the “Template” class from the standard library’s “string” module. This allows for simple string-substitution templates. 
* **The Common Gateway Interface (CGI)** is an Internet standard that allows for a web server to run a server-side program, known as a CGI script.
* `import glob` : The **glob** module lets you query your operating system for a list of file names.


**Bookmark Head First Python:** page 244 (chapter 7)
