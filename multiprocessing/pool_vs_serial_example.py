from multiprocessing import Pool
import time
import os
import cProfile

def calculate(n):
    #print('START pid', os.getpid(), 'working on n=', n)
    sum = 0
    for x in range(100000):
        sum += x * x
    #print('END pid', os.getpid(), 'working on n=', n)
    return sum

def go():
    t1 = time.time()
    p = Pool() #it uses the number of cores by default
    result = p.map(calculate, range(100))
    p.close()
    p.join()
    print("Pool took", time.time() - t1)

    t2 = time.time()
    result = []
    for x in range(100):
        result.append(calculate(x))
    print("Serial programming took", time.time() - t2)

if __name__ == "__main__":
    cProfile.run('go()', 'profiling_data.cprof')
    #go()

