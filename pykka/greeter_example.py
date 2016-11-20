import pykka

class Greeter(pykka.ThreadingActor):
    def __init__(self, greeting='Hi there!'):
        super(Greeter, self).__init__()
        self.greeting = greeting

    def on_receive(self, message):
        print('Message received:', message)
        print(self.greeting)
        

actor_ref = Greeter.start(greeting='Hi you!')

actor_ref.tell({'msg': 'Hi!'})
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