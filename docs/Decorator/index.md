---
layout: page
nav_order: 40
title: Decorator
permalink: /Decorator/
has_children: false
---


# Decorator

A decorator is a shorthand for wrapping a method in another method.  You will use this use alot in Python frameworks -- gaming,
tests, web app, etc.

## Intro

ex:
```python
decorated_method = []
def my_decorator(func):
    print(f"wrapping func: {func.__name__}")
    decorated_method.append(func)
    return func

def _my_func():
    print("I am my_func")

my_func = my_decorator( _my_func )

print("Calling 'my_func' -- ", end="")
my_func()
for func in decorated_method:
    print("Calling from 'decorated_method' list: ", end="")
    func()
```

You will get an output like:
```text
wrapping func: _my_func
Calling 'my_func' -- I am my_func
Calling from 'decorated_method' list: I am my_func
```

The above sample, the method ```my_decorator``` takes a function point and add them to the list of ```decorated_method``` then return the
method it wraps.

the wrapped method ```_my_func``` can be invoked from the variable name ```my_func``` or from the ```decorated_method``` list.

## The Shorthand

The shorthand is prefix the function wrapper with ```@```, then follow by the definition of the method.

```python
decorated_method = []
def my_decorator(func):
    print(f"wrapping func: {func.__name__}")
    decorated_method.append(func)
    return func

@my_decorator
def my_func():
    print("I am my_func")

print("Calling 'my_func' -- ", end="")
my_func()
for func in decorated_method:
    print("Calling from 'decorated_method' list: ", end="")
    func()
```

```text
wrapping func: my_func
Calling 'my_func' -- I am my_func
Calling from 'decorated_method' list: I am my_func
```

Note that in Python a method is also an object that can be modified at run time.  A decorator usually add/modify attribute
on the method.  Such as flag the method as part of the framework implementation, etc.

ex:
```python
def my_decorator(func):
    print(f"wrapping func: {func.__name__}")
    setattr(func, "is_my_method", True)
    return func

@my_decorator
def my_func():
    print("I am my_func")
```
