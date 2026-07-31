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

The ***primitive*** data type are fixed in memory size: int, float, char, byte, ... and now included str (a collection of char)

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

## Default Values

Be careful with default values where the values are not primitive data type.  When you have a simple default value such as:
```python
class MyTest:
    data = {}

```

The value of ```data``` is a pointer to an address of a ```dict``` data type.   This address is fixed, such that all
instances will be using the same address -- working with the same data.

To test this out, try the below code
```python
class DefaultVal:
    default_val = {}


my_data1 = DefaultVal()
my_data2 = DefaultVal()
my_data3 = DefaultVal()
print(f"my_data1: {id(my_data1.default_val)}")
print(f"my_data2: {id(my_data2.default_val)}")
print(f"my_data3: {id(my_data3.default_val)}")
```
You will get the below output:
```text
my_data1: 4312677952
my_data2: 4312677952
my_data3: 4312677952
```
The integer shown is the address to the memory location where the data resides.

<hr/>

Another default value to be careful on is method arguments.

```python
import time
def some_method(now=time.time()):
    ...
```

Here, the default value of the argument ```now``` is **NOT** the actual current time.  The value is the time this method is loaded
into memory -- a fixed value.  Run this test to see:
```python
def test_default_arg_value(now=time.time()):
    print(f"now is: {now}")

test_default_arg_value()
test_default_arg_value()
test_default_arg_value()
```

You will something like this.  The floating point value are the number of milli-seconds since epoch.
```text
now is: 1785540379.5673559
now is: 1785540379.5673559
now is: 1785540379.5673559
```

Another test of default value:
```python
def test_default_arg_value2(data={}):
    print(f"data is @: {id(data)}")

test_default_arg_value2()
test_default_arg_value2()
test_default_arg_value2()
```

default value with same address location for the argument.
```text
data is @: 4373051648
data is @: 4373051648
data is @: 4373051648
```

# Arguments - passing by value or address

Python shares this with Java where primitive data type are passed by value and objects are passed by address.
Below test shows the difference between primitive data type passing and object data type passing.

```python
def test_argument(primitive_type, object_type):
    print("inside of 'test_argument' method")
    print(f" - primitive_type value: {primitive_type}")
    print(f" - object_type value: {object_type}")
    print("changing both values")
    primitive_type += 1
    object_type.append("efgh")
    print("after data changed")
    print(f" - primitive_type value: {primitive_type}")
    print(f" - object_type value: {object_type}")

print("=============================================")
primitive_data = 3
object_data = ["abcd"]
test_argument(primitive_data, object_data)
print("after the function call to 'test_argument'")
print(f" - primitive_data: {primitive_data}")
print(f" - object_data: {object_data}")
```

The variable ```primitive_data``` and ```object_data``` are defined outside of the ```test_argument``` method call.
The ```test_argument``` method modifies the method argument value.  

```text
inside of 'test_argument' method
 - primitive_type value: 3
 - object_type value: ['abcd']
changing both values
after data changed
 - primitive_type value: 4
 - object_type value: ['abcd', 'efgh']
after the function call to 'test_argument'
 - primitive_data: 3
 - object_data: ['abcd', 'efgh']
```

The sample output shows that operating on primitive values, only the values got changed, which stays within the scape of the method.
But for object type data modification, the value are changed at the address location where the argument was passed in. 
Therefore, the modification of the value from ```object_data``` changes the original data.

## Dunder method

Python has set of method called **dunder** methods.  These are build in method that can be override.  Most frequent used is the ```__init__()``` method.   Note that this method only initialize the class after creation, not controlling the creation of the class.  To overwrite the creation you will need to override ```__new__()```

```python
d = {}
for name in dir(d):
  print(f"{name} ==> {getattr(d, name, '')}")
```

You can use dunder methods to define your own class's functionality.
ex:

```python
class MyData:
    """
        class doc... describe the class here
    """

    data: dict = None

    def __init__(self, *, data=None):
        if data is None:
            self.data = {}
        else:
            self.data = data

    def add_data(self, *, key, value):
        self.data[key] = value

    def __setitem__(self, key, value):
        self.add_data(key=key, value=value)

    def __getitem__(self, item):
        if item in self.data:
            return self.data[item]
        return None

    
my_data = MyData()
my_data["test"] = "works"

print(f"my_data.data: {my_data.data}")
```

the above test will show this:

```text
my_data.data: {'test': 'works'}
```



