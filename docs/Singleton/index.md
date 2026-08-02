---
layout: page
nav_order: 30
title: Singleton
permalink: /Singleton/
has_children: false
---


# Singleton

A singleton class is a class that has only one instance throughout the application's lifetime.

```python

class SingletonClass:
    _singleton_instance_name_ = "_singleton_instance_name_"

    def __new__(cls, *args, **kwargs):
        try:
            instance_name = f"{SingletonClass._singleton_instance_name_}_{cls.__module__}_{cls.__name__}"
        except:
            instance_name = f"{SingletonClass._singleton_instance_name_}_{cls.__name__}"

        singleton_instance = getattr(cls, instance_name, None)

        if singleton_instance is None:
            singleton_instance = super(SingletonClass, cls).__new__(cls)
            setattr(cls, instance_name, singleton_instance)

        return singleton_instance

class TestSingleton1(SingletonClass): pass

class TestSingleton2(SingletonClass): pass


print(f"Singleton instance 1 id: {id(TestSingleton1())}")
print(f"Singleton instance 1 id: {id(TestSingleton1())}")
print(f"Singleton instance 1 id: {id(TestSingleton1())}")
print(f"Singleton instance 2 id: {id(TestSingleton2())}")
print(f"Singleton instance 2 id: {id(TestSingleton2())}")
print(f"Singleton instance 2 id: {id(TestSingleton2())}")

```

the test

```text
Singleton instance 1 id: 4304408160
Singleton instance 1 id: 4304408160
Singleton instance 1 id: 4304408160
Singleton instance 2 id: 4304408256
Singleton instance 2 id: 4304408256
Singleton instance 2 id: 4304408256
```


