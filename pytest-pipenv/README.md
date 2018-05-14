# Sandbox for trying pytest and pipenv

## pytest
* https://docs.pytest.org
* https://docs.pytest.org/en/latest/goodpractices.html#test-discovery
* Changing standard (Python) test discovery: https://docs.pytest.org/en/latest/example/pythoncollection.html
* `pytest`: run all the tests
* `pytest -q test_sysexit.py`: run with quiet mode
* The method test must start with "test" (I guess/hope it can be changed)


## mock
* https://docs.python.org/dev/library/unittest.mock.html
* Mock and MagicMock objects create all attributes and methods as you access them and store details of how they have been used.
* MagicMock is a subclass of Mock with all the magic methods pre-created and ready to use.
* `side_effect` allows you to perform side effects, including raising an exception when a mock is called
* The `patch()` decorator / context manager makes it easy to mock classes or objects in a module under test. The object you specify will be replaced with a mock (or other object) during the test and restored when the test ends
* By default patch() will create a MagicMock for you. You can specify an alternative class of Mock using the new_callable argument to patch().
* For ensuring that the mock objects in your tests have the same api as the objects they are replacing, you can use auto-speccing.
    * create_autospec() can also be used on classes, where it copies the signature of the __init__ method, and on callable objects where it copies the signature of the __call__ method.

## pipenv
https://github.com/pypa/pipenv

`sudo apt-get install python3-distutils`

* `pipenv --python 3.6`
* `pipenv shell`: activate the project
* Type `exit`or Ctl-D to exit the environment
* `pipenv install -e .`:  Install a local setup.py into your virtual environment/Pipfile
* `pipenv --where`: locate the project
* `pipenv --py`: locate the python interpreter
* `pipenv install`: install packages
* `pipenv install pytest --dev`: install a dev dependency
* `pipenv lock`: generate a lock file
* `pipenv uninstall --all`: uninstall all dependencies
* `pipenv shell`: use the shell
* `pipenv check`: Check your installed dependencies for security vulnerabilities
* `pipenv run python xxxx.py`: Executing code without activating your virtual environment