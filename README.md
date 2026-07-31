# Coding in General

## All related code are to be placed into one ***group*** 
***group*** can be defined as file, class, function.

## Create function rather than directly access the data

❌ 
```python
my_data = "a test"
...  # do something
print(f"my data: {my_data}")
```

✅ 
```python
my_data = ""
def get_data():
  return my_data

... # do something

print(f"my data: {get_data()}")
```
This way, you are free to modify the function ```get_data``` and no other code changes needed.

<hr/>

## No global variable

❌ 
```python
some_config_flag_enabled = True
...  # do something
def update_some_config_flag():
  some_config_flag_enabled = False
```

✅ 
```python
class SomeConfig:
  some_config_flag_enabled = True
...  # do something
def update_some_config_flag():
  SomeConfig.some_config_flag_enabled = False
```

Global variable causes confusion and data conflict. Confusion:
* when variable not exists, you cannot access it, it will crash
* when creating a local variable with the same name as global variable, reading and writing can be confusing
* cannot access global variable without ```global``` keyword.

<hr>

# Python - General

Python keeps some of the low level programing language features.  It has two sets of data types:
* primitive
* object

The ***primitive*** data type are fixed in memory size: int, float, char, byte, ... and now included str (a collection of char), dict, list, tuple (read-only list)

Everything else is ***object***, including the class itself and methods.  You can access all members of the object using:

dump attributes for method:
```python
def my_func():
  print("test")
for name in dir(my_func):
  print(f"{name} ==> {getattr(my_func, name, '')}")
```

dump attributes for dict
```python
d = {}
for name in dir(d):
  print(f"{name} ==> {getattr(d, name, '')}")
```

Noticed, ```getattr``` is a building in method that can get the object's attribute value.  There's also ```setattr``` to set attribute value.

## Dunder method

Python has set of method called **dunder** methods.  These are build in method that can be override.  Most frequent used is the ```__init__()``` method.   Note that this method only initialize the class after creation, not controlling the creation of the class.  To overwrite the creation you will need to override ```__new__()```

```python
d = {}
for name in dir(d):
  print(f"{name} ==> {getattr(d, name, '')}")
```



