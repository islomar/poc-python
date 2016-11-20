from multiprocessing import Pool
import os

def f(x):
    print('pid', os.getpid())
    print('working on x=', x)
    #print(os.environ['REDIS_DB_URI'])
    return x*x

# Passing an environment variable works just fine
# REDIS_DB_URI='my-redis-uri' python pool_example.py
if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))