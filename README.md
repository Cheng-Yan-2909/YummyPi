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
my_data = """
def get_data():
  return my_data

... # do something

print(f"my data: {get_data()}")
```
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






