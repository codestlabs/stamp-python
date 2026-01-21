# Java Emulation API Reference

Java standard library emulation.

## Import

```python
from stamp.java import System, String, Math, ArrayList, HashMap, HashSet, Scanner
```

## Overview

Stamp provides complete Java standard library emulation, allowing Java-like syntax in Python.

## System Class

Java System utilities.

### System.out.println(message)

Print message to console.

**Parameters:**
- `message`: Message to print

```python
from stamp.java import System

System.out.println("Hello, World!")
System.out.println(42)
System.out.println([1, 2, 3])
```

### System.out.print(message)

Print message without newline.

**Parameters:**
- `message`: Message to print

```python
from stamp.java import System

System.out.print("Hello, ")
System.out.print("World!")
# Output: Hello, World!
```

### System.currentTimeMillis()

Get current time in milliseconds.

**Returns:** int - Milliseconds since epoch

```python
from stamp.java import System

ms = System.currentTimeMillis()
print(ms)
# Output: 1726657200000
```

### System.arraycopy(src, src_pos, dest, dest_pos, length)

Copy array elements.

**Parameters:**
- `src` (list): Source array
- `src_pos` (int): Source position
- `dest` (list): Destination array
- `dest_pos` (int): Destination position
- `length` (int): Number of elements to copy

```python
from stamp.java import System

src = [1, 2, 3, 4, 5]
dest = [0, 0, 0, 0, 0]

System.arraycopy(src, 1, dest, 2, 3)
print(dest)
# Output: [0, 0, 2, 3, 4]
```

## String Class

Java String operations.

### String.length()

Get string length.

**Returns:** int - String length

```python
from stamp.java import String

s = String("Hello World")
print(s.length())
# Output: 11
```

### String.charAt(index)

Get character at index.

**Parameters:**
- `index` (int): Character index

**Returns:** str - Character at index

```python
from stamp.java import String

s = String("Hello")
print(s.charAt(0))
# Output: H
print(s.charAt(4))
# Output: o
```

### String.substring(start, end=None)

Get substring.

**Parameters:**
- `start` (int): Start index
- `end` (int): End index (optional, defaults to end of string)

**Returns:** str - Substring

```python
from stamp.java import String

s = String("Hello World")
print(s.substring(0, 5))
# Output: Hello

print(s.substring(6))
# Output: World
```

### String.indexOf(str)

Find substring index.

**Parameters:**
- `str` (str): Substring to find

**Returns:** int - Index of substring (-1 if not found)

```python
from stamp.java import String

s = String("Hello World")
print(s.indexOf("World"))
# Output: 6

print(s.indexOf("xyz"))
# Output: -1
```

### String.toLowerCase()

Convert to lowercase.

**Returns:** str - Lowercase string

```python
from stamp.java import String

s = String("HELLO")
print(s.toLowerCase())
# Output: hello
```

### String.toUpperCase()

Convert to uppercase.

**Returns:** str - Uppercase string

```python
from stamp.java import String

s = String("hello")
print(s.toUpperCase())
# Output: HELLO
```

### String.trim()

Remove leading/trailing whitespace.

**Returns:** str - Trimmed string

```python
from stamp.java import String

s = String("  Hello  ")
print(s.trim())
# Output: Hello
```

### String.replace(old, new)

Replace substring.

**Parameters:**
- `old` (str): Old substring
- `new` (str): New substring

**Returns:** str - String with replacements

```python
from stamp.java import String

s = String("Hello World")
print(s.replace("World", "Python"))
# Output: Hello Python
```

### String.split(regex)

Split string by regex.

**Parameters:**
- `regex` (str): Regular expression

**Returns:** list - Split parts

```python
from stamp.java import String

s = String("a,b,c")
print(s.split(","))
# Output: ['a', 'b', 'c']
```

### String.equals(other)

Check string equality.

**Parameters:**
- `other` (str): String to compare

**Returns:** bool - True if equal

```python
from stamp.java import String

s1 = String("Hello")
s2 = String("Hello")
print(s1.equals(s2))
# Output: True
```

## Math Class

Mathematical operations.

### Math.abs(x)

Absolute value.

**Parameters:**
- `x` (int/float): Number

**Returns:** int/float - Absolute value

```python
from stamp.java import Math

print(Math.abs(-5))
# Output: 5

print(Math.abs(-3.14))
# Output: 3.14
```

### Math.max(a, b)

Maximum of two numbers.

**Parameters:**
- `a` (int/float): First number
- `b` (int/float): Second number

**Returns:** int/float - Maximum

```python
from stamp.java import Math

print(Math.max(5, 10))
# Output: 10
```

### Math.min(a, b)

Minimum of two numbers.

**Parameters:**
- `a` (int/float): First number
- `b` (int/float): Second number

**Returns:** int/float - Minimum

```python
from stamp.java import Math

print(Math.min(5, 10))
# Output: 5
```

### Math.pow(a, b)

Power function.

**Parameters:**
- `a` (int/float): Base
- `b` (int/float): Exponent

**Returns:** float - a raised to power b

```python
from stamp.java import Math

print(Math.pow(2, 8))
# Output: 256.0

print(Math.pow(10, 3))
# Output: 1000.0
```

### Math.sqrt(x)

Square root.

**Parameters:**
- `x` (int/float): Number

**Returns:** float - Square root

```python
from stamp.java import Math

print(Math.sqrt(16))
# Output: 4.0

print(Math.sqrt(25))
# Output: 5.0
```

### Math.round(x)

Round to nearest integer.

**Parameters:**
- `x` (int/float): Number

**Returns:** int - Rounded value

```python
from stamp.java import Math

print(Math.round(3.7))
# Output: 4

print(Math.round(3.2))
# Output: 3
```

### Math.floor(x)

Floor (round down).

**Parameters:**
- `x` (int/float): Number

**Returns:** int - Floor value

```python
from stamp.java import Math

print(Math.floor(3.7))
# Output: 3
```

### Math.ceil(x)

Ceiling (round up).

**Parameters:**
- `x` (int/float): Number

**Returns:** int - Ceiling value

```python
from stamp.java import Math

print(Math.ceil(3.2))
# Output: 4
```

### Math.random()

Random number between 0.0 and 1.0.

**Returns:** float - Random number

```python
from stamp.java import Math

print(Math.random())
# Output: 0.123456...
```

### Math.PI

Pi constant.

```python
from stamp.java import Math

print(Math.PI)
# Output: 3.14159...
```

### Math.E

Euler's number constant.

```python
from stamp.java import Math

print(Math.E)
# Output: 2.71828...
```

## ArrayList Class

Dynamic array (list) operations.

### ArrayList.__init__()

Create empty ArrayList.

```python
from stamp.java import ArrayList

list = ArrayList()
```

### ArrayList.add(item)

Add item to list.

**Parameters:**
- `item`: Item to add

```python
from stamp.java import ArrayList

list = ArrayList()
list.add(1)
list.add(2)
list.add(3)
```

### ArrayList.get(index)

Get item at index.

**Parameters:**
- `index` (int): Index

**Returns:** Item at index

```python
from stamp.java import ArrayList

list = ArrayList()
list.add("Hello")
item = list.get(0)
print(item)
# Output: Hello
```

### ArrayList.remove(index)

Remove item at index.

**Parameters:**
- `index` (int): Index

```python
from stamp.java import ArrayList

list = ArrayList()
list.add(1)
list.add(2)
list.remove(0)
```

### ArrayList.size()

Get list size.

**Returns:** int - List size

```python
from stamp.java import ArrayList

list = ArrayList()
list.add(1)
list.add(2)
list.add(3)
print(list.size())
# Output: 3
```

### ArrayList.contains(item)

Check if list contains item.

**Parameters:**
- `item`: Item to check

**Returns:** bool - True if contains

```python
from stamp.java import ArrayList

list = ArrayList()
list.add(1)
print(list.contains(1))
# Output: True

print(list.contains(2))
# Output: False
```

### ArrayList.clear()

Clear all items.

```python
from stamp.java import ArrayList

list = ArrayList()
list.add(1)
list.add(2)
list.clear()
```

## HashMap Class

Key-value map operations.

### HashMap.__init__()

Create empty HashMap.

```python
from stamp.java import HashMap

map = HashMap()
```

### HashMap.put(key, value)

Put key-value pair.

**Parameters:**
- `key`: Key
- `value`: Value

```python
from stamp.java import HashMap

map = HashMap()
map.put("name", "Alice")
map.put("age", 25)
```

### HashMap.get(key)

Get value by key.

**Parameters:**
- `key`: Key

**Returns:** Value associated with key

```python
from stamp.java import HashMap

map = HashMap()
map.put("name", "Alice")
name = map.get("name")
print(name)
# Output: Alice
```

### HashMap.remove(key)

Remove key-value pair.

**Parameters:**
- `key`: Key

```python
from stamp.java import HashMap

map = HashMap()
map.put("name", "Alice")
map.remove("name")
```

### HashMap.containsKey(key)

Check if key exists.

**Parameters:**
- `key`: Key

**Returns:** bool - True if key exists

```python
from stamp.java import HashMap

map = HashMap()
map.put("name", "Alice")
print(map.containsKey("name"))
# Output: True
```

### HashMap.size()

Get map size.

**Returns:** int - Number of entries

```python
from stamp.java import HashMap

map = HashMap()
map.put("a", 1)
map.put("b", 2)
print(map.size())
# Output: 2
```

### HashMap.clear()

Clear all entries.

```python
from stamp.java import HashMap

map = HashMap()
map.put("a", 1)
map.clear()
```

## HashSet Class

Set operations (unique items).

### HashSet.__init__()

Create empty HashSet.

```python
from stamp.java import HashSet

set = HashSet()
```

### HashSet.add(item)

Add item to set.

**Parameters:**
- `item`: Item to add

```python
from stamp.java import HashSet

set = HashSet()
set.add(1)
set.add(2)
set.add(1)  # Duplicate, won't be added
```

### HashSet.contains(item)

Check if set contains item.

**Parameters:**
- `item`: Item to check

**Returns:** bool - True if contains

```python
from stamp.java import HashSet

set = HashSet()
set.add(1)
print(set.contains(1))
# Output: True
```

### HashSet.remove(item)

Remove item from set.

**Parameters:**
- `item`: Item to remove

```python
from stamp.java import HashSet

set = HashSet()
set.add(1)
set.remove(1)
```

### HashSet.size()

Get set size.

**Returns:** int - Set size

```python
from stamp.java import HashSet

set = HashSet()
set.add(1)
set.add(2)
print(set.size())
# Output: 2
```

### HashSet.clear()

Clear all items.

```python
from stamp.java import HashSet

set = HashSet()
set.add(1)
set.clear()
```

## Scanner Class

Input parsing.

### Scanner.__init__(source)

Create scanner.

**Parameters:**
- `source`: Input source (string or file)

```python
from stamp.java import Scanner

# String scanner
scanner = Scanner("Hello World")

# File scanner
scanner = Scanner(open("file.txt"))
```

### Scanner.next()

Get next token.

**Returns:** str - Next token

```python
from stamp.java import Scanner

scanner = Scanner("Hello World")
word1 = scanner.next()
word2 = scanner.next()
print(word1, word2)
# Output: Hello World
```

### Scanner.nextLine()

Get next line.

**Returns:** str - Next line

```python
from stamp.java import Scanner

scanner = Scanner("Line 1\nLine 2\n")
line1 = scanner.nextLine()
line2 = scanner.nextLine()
print(line1)
# Output: Line 1
```

### Scanner.nextInt()

Get next integer.

**Returns:** int - Next integer

```python
from stamp.java import Scanner

scanner = Scanner("42 100")
num1 = scanner.nextInt()
num2 = scanner.nextInt()
print(num1, num2)
# Output: 42 100
```

### Scanner.hasNext()

Check if more tokens.

**Returns:** bool - True if more tokens

```python
from stamp.java import Scanner

scanner = Scanner("Hello World")
while scanner.hasNext():
    print(scanner.next())
```

### Scanner.close()

Close scanner.

```python
from stamp.java import Scanner

scanner = Scanner("Hello World")
scanner.close()
```

## Usage Examples

### Hello World

```python
from stamp.java import System

System.out.println("Hello, World!")
```

### String Operations

```python
from stamp.java import String

s = String("Hello World")
System.out.println(s.length())
System.out.println(s.toUpperCase())
System.out.println(s.substring(0, 5))
```

### Math Operations

```python
from stamp.java import Math

System.out.println(Math.abs(-5))
System.out.println(Math.max(10, 20))
System.out.println(Math.sqrt(25))
```

### ArrayList

```python
from stamp.java import ArrayList

list = ArrayList()
list.add(1)
list.add(2)
list.add(3)

System.out.println(list.size())
System.out.println(list.get(0))
```

### HashMap

```python
from stamp.java import HashMap

map = HashMap()
map.put("name", "Alice")
map.put("age", 25)

System.out.println(map.get("name"))
```

## Notes

- Java emulation allows Java-like syntax in Python
- Most Java standard library methods are available
- Uses Python list/dict/set internally
- Scanner can parse strings or files
- All operations are Python-optimized

---

See [Java Emulation Examples](../examples/java-emu.md) for more examples.
See [Java Guide](../guides/java-guide.md) for detailed guide.
