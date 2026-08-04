---
nav_order: 0
lauyout: home
title: Python Coding
has_children: true
has_toc: false
---

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


## Standard class flow

* constructor
* initializer
* destructor

***Constructor***: Is the first method a class instantiation will go through.  Once the constructor ran, it's now an object
of the class (taking memory space).  

```python
class YourClassName:
    def __new__(cls, *args, **kwargs):
        ...
```

***Initializer***: Some programing language such as Python will run the initialization method to 
initialize the class.  Note that the initiator will be invoked each time a class is called -- ```YourClassName()```. 
For special case such as singleton class, you will need to check for initialization state.

```python
class YourClassName:
    def __init__(self):
        ...
```

***Destructor***: This is the last method your class would invoke.  Usually, this is not implemented by users.  This method
can be used to ensure your class exit cleanly such as closing all open handles -- file, network, etc.

```python
class YourClassName:
    def __del__(self):
        ...
```

