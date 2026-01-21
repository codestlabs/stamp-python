# Utilities API Reference

Utility classes for type checking, calculations, and more.

## Import

```python
from stamp.main import Type, Frozen, _calc, Debug, Royal, Alias
```

## Type Class

Type conversion and checking utilities.

### Type.constant(value)
Convert value to constant (immutable).

**Parameters:**
- `value`: Any value to convert

**Returns:** Immutable version of value

```python
from stamp.main import Type

# Create constant
const = Type.constant([1, 2, 3])
# Returns immutable list

# Attempting to modify will raise error
```

### Type.list(value)
Convert value to list.

**Parameters:**
- `value`: Any value to convert

**Returns:** List representation

```python
from stamp.main import Type

# Convert to list
result = Type.list("hello")
# Returns: ['h', 'e', 'l', 'l', 'o']

result = Type.list(123)
# Returns: [1, 2, 3]

result = Type.list((1, 2, 3))
# Returns: [1, 2, 3]
```

### Type.type(value)
Get type of value as string.

**Parameters:**
- `value`: Any value

**Returns:** str - Type name

```python
from stamp.main import Type

print(Type.type(123))      # int
print(Type.type("hello"))  # str
print(Type.type([1,2,3])) # list
print(Type.type({"a":1}))  # dict
```

### Type.flt(value)
Convert to float.

**Parameters:**
- `value`: Value to convert

**Returns:** float

```python
from stamp.main import Type

result = Type.flt("123.45")
print(result)  # 123.45

result = Type.flt(123)
print(result)  # 123.0
```

### Type.btype(value)
Get basic type (str, int, float, bool, list, dict, tuple, set).

**Parameters:**
- `value`: Any value

**Returns:** str - Basic type name

```python
from stamp.main import Type

print(Type.btype(123))         # int
print(Type.btype("hello"))     # str
print(Type.btype([1,2,3]))    # list
print(Type.btype(True))        # bool
```

## Frozen Class

Immutable data structures.

### Frozen.__init__(data)
Create frozen (immutable) data structure.

**Parameters:**
- `data`: Data to freeze

```python
from stamp.main import Frozen

# Create frozen list
frozen_list = Frozen([1, 2, 3])

# Create frozen dict
frozen_dict = Frozen({"a": 1, "b": 2})

# Create frozen tuple
frozen_tuple = Frozen((1, 2, 3))
```

### Frozen.frozenc(*args)
Create frozen collection.

**Parameters:**
- `*args`: Items to freeze

**Returns:** Frozen collection

```python
from stamp.main import Frozen

# Freeze multiple items
frozen = Frozen.frozenc(1, 2, 3, 4, 5)
# Returns frozen collection with 1,2,3,4,5
```

### Frozen.frozenq(*args)
Create frozen collection with query support.

**Parameters:**
- `*args`: Items to freeze

**Returns:** Frozen collection with query methods

```python
from stamp.main import Frozen

# Create queryable frozen collection
frozen = Frozen.frozenq(1, 2, 3, 4, 5)

# Query methods available
# frozen.contains(3)  # True
# frozen.count()       # 5
```

## Royal Class

Royal data structures (special-purpose).

### Royal.royal(data)
Create royal data structure.

**Parameters:**
- `data`: Data to make royal

**Returns:** Royal data structure

```python
from stamp.main import Royal

# Create royal structure
royal = Royal.royal([1, 2, 3, 4, 5])
```

### Royal.royalc(*args)
Create royal collection.

**Parameters:**
- `*args`: Items to make royal

**Returns:** Royal collection

```python
from stamp.main import Royal

royal = Royal.royalc(1, 2, 3, 4, 5)
```

### Royal.royalq(*args)
Create royal collection with query support.

**Parameters:**
- `*args`: Items to make royal

**Returns:** Royal collection with query methods

```python
from stamp.main import Royal

royal = Royal.royalq(1, 2, 3, 4, 5)
```

## _calc Class

Custom calculations and operations.

### _calc._calc(expression)
Evaluate mathematical expression.

**Parameters:**
- `expression` (str): Mathematical expression

**Returns:** Result of calculation

```python
from stamp.main import _calc

# Basic math
result = _calc._calc("2 + 2")
print(result)  # 4

result = _calc._calc("10 * 5")
print(result)  # 50

result = _calc._calc("(2 + 3) * 4")
print(result)  # 20
```

### _calc.add(a, b)
Add two numbers.

**Parameters:**
- `a` (int/float): First number
- `b` (int/float): Second number

**Returns:** Sum of a and b

```python
from stamp.main import _calc

result = _calc.add(5, 3)
print(result)  # 8
```

### _calc.subtract(a, b)
Subtract b from a.

**Parameters:**
- `a` (int/float): First number
- `b` (int/float): Second number

**Returns:** Difference of a and b

```python
from stamp.main import _calc

result = _calc.subtract(10, 3)
print(result)  # 7
```

### _calc.multiply(a, b)
Multiply two numbers.

**Parameters:**
- `a` (int/float): First number
- `b` (int/float): Second number

**Returns:** Product of a and b

```python
from stamp.main import _calc

result = _calc.multiply(5, 4)
print(result)  # 20
```

### _calc.divide(a, b)
Divide a by b.

**Parameters:**
- `a` (int/float): First number
- `b` (int/float): Second number

**Returns:** Quotient of a and b

```python
from stamp.main import _calc

result = _calc.divide(20, 4)
print(result)  # 5.0
```

### _calc.modulo(a, b)
Get remainder of a divided by b.

**Parameters:**
- `a` (int/float): First number
- `b` (int/float): Second number

**Returns:** Remainder

```python
from stamp.main import _calc

result = _calc.modulo(10, 3)
print(result)  # 1
```

### _calc.power(a, b)
Raise a to the power of b.

**Parameters:**
- `a` (int/float): Base
- `b` (int/float): Exponent

**Returns:** a raised to power of b

```python
from stamp.main import _calc

result = _calc.power(2, 8)
print(result)  # 256

result = _calc.power(10, 3)
print(result)  # 1000
```

### _calc.sqrt(a)
Get square root of a.

**Parameters:**
- `a` (int/float): Number

**Returns:** Square root

```python
from stamp.main import _calc

result = _calc.sqrt(16)
print(result)  # 4.0

result = _calc.sqrt(25)
print(result)  # 5.0
```

## Alias Class

Create and manage aliases.

### Alias._new(alias_name, target)
Create new alias.

**Parameters:**
- `alias_name` (str): Name for alias
- `target`: Target object/function to alias

**Returns:** Alias

```python
from stamp.main import Alias

# Create alias
my_print = Alias._new("my_print", print)

# Use alias
my_print("Hello, World!")
```

### Alias._export(alias_name, export_file)
Export alias to file.

**Parameters:**
- `alias_name` (str): Name of alias
- `export_file` (str): File path

```python
from stamp.main import Alias

# Export alias
Alias._export("my_print", "aliases.txt")
```

## Debug Class

Debugging utilities (see [Core API - Debug](core.md#debug)).

## Unite Class

Unite multiple values.

### Unite.unite(*args)
Unite multiple values into one.

**Parameters:**
- `*args`: Values to unite

**Returns:** United value

```python
from stamp.main import Unite

# Unite strings
result = Unite.unite("Hello", " ", "World")
print(result)  # Hello World

# Unite lists
result = Unite.unite([1, 2], [3, 4])
print(result)  # [1, 2, 3, 4]
```

## Kit Class

Tool kit for common operations.

### Kit.kit(*args)
Apply kit operation to args.

**Parameters:**
- `*args`: Arguments to process

**Returns:** Processed result

```python
from stamp.main import Kit

# Use kit
result = Kit.kit("hello", "world")
print(result)
```

## Abombination Class

Special-purpose data structure.

### Abombination.abomb(*args)
Create abombination structure.

**Parameters:**
- `*args`: Items to include

**Returns:** Abombination structure

```python
from stamp.main import Abombination

result = Abombination.abomb(1, 2, 3, 4, 5)
```

## _count_ds Class

Count data structures.

### _count_ds._count_ds(data)
Count elements in data structure.

**Parameters:**
- `data`: Data structure to count

**Returns:** int - Count of elements

```python
from stamp.main import _count_ds

count = _count_ds._count_ds([1, 2, 3, 4, 5])
print(count)  # 5

count = _count_ds._count_ds("hello")
print(count)  # 5
```

## _count_subds Class

Count sub-data structures.

### _count_subds._count_subds(data)
Count nested data structures.

**Parameters:**
- `data`: Data structure with sub-structures

**Returns:** int - Count of all elements including nested

```python
from stamp.main import _count_subds

data = [1, 2, [3, 4], {"a": 5}]
count = _count_subds._count_subds(data)
print(count)  # 7 (including nested elements)
```

## _dynvar Class

Dynamic variable management.

### _dynvar._dynvar(name, value=None)
Create or get dynamic variable.

**Parameters:**
- `name` (str): Variable name
- `value`: Value to set (optional)

**Returns:** Dynamic variable

```python
from stamp.main import _dynvar

# Set dynamic variable
_dynvar._dynvar("my_var", 42)

# Get dynamic variable
value = _dynvar._dynvar("my_var")
print(value)  # 42
```

## _link Class

Create links between objects.

### _link._link(obj1, obj2)
Create link between two objects.

**Parameters:**
- `obj1`: First object
- `obj2`: Second object

**Returns:** Link object

```python
from stamp.main import _link

# Create link
link = _link._link(obj1, obj2)
```

## strint Class

String-integer conversion utilities.

### strint.strint(value)
Convert between string and integer.

**Parameters:**
- `value`: Value to convert

**Returns:** Converted value

```python
from stamp.main import strint

# String to int
result = strint.strint("123")
print(result)  # 123

# Int to string
result = strint.strint(123)
print(result)  # "123"
```

### strint.intstr(value)
Alias for strint().

```python
from stamp.main import strint

result = strint.intstr("456")
print(result)  # 456
```

## join3 and rj3

String joining utilities.

### join3.join3(s1, s2, s3, separator="")
Join three strings.

**Parameters:**
- `s1` (str): First string
- `s2` (str): Second string
- `s3` (str): Third string
- `separator` (str): Separator (default: "")

**Returns:** Joined string

```python
from stamp.main import join3

result = join3.join3("Hello", "World", "!", " ")
print(result)  # Hello World !
```

### rj3.rj3(s1, s2, s3, separator="")
Reverse join three strings.

**Parameters:**
- `s1` (str): First string
- `s2` (str): Second string
- `s3` (str): Third string
- `separator` (str): Separator (default: "")

**Returns:** Reversed joined string

```python
from stamp.main import rj3

result = rj3.rj3("Hello", "World", "!", " ")
print(result)  # ! World Hello
```

## Usage Examples

### Type Conversion

```python
from stamp.main import Type

# Check types
print(Type.type(123))      # int
print(Type.btype("hello")) # str

# Convert types
lst = Type.list("hello")
flt = Type.flt("123.45")
```

### Calculations

```python
from stamp.main import _calc

# Evaluate expression
result = _calc._calc("(2 + 3) * 4")
print(result)  # 20

# Use methods
result = _calc.add(5, 3)
print(result)  # 8
```

### Frozen Data

```python
from stamp.main import Frozen

# Create frozen list
frozen = Frozen([1, 2, 3])
# Immutable - cannot modify
```

### Aliases

```python
from stamp.main import Alias

# Create alias
my_func = Alias._new("my_func", print)
my_func("Hello!")
```

---

See [Core API](core.md) for main module documentation.
See [Advanced Examples](../examples/advanced.md) for more usage examples.
