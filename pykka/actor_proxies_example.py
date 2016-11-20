import pykka

class Calculator(pykka.ThreadingActor):
    def __init__(self):
        super(Calculator, self).__init__()
        self.last_result = None

    def add(self, a, b=None):
        if b is not None:
            self.last_result = a + b
        else:
            self.last_result += a
        return self.last_result

    def sub(self, a, b=None):
        if b is not None:
            self.last_result = a - b
        else:
            self.last_result -= a
        return self.last_result

if __name__ == '__main__':
    actor_ref = Calculator.start()

    proxy = actor_ref.proxy()

    future = proxy.add(1, 3)

    #All results are wrapped in “future” objects, so you must use the get() method to get the actual data
    result = future.get()
    print('result', result)

    proxy.sub(5)
    proxy.add(3)
    proxy.last_result.get()