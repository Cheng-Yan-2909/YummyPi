---
layout: page
nav_order: 10
parent: Dunder Methods
title: dunder list
permalink: /Dunder/the-list
has_children: false
---

### Object Initialization and Cleanup
* __new__(cls, ...): Handles object creation.
* __init__(self, ...): Handles object initialization.
* __del__(self): Handles object destruction or cleanup.

### String and Representation
* __str__(self): Defines user-friendly string output via str(obj) or print(obj).
* __repr__(self): Defines unambiguous developer-focused string output via repr(obj) or debugging tools.
* __format__(self, format_spec): Customizes behavior for format(obj) or f-string formatting.
* __bytes__(self): Evaluates a byte-string representation via bytes(obj).

### Comparison Operators
* __eq__(self, other): Implements the equality operator ==.
* __ne__(self, other): Implements the inequality operator !=.
* __lt__(self, other): Implements the less-than operator <.
* __le__(self, other): Implements the less-than-or-equal-to operator <=.
* __gt__(self, other): Implements the greater-than operator >.
* __ge__(self, other): Implements the greater-than-or-equal-to operator >=.
* __hash__(self): Calculates a unique integer hash via hash(obj) for dictionary keys and sets.

### Standard Arithmetic Operators__add__(self, other): Overloads addition +.
* __sub__(self, other): Overloads subtraction -.
* __mul__(self, other): Overloads multiplication *.
* __truediv__(self, other): Overloads true division /.
* __floordiv__(self, other): Overloads floor division //.
* __mod__(self, other): Overloads the modulus operator %.
* __pow__(self, other): Overloads exponentiation **.
* __matmul__(self, other): Overloads matrix multiplication @.

### Reflected/Right-Hand Arithmetic
(Invoked if the left-hand operand does not support the operation but the right-hand operand does)
* __radd__(self, other): Right-hand addition.
* __rsub__(self, other): Right-hand subtraction.
* __rmul__(self, other): Right-hand multiplication.
* __rtruediv__(self, other): Right-hand true division.

### In-Place Arithmetic Assignment
* __iadd__(self, other): Implements in-place addition +=.
* __isub__(self, other): Implements in-place subtraction -=.
* __imul__(self, other): Implements in-place multiplication *=.
* __itruediv__(self, other): Implements in-place division /=.

### Type Conversions and Math
* __int__(self): Converts an object to an integer via int(obj).
* __float__(self): Converts an object to a float via float(obj).
* __bool__(self): Evaluates truthiness via bool(obj).
* __abs__(self): Returns the absolute value via abs(obj).
* __round__(self, n): Controls rounding via round(obj, n).

### Containers and Sequences
* __len__(self): Returns collection length via len(obj).
* __getitem__(self, key): Retrieves an item by index or key using obj[key].
* __setitem__(self, key, value): Sets an item using obj[key] = value.
* __delitem__(self, key): Deletes an item using del obj[key].
* __contains__(self, item): Checks membership using item in obj.

### Iterators and Generators
* __iter__(self): Returns an iterator instance using iter(obj) or a for loop.
* __next__(self): Retrieves the next item from an iterator using next(obj).
* __reversed__(self): Customizes sequence reversal via reversed(obj).

### Attribute Access control
* __getattr__(self, name): Intercepts undefined attributes when accessed via obj.name.
* __getattribute__(self, name): Intercepts all attribute access regardless of whether they exist.
* __setattr__(self, name, value): Intercepts attribute assignment obj.name = value.
* __delattr__(self, name): Intercepts attribute deletion del obj.name.
* __dir__(self): Customizes the list of attributes returned by dir(obj).

### Context Managers and Callables
* __enter__(self): Runs setup behavior when entering a with statement block.
* __exit__(self, exc_type, exc_val, exc_tb): Runs teardown or error-handling when exiting a with block.
* __call__(self, *args, **kwargs): Allows instances to be called like functions using obj().




