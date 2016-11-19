from multiprocessing import Process

def hello(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=hello, args=('bob',))
    p.start()
    p.join()