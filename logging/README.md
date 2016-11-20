#logging

https://docs.python.org/3/library/logging.html

https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook

##Best practices
https://docs.python.org/3/howto/logging.html

A good convention to use when naming loggers is to use a module-level logger, in each module which uses logging, named as follows:
`logger = logging.getLogger(__name__)`

http://www.robg3d.com/2012/02/python-logging-best-practices/
If you have multiple classes in a file, give them each their own logger. Do not use a single module logger for many classes. 
Identify the logger by the class name so you know what logger produced what log.

import logging
logging.getLogger('simple_example').setLevel(logging.DEBUG)