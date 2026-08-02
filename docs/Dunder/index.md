---
layout: page
nav_order: 10
title: Dunder Methods
permalink: /Dunder/
has_children: true
---


# Dunder method

Python has set of method called **dunder** methods.  These are build in method that can be override.  Most frequent used is the ```__init__()``` method.   Note that this method only initialize the class after creation, not controlling the creation of the class.  To overwrite the creation you will need to override ```__new__()```

```python
d = {}
for name in dir(d):
  print(f"{name} ==> {getattr(d, name, '')}")
```

You can use dunder methods to define your own class's functionality.
ex:

```python
class Jobs:
    """
        class doc... describe the class here
    """

    available_jobs = [
        "teacher", "principal", "administrator"
    ]

    teacher = None
    principal = None
    administrator = None


    def add_data(self, *, key, value):
        if not key in self.available_jobs:
            return
        setattr(self, key, value)

    def __setitem__(self, key, value):
        self.add_data(key=key, value=value)

    def __getitem__(self, item):
        if item in self.available_jobs:
            return getattr(self, item)
        return None

    def __str__(self):
        s = ""
        for job in self.available_jobs:
            s = f"{s}, {job}={getattr(self, job)}"
        return s
    

job = Jobs()
job["test"] = "testing job"
job["teacher"] = "science"
job["principal"] = "Bob"
print(f"job of 'teacher': {job['teacher']}")
print(f"my_job: {job}")
```

The above demonstrate the use of dunder methods to implement **getter** and **setter** to allow accessing data via keys 
-- similar to dictionary.  The end of the class also define its string representation.
It shows this:

```text
job of 'teacher': science
my_job: , teacher=science, principal=Bob, administrator=None
```


