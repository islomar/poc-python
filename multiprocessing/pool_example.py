from multiprocessing import Pool
import os

def f(x):
    print('pid', os.getpid())
    print('working on x=', x)
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))