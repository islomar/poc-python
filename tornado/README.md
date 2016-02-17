#Tornado
Playground for learning about the (Tornado web framework)[http://www.tornadoweb.org/en/stable/].


##Links
* (GitHub source code)[https://github.com/tornadoweb/tornado]


##Instructions
* Automatic installation:
`pip install tornado`


##What Tornado is about
Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed. By using non-blocking network I/O, Tornado can scale to tens of thousands of open connections, making it ideal for long polling, WebSockets, and other applications that require a long-lived connection to each user.

The Tornado web framework and HTTP server together offer a full-stack alternative to WSGI. While it is possible to use the Tornado web framework in a WSGI container (WSGIAdapter), or use the Tornado HTTP server as a container for other WSGI frameworks (WSGIContainer), each of these combinations has limitations and to take full advantage of Tornado you will need to use the Tornado’s web framework and HTTP server together.


##Asynchronous and non-Blocking I/O
Real-time web features require a long-lived mostly-idle connection per user. In a traditional synchronous web server, this implies devoting one thread to each user, which can be very expensive.

To minimize the cost of concurrent connections, Tornado uses a **single-threaded event loop**. This means that **all application code should aim to be asynchronous and non-blocking because only one operation can be active at a time**.

There are many styles of asynchronous interfaces:
* Callback argument
* Return a placeholder (Future, Promise, Deferred)
* Deliver to a queue
* Callback registry (e.g. POSIX signals)

##Ideas for Alea
* Everything async.
* Use of (Futures)[http://www.tornadoweb.org/en/stable/guide/async.html].