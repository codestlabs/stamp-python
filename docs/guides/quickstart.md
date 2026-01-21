# Stamp Quickstart Guide

Get started with Stamp in 5 minutes.

## Installation

Stamp is monolithic - everything is in one module. Just place the `stamp` folder in your Python path or import directly.

```python
from stamp.main import Stamp, edit, Debug, PCStamp
```

Or use the package:

```python
import stamp
from stamp.main import Stamp
```

## Your First Timestamp

Stamp's custom timestamp format is unique:

```python
from stamp.main import Stamp

# Get current timestamp
timestamp = Stamp.stamp_()
print(timestamp)
# Output: ML2-CT0-ST02-M09-D18-H12-MI05-pm-S30
```

The format breaks down as:
- `ML{millennia}` - Millennium number
- `CT{century}` - Century
- `ST{sub_year_tens}{sub_year_ones}` - Year parts
- `M{month}` - Month
- `D{day}` - Day
- `H{hour}` - Hour
- `MI{minute}` - Minute
- `{am/pm}` - AM/PM
- `S{second}` - Second

## Error Handling

Stamp includes 36+ custom error codes:

```python
from stamp.main import adverr, Debug

# Use error codes
adverr.e2()  # FileNotFoundError
adverr.e7()  # ValueError
adverr.e8()  # TypeError

# Or use the Control class
from stamp.main import Control
Control.ct(2)  # Raises FileNotFoundError
```

## String Manipulation

The `edit` class provides extensive string tools:

```python
from stamp.main import edit

text = "Hello World"

# Common operations
print(edit.join("Hello", "World"))  # HelloWorld
print(edit.split("a,b,c", ","))    # ['a', 'b', 'c']
print(edit.upper("hello"))           # HELLO
print(edit.lower("HELLO"))           # hello
print(edit.replace("hello", "world"))  # world
print(edit.reverse("hello"))          # olleh

# String checks
print(edit.isalpha("hello"))   # True
print(edit.isdigit("123"))     # True
print(edit.isalnum("abc123")) # True

# Case conversion
print(edit.title("hello world"))  # Hello World
print(edit.capitalize("hello"))   # Hello
print(edit.camel_case("hello world"))  # helloWorld
print(edit.snake_case("hello world"))  # hello_world
```

## Debugging

Use the Debug class for formatted output:

```python
from stamp.main import Debug

Debug.debug("This is a debug message")
Debug.info("This is info")
Debug.warn("This is a warning")
Debug.error("This is an error")
Debug.critical("This is critical")
Debug.custom("MYTAG", "Custom message", capital=True)
```

## Memory Server

Store data in memory:

```python
from stamp.main import __msrv__

# Add items
__msrv__.addMem("item1")
__msrv__.addMem("item2")
__msrv__.addMem("item3")

# List all items
__msrv__.srv()

# Delete by index
__msrv__.delMem(0)

# Delete by value
__msrv__.delMem("item2")

# Reset (clear all)
__msrv__.resetMem()
```

## Key-Value Store

```python
from stamp.main import _kvstore

# Set values
_kvstore.set("name", "Stamp")
_kvstore.set("version", "4.3.2.2")

# Get values
name = _kvstore.get("name")
print(name)  # Stamp

# List all
_kvstore.list()

# Delete
_kvstore.delete("version")

# Export to file
_kvstore.export("kvstore_export.txt")
```

## System Information

Get hardware and system stats:

```python
from stamp.main import PCStamp

# Get all system info
PCStamp(lri=True, sysinfo=True)
```

This displays:
- CPU cores (physical and total)
- CPU usage percentage
- Memory (total GB, available GB)
- Disk usage (total GB, used GB)
- System platform
- Python version
- Public and private IP addresses

## Next Steps

- [API Reference](../api/core.md) - Complete API documentation
- [Examples](../examples/basic-usage.md) - More code examples
- [Physics Guide](physics-guide.md) - Using the physics engine
- [Java Guide](java-guide.md) - Java emulation

## Common Imports

```python
from stamp.main import (
    Stamp, PCStamp, edit, Debug, adverr,
    __msrv__, _kvstore, _history,
    Type, Frozen, _calc
)

# For physics
from stamp.physics import PhysicsSim, PhysicsObject

# For servers
from stamp.server import run_server, run_ws, run_http
```

---