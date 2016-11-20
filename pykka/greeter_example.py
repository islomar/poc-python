import pykka
import os

class Greeter(pykka.ThreadingActor):
    def __init__(self, greeting='Hi there!'):
        super(Greeter, self).__init__()
        self.greeting = greeting

    def on_receive(self, message):
        print('Process executing this actor:', os.getpid())
        print('Sleeping...')
        #sleep(.1)
        print('Awakening...')
        print('Message received:', message)
        print(self.greeting)
        
if __name__ == '__main__':
    print('main executing from pid:', os.getpid())
    actor_ref_1 = Greeter.start(greeting='Hi you!')
    actor_ref_2 = Greeter.start(greeting='Hi you!')

    actor_ref_1.tell({'msg': 'Hi1!'})
    actor_ref_2.tell({'msg': 'Hi2!'})
    # => Returns nothing. Will never block.

    #answer = actor_ref.ask({'msg': 'Hi?'})
    # => May block forever waiting for an answer

    #answer = actor_ref.ask({'msg': 'Hi?'}, timeout=3)
    # => May wait 3s for an answer, then raises exception if no answer.

    #future = actor_ref.ask({'msg': 'Hi?'}, block=False)
    # => Will return a future object immediately.
    #answer = future.get()
    # => May block forever waiting for an answer
    #answer = future.get(timeout=0.1)
    # => May wait 0.1s for an answer, then raises exception if no answer.