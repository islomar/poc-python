# Sandbox for trying pytest and pipenv

## pytest
TBD

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