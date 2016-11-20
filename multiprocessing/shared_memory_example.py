# please, DO NOT fucking do this!! (do not share!)
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

# Data can be stored in a shared memory map using Value or Array.
if __name__ == '__main__':
    num = Value('d', 0.0) #d means 'double'
    arr = Array('i', range(10)) #i means 'integer'

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])