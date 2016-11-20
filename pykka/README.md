#Pykka: actor's model library

##Documentations
https://www.pykka.org/en/latest/


##Examples
https://github.com/jodal/pykka/


##Rules of the actor model
* An actor is an execution unit that executes concurrently with other actors.
* An actor does not share state with anybody else, but it can have its own state.
* An actor can only communicate with other actors by sending and receiving messages. It can only send messages to actors whose address it has.
* When an actor receives a message it may take actions like:
  * altering its own state, e.g. so that it can react differently to a future message,
  * sending messages to other actors, or
  * starting new actors.
  None of the actions are required, and they may be applied in any order.
* An actor only processes one message at a time. In other words, a single actor does not give you any concurrency, and it does not need to use locks internally to protect its own state.


##Pykka features
* Looks like it uses multithreading, not multiprocessing