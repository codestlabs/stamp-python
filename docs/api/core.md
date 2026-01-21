# Core API Reference

Main module - core functionality for Stamp.

## Import

```python
from stamp.main import Stamp, PCStamp, edit, Debug, adverr
```

## Classes

### Stamp

Static methods for timestamping and core operations.

#### Stamp.stamp_()
Returns current timestamp in Stamp format.

```python
timestamp = Stamp.stamp_()
print(timestamp)
# Output: ML2-CT0-ST02-M09-D18-H12-MI05-pm-S30
```

**Format:**
- `ML{millennia}` - Millennium
- `CT{century}` - Century  
- `ST{sub_year_tens}{sub_year_ones}` - Year parts
- `M{month}` - Month (01-12)
- `D{day}` - Day (01-31)
- `H{hour}` - Hour (00-23)
- `MI{minute}` - Minute (00-59)
- `{am/pm}` - AM or PM
- `S{second}` - Second (00-59)

### PCStamp

System and hardware information.

#### PCStamp.__get_hardware_stats__(lri=None, sysinfo=None)

Get detailed system information.

**Parameters:**
- `lri` (bool): Location related info (IP addresses)
- `sysinfo` (bool): System information (CPU, memory, disk)

**Returns:** None (prints to console)

```python
# Get system info only
PCStamp(lri=None, sysinfo=True)

# Get location info only
PCStamp(lri=True, sysinfo=None)

# Get both
PCStamp(lri=True, sysinfo=True)
```

**Displays:**
- CPU cores (physical/total)
- CPU usage percentage
- Memory (total GB, available GB)
- Disk usage (total GB, used GB)
- Virtual memory percentage
- System platform
- Python version
- Public IP address
- Private IP address

### ErrorSystem

Custom error handling with detailed tracebacks.

#### ErrorSystem.CustomError()

Create custom error with traceback.

**Parameters:**
- `ErrorName` (str): Error name
- `errorMessage` (str): Error message
- `fileCausedErrorFilePath` (str): File path
- `fileCausedErrorLine` (int): Line number
- `fileCausedErrorColumn` (int): Column number
- `inModuleName` (str): Module name
- `fileCausedErrorLineContents` (str): Line content

```python
ErrorSystem.CustomError(
    ErrorName="CustomError",
    errorMessage="Something went wrong",
    fileCausedErrorFilePath="script.py",
    fileCausedErrorLine=10,
    fileCausedErrorColumn=5,
    inModuleName="main",
    fileCausedErrorLineContents="print(\"hello\")"
)
```

#### ErrorSystem.NotEnoughArgumentsProvidedError()

Show argument count errors.

**Parameters:**
- `argumentNeedCount` (int): Required arguments
- `argumentGivenCount` (int): Given arguments
- `classOrDefName` (str): Class/function name
- `classOrDefIsClass` (bool): Is a class?
- `classOrDefIsDef` (bool): Is a function?
- `classOrDefIsMethod` (bool): Is a method?
- `anythingInputed` (bool): Was anything input?

### ListDirectory

Directory listing with multiple options.

#### ListDirectory.listdir(fromRoot=None, openInSeperateCMD=None)

List directory contents.

**Parameters:**
- `fromRoot` (bool): List from root (C:\ or /)
- `openInSeperateCMD` (bool): Open in separate terminal

```python
# List current directory
ListDirectory.listdir(fromRoot=False, openInSeperateCMD=False)

# List root in separate CMD
ListDirectory.listdir(fromRoot=True, openInSeperateCMD=True)
```

## Classes: Data Management

### __msrv__

In-memory data storage.

#### __msrv__.addMem(mem)
Add item to memory store.

```python
__msrv__.addMem("item1")
```

#### __msrv__.delMem(index)
Delete item from memory store.

**Parameters:**
- `index` (int or str): Index or value to delete

```python
__msrv__.delMem(0)  # Delete by index
__msrv__.delMem("item1")  # Delete by value
```

#### __msrv__.resetMem()
Clear all items from memory store.

```python
__msrv__.resetMem()
```

#### __msrv__.srv()
List all items in memory store.

```python
__msrv__.srv()
# Output:
# [0]/item1
# [1]/item2
```

### _kvstore

Key-value storage with file export.

#### _kvstore.set(key, value)
Set key-value pair.

```python
_kvstore.set("name", "Stamp")
_kvstore.set("version", "4.3.2.2")
```

#### _kvstore.get(key)
Get value by key.

```python
name = _kvstore.get("name")
print(name)  # Stamp
```

#### _kvstore.delete(key)
Delete key-value pair.

```python
_kvstore.delete("version")
```

#### _kvstore.list()
List all key-value pairs.

```python
_kvstore.list()
```

#### _kvstore.export(file, end="\n", endOnNewline=True)
Export to file.

```python
_kvstore.export("kvstore.txt", end="\n", endOnNewline=True)
```

### _history

Command history tracking.

#### _history.add(cmd)
Add command to history.

```python
_history.add("Stamp.stamp_()")
```

#### _history.show()
Show all commands in history.

```python
_history.show()
# Output:
# [0] Stamp.stamp_()
# [1] edit.join("a", "b")
```

#### _history.get(index)
Get command by index.

```python
cmd = _history.get(0)
print(cmd)  # Stamp.stamp_()
```

#### _history.export(file, end="\n", endOnNewline=True)
Export history to file.

```python
_history.export("history.txt")
```

## Classes: String Manipulation

### edit

Extensive string manipulation tools.

#### edit.join(W1, W2)
Join two strings.

```python
result = edit.join("Hello", "World")
print(result)  # HelloWorld
```

#### edit.split(text, splitby)
Split string.

```python
parts = edit.split("a,b,c", ",")
print(parts)  # ['a', 'b', 'c']
```

#### edit.upper(text)
Convert to uppercase.

```python
result = edit.upper("hello")
print(result)  # HELLO
```

#### edit.lower(text)
Convert to lowercase.

```python
result = edit.lower("HELLO")
print(result)  # hello
```

#### edit.replace(text, old, new)
Replace substring.

```python
result = edit.replace("hello world", "world", "python")
print(result)  # hello python
```

#### edit.find(text, find)
Find substring.

```python
index = edit.find("hello world", "world")
print(index)  # 6
```

#### edit.count(text, count)
Count occurrences.

```python
count = edit.count("hello hello", "hello")
print(count)  # 2
```

#### edit.startswith(text, startswith)
Check if starts with.

```python
result = edit.startswith("hello world", "hello")
print(result)  # True
```

#### edit.endswith(text, endswith)
Check if ends with.

```python
result = edit.endswith("hello world", "world")
print(result)  # True
```

#### edit.isalpha(text)
Check if all alphabetic.

```python
result = edit.isalpha("hello")
print(result)  # True
```

#### edit.isdigit(text)
Check if all digits.

```python
result = edit.isdigit("123")
print(result)  # True
```

#### edit.isalnum(text)
Check if alphanumeric.

```python
result = edit.isalnum("abc123")
print(result)  # True
```

#### edit.isspace(text)
Check if all whitespace.

```python
result = edit.isspace("   ")
print(result)  # True
```

#### edit.islower(text)
Check if all lowercase.

```python
result = edit.islower("hello")
print(result)  # True
```

#### edit.isupper(text)
Check if all uppercase.

```python
result = edit.isupper("HELLO")
print(result)  # True
```

#### edit.title(text)
Convert to title case.

```python
result = edit.title("hello world")
print(result)  # Hello World
```

#### edit.capitalize(text)
Capitalize first letter.

```python
result = edit.capitalize("hello")
print(result)  # Hello
```

#### edit.swapcase(text)
Swap case.

```python
result = edit.swapcase("Hello World")
print(result)  # hELLO wORLD
```

#### edit.zfill(text, width)
Pad with zeros.

```python
result = edit.zfill("123", 6)
print(result)  # 000123
```

#### edit.strip(text, chars=None)
Strip whitespace/characters.

```python
result = edit.strip("  hello  ")
print(result)  # hello
```

#### edit.reverse(text)
Reverse string.

```python
result = edit.reverse("hello")
print(result)  # olleh
```

#### edit.camel_case(text)
Convert to camelCase.

```python
result = edit.camel_case("hello world")
print(result)  # helloWorld
```

#### edit.snake_case(text)
Convert to snake_case.

```python
result = edit.snake_case("hello world")
print(result)  # hello_world
```

## Classes: Debugging

### Debug

Formatted debug output.

#### Debug.debug(dbgmsg, lower=None)
Debug message.

```python
Debug.debug("This is a debug message")
# DEBUG This is a debug message

Debug.debug("This is a debug message", lower=True)
# debug this is a debug message
```

#### Debug.info(infomsg, lower=None)
Info message.

```python
Debug.info("Application started")
# INFO Application started
```

#### Debug.warn(warnmsg, lower=None)
Warning message.

```python
Debug.warn("Low memory")
# WARN Low memory
```

#### Debug.error(errmsg, lower=None)
Error message.

```python
Debug.error("Failed to connect")
# ERROR Failed to connect
```

#### Debug.critical(critmsg, lower=None)
Critical message.

```python
Debug.critical("System crash imminent")
# CRITICAL System crash imminent
```

#### Debug.custom(errname, errmsg, capital=None)
Custom message.

```python
Debug.custom("MYTAG", "Custom message", capital=True)
# MYTAG CUSTOM MESSAGE

Debug.custom("mytag", "Custom message", capital=False)
# mytag custom message
```

## Classes: Error Handling

### adverr

36+ error codes with Rich formatting.

#### Error Codes

```python
adverr.e0()   # KeyboardInterrupt
adverr.e1()   # NotADirectoryError
adverr.e2()   # FileNotFoundError
adverr.e3()   # PermissionError
adverr.e4()   # DeprecationWarning
adverr.e5()   # NotImplementedError
adverr.e6()   # LookupError
adverr.e7()   # ValueError
adverr.e8()   # TypeError
adverr.e9()   # OSError
adverr.e10()  # IOError
adverr.e11(e) # ImportError
adverr.e12(e) # CalledProcessError
adverr.e13()  # SystemError
adverr.e14()  # SyntaxError
adverr.e15()  # MemoryError
adverr.e16()  # OverflowError
adverr.e17()  # SyntaxWarning
adverr.e18()  # TimestampError
adverr.e19()  # AttributeError
adverr.e20()  # WindowsError
adverr.e21()  # IndexError
adverr.e22()  # IndentationError
adverr.e23()  # KeyError
adverr.e24()  # UnicodeError
adverr.e25()  # UnicodeEncodeError
adverr.e26()  # UnicodeDecodeError
adverr.e27()  # UnicodeTranslateError
adverr.e28()  # UnicodeWarning
adverr.e29()  # EnvironmentError
adverr.e30()  # ConnectionResetError
adverr.e31()  # ConnectionError
adverr.e32()  # ConnectionAbortedError
adverr.e33()  # ConnectionRefusedError
adverr.e34()  # TimeoutError
adverr.e35(e) # Exception
```

### Control

Programmatic error control.

#### Control.ct(adverrErrorInt, e="")
Raise error by code.

**Parameters:**
- `adverrErrorInt` (int): Error code (0-35)
- `e` (str): Exception message (for codes 11, 12, 35)

```python
Control.ct(2)  # FileNotFoundError
Control.ct(7)  # ValueError
Control.ct(11, "Module not found")  # ImportError with message
```

## Classes: Configuration

### _ConfigValue

Named value holder.

```python
from stamp.main import S1, S2, C1, C2, K1, K2, T1, T2, L1, L2, R1, R2, temp

# Set values
S1.set("value1")
S2.set("value2")

# Get values
value = S1.get()

# Convert to string
str(S1)
```

Pre-configured holders:
- `S1, S2` - String holders
- `C1, C2` - Config holders
- `K1, K2` - Key holders
- `T1, T2` - Temporary holders
- `L1, L2` - List holders
- `R1, R2` - Reference holders
- `temp` - Temporary holder

---

See [Timestamp API](timestamps.md) for timestamp details.
See [Utilities API](utilities.md) for more utilities.
