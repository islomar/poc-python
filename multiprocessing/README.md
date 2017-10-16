# Multiprocessing
Playground for trying the native library `multiprocessing`

## Manual installation
mkvirtualenv --python=/usr/local/bin/python3.5 multiprocessing
workon multiprocessing

## Execution
`python <file_name>`
For time profiling:
`python -m cProfile [-o output_file] [-s sort_order] myscript.py`
E.g.: `python -m cProfile -o multiprocessing_profiling.txt pool_example.py`

## Documentation
https://docs.python.org/3/library/multiprocessing.html

## Interesting videos
* Multiprocessing in Python: https://www.youtube.com/watch?v=s1SkCYMnfbY
* Python Multiprocessing Introduction: https://www.youtube.com/watch?v=Lu5LrKh1Zno
* Multiprocessing vs multithreading: https://www.youtube.com/watch?v=oIN488Ldg9k
* Multiprocessing Pool (Map Reduce): https://www.youtube.com/watch?v=_1ZwkCY9wxk

## Pools
`class multiprocessing.Pool([processes[, initializer[, initargs[, maxtasksperchild]]]])`
`processes` is the number of worker processes to use. If processes is None then the number returned by cpu_count() is used. 

## Communication
* Queue: one way communication
* Pipe: two way communications

## Example with profiling
cProfile and multiprocessing are not good friends... it crashes!
For that reason, you should use it inside your code :-(

In order to analyse the results:
```
import pstats
p = pstats.Stats('profiling_data.cprof')
p.strip_dirs().sort_stats(-1).print_stats()
p.sort_stats('time').print_stats('calculate')
```
