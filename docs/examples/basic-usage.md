# Basic Usage Examples

Fundamental Stamp usage examples.

## Import

```python
from stamp.main import Stamp, edit, Debug, adverr, __msrv__, _kvstore
```

## Timestamps

### Get Current Timestamp

```python
from stamp.main import Stamp

# Simple timestamp
ts = Stamp.stamp_()
print(f"Current time: {ts}")
# Output: ML2-CT0-ST02-M09-D18-H12-MI05-pm-S30
```

### Log Timestamps

```python
from stamp.main import Stamp, __log__

# Create log with timestamp
timestamp = Stamp.stamp_()
__log__.log(timestamp, "app.log", "\n")
```

## String Manipulation

### Text Processing

```python
from stamp.main import edit

# Basic operations
text = "Hello World"

result = edit.join("Hello", " ", "World")
print(result)  # Hello World

result = edit.split("a,b,c", ",")
print(result)  # ['a', 'b', 'c']

# Case conversion
result = edit.upper("hello")
print(result)  # HELLO

result = edit.lower("HELLO")
print(result)  # hello

result = edit.capitalize("hello world")
print(result)  # Hello world

result = edit.title("hello world")
print(result)  # Hello World

# Reversal
result = edit.reverse("hello")
print(result)  # olleh
```

### String Checks

```python
from stamp.main import edit

# Validation
print(edit.isalpha("hello"))   # True
print(edit.isdigit("123"))     # True
print(edit.isalnum("abc123"))  # True
print(edit.isspace("   "))      # True
print(edit.islower("hello"))    # True
print(edit.isupper("HELLO"))    # True

# Prefix/Suffix
text = "hello world.txt"
print(edit.startswith(text, "hello"))  # True
print(edit.endswith(text, ".txt"))      # True
```

### Text Search and Replace

```python
from stamp.main import edit

text = "hello world"

# Find position
pos = edit.find(text, "world")
print(pos)  # 6

# Count occurrences
count = edit.count("hello hello", "hello")
print(count)  # 2

# Replace
result = edit.replace("hello world", "world", "python")
print(result)  # hello python

# Strip whitespace
result = edit.strip("  hello  ")
print(result)  # hello
```

### Advanced String Operations

```python
from stamp.main import edit

# Camel case
result = edit.camel_case("hello world")
print(result)  # helloWorld

# Snake case
result = edit.snake_case("hello world")
print(result)  # hello_world

# Pad with zeros
result = edit.zfill("123", 6)
print(result)  # 000123

# Swap case
result = edit.swapcase("Hello World")
print(result)  # hELLO wORLD
```

## Debugging

### Debug Levels

```python
from stamp.main import Debug

# Different levels
Debug.debug("Variable state: x=5")
Debug.info("Application started")
Debug.warn("Memory usage high")
Debug.error("Failed to connect to database")
Debug.critical("System crash imminent")
```

### Custom Debug Messages

```python
from stamp.main import Debug

# Custom tag
Debug.custom("AUTH", "User logged in", capital=True)
# AUTH USER LOGGED IN

Debug.custom("auth", "User logged in", capital=False)
# auth user logged in
```

### Lowercase Debug

```python
from stamp.main import Debug

# All lowercase
Debug.debug("Debug message", lower=True)
Debug.info("Info message", lower=True)
Debug.warn("Warning message", lower=True)
```

## Error Handling

### Using Error Codes

```python
from stamp.main import adverr

# Common errors
adverr.e0()   # KeyboardInterrupt
adverr.e2()   # FileNotFoundError
adverr.e3()   # PermissionError
adverr.e7()   # ValueError
adverr.e8()   # TypeError
```

### With Exception Messages

```python
from stamp.main import adverr

# Errors with messages
adverr.e11("Module 'requests' not found")
adverr.e12("Command 'git' failed with exit code 1")
adverr.e35("Unexpected error occurred")
```

### Control Class

```python
from stamp.main import Control

# Programmatic error control
try:
    Control.ct(7)  # ValueError
except Exception as e:
    print(f"Error code raised: {e}")

# With messages
Control.ct(11, "Cannot import module")
Control.ct(12, "Process failed")
```

## Data Storage

### Memory Server

```python
from stamp.main import __msrv__

# Add items
__msrv__.addMem("user1")
__msrv__.addMem("user2")
__msrv__.addMem("user3")

# List all
__msrv__.srv()
# [0]/user1
# [1]/user2
# [2]/user3

# Delete by index
__msrv__.delMem(0)
# Removed: user1

# Delete by value
__msrv__.delMem("user2")
# Removed: user2

# Reset (clear all)
__msrv__.resetMem()
__msrv__.srv()
# memsrv: msrv: server mlock empty.
```

### Key-Value Store

```python
from stamp.main import _kvstore

# Set key-value pairs
_kvstore.set("app_name", "MyApp")
_kvstore.set("version", "1.0.0")
_kvstore.set("debug_mode", "true")

# Get values
app_name = _kvstore.get("app_name")
print(app_name)  # MyApp

version = _kvstore.get("version")
print(version)  # 1.0.0

# List all
_kvstore.list()
# app_name: MyApp
# version: 1.0.0
# debug_mode: true

# Delete key
_kvstore.delete("debug_mode")

# Export to file
_kvstore.export("config.txt")
# kvstore: exported 2 items to config.txt
```

### History Tracking

```python
from stamp.main import _history

# Add to history
_history.add("Stamp.stamp_()")
_history.add("edit.join('a', 'b')")
_history.add("Debug.info('Started')")

# Show history
_history.show()
# [0] Stamp.stamp_()
# [1] edit.join('a', 'b')
# [2] Debug.info('Started')

# Get specific command
cmd = _history.get(1)
print(cmd)  # edit.join('a', 'b')

# Export history
_history.export("history.txt")
# history: exported 3 items to history.txt
```

## System Information

### Hardware Stats

```python
from stamp.main import PCStamp

# Get system info
PCStamp(sysinfo=True)
# cores.physical:8
# cores.total:12
# cpu.usagepercent:45%
# mem.total.gb:16.0GB
# mem.avail.gb:8.5GB
# virtual.mempercent:47%
# disk.total.gb:512.0GB
# disk.used.gb:256.0GB
# disk.usagepercent:50%
# system.platform:win32
# system.executable:C:\Python\python.exe
# system.$PATH:[...]
# system.argv:['script.py']
# system.modules:{...}
# timestamp: ML2-CT0-ST02-M09-D18-H12-MI05-pm-S30
```

### Location Info

```python
from stamp.main import PCStamp

# Get IP addresses
PCStamp(lri=True)
```

### Both

```python
from stamp.main import PCStamp

# Get everything
PCStamp(lri=True, sysinfo=True)
```

## Text Processing

### Process User Input

```python
from stamp.main import edit, Debug

# Clean input
user_input = "  HELLO WORLD  "

# Trim
cleaned = edit.strip(user_input)
# HELLO WORLD

# Normalize case
normalized = edit.lower(cleaned)
# hello world

# Validate
if edit.isalnum(normalized):
    Debug.info(f"Valid input: {normalized}")
else:
    Debug.warn(f"Invalid input: {normalized}")
```

### Filename Processing

```python
from stamp.main import edit

filename = "my_document.txt"

# Check extension
if edit.endswith(filename, ".txt"):
    print("Text file")

# Get name without extension
name = edit.split(filename, ".")[0]
print(name)  # my_document

# Create backup
backup = edit.join(name, "_backup.txt")
print(backup)  # my_document_backup.txt
```

## Config Values

### Using Config Holders

```python
from stamp.main import S1, S2, C1, C2, K1, K2, temp

# Set values
S1.set("username")
C1.set("127.0.0.1")
K1.set("value1")

# Use values
username = S1.get()
host = C1.get()
key = K1.get()

print(f"Connecting to {username}@{host} with key {key}")
```

## Complete Example

```python
from stamp.main import (
    Stamp, edit, Debug, adverr,
    __msrv__, _kvstore, _history, PCStamp
)

def main():
    # Log start
    timestamp = Stamp.stamp_()
    Debug.info(f"Started at {timestamp}")
    _history.add(f"App started at {timestamp}")
    
    # Load config
    _kvstore.set("start_time", timestamp)
    _kvstore.set("status", "running")
    
    # Process data
    text = "  hello world  "
    cleaned = edit.strip(text)
    Debug.debug(f"Cleaned text: {cleaned}")
    
    # Add to memory
    __msrv__.addMem(cleaned)
    
    # Check system
    PCStamp(sysinfo=True, lri=True)
    
    # Save history
    _history.export("session_history.txt")
    _kvstore.export("session_config.txt")
    
    # Log completion
    Debug.info("Session completed")
    __msrv__.srv()

if __name__ == "__main__":
    main()
```

## Next Steps

- [API Reference](../api/core.md) - Complete API documentation
- [Timestamp Examples](timestamps.md) - More timestamp examples
- [Physics Demo](physics-demo.md) - Physics simulation examples
- [Advanced Examples](advanced.md) - Advanced usage patterns

---

**More examples available in:** [Examples Index](../examples/basic-usage.md)
