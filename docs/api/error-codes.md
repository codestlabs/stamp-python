# Error Codes API Reference

36+ custom error codes with Rich formatting.

## Import

```python
from stamp.main import adverr, Control
```

## Overview

Stamp provides 36+ custom error codes through the `adverr` class. Each error code is formatted with Rich and provides detailed information about the error.

## Error Codes

### e0 - KeyboardInterrupt

Raised when user interrupts program execution.

```python
from stamp.main import adverr

adverr.e0()
```

**Exception:** `KeyboardInterrupt`

---

### e1 - NotADirectoryError

Raised when operation expected a directory but got something else.

```python
from stamp.main import adverr

adverr.e1()
```

**Exception:** `NotADirectoryError`

---

### e2 - FileNotFoundError

Raised when file or directory not found.

```python
from stamp.main import adverr

adverr.e2()
```

**Exception:** `FileNotFoundError`

---

### e3 - PermissionError

Raised when insufficient permissions for operation.

```python
from stamp.main import adverr

adverr.e3()
```

**Exception:** `PermissionError`

---

### e4 - DeprecationWarning

Warning about deprecated feature.

```python
from stamp.main import adverr

adverr.e4()
```

**Exception:** `DeprecationWarning`

---

### e5 - NotImplementedError

Raised when method/feature not implemented.

```python
from stamp.main import adverr

adverr.e5()
```

**Exception:** `NotImplementedError`

---

### e6 - LookupError

Base class for index/key errors.

```python
from stamp.main import adverr

adverr.e6()
```

**Exception:** `LookupError`

---

### e7 - ValueError

Raised when value has inappropriate type.

```python
from stamp.main import adverr

adverr.e7()
```

**Exception:** `ValueError`

---

### e8 - TypeError

Raised when operation applied to object of inappropriate type.

```python
from stamp.main import adverr

adverr.e8()
```

**Exception:** `TypeError`

---

### e9 - OSError

Raised when system function returns system-related error.

```python
from stamp.main import adverr

adverr.e9()
```

**Exception:** `OSError`

---

### e10 - IOError

I/O operation failed (alias for OSError in Python 3).

```python
from stamp.main import adverr

adverr.e10()
```

**Exception:** `IOError`

---

### e11 - ImportError

Module import failed.

**Parameters:**
- `e` (str): Exception message

```python
from stamp.main import adverr

adverr.e11("Module 'requests' not found")
```

**Exception:** `ImportError`

---

### e12 - CalledProcessError

Subprocess returned non-zero exit status.

**Parameters:**
- `e` (str): Exception message

```python
from stamp.main import adverr

adverr.e12("Command 'git' failed with exit code 1")
```

**Exception:** `CalledProcessError`

---

### e13 - SystemError

Internal interpreter error.

```python
from stamp.main import adverr

adverr.e13()
```

**Exception:** `SystemError`

---

### e14 - SyntaxError

Invalid syntax.

```python
from stamp.main import adverr

adverr.e14()
```

**Exception:** `SyntaxError`

---

### e15 - MemoryError

Out of memory.

```python
from stamp.main import adverr

adverr.e15()
```

**Exception:** `MemoryError`

---

### e16 - OverflowError

Arithmetic operation result too large.

```python
from stamp.main import adverr

adverr.e16()
```

**Exception:** `OverflowError`

---

### e17 - SyntaxWarning

Warning about suspicious syntax.

```python
from stamp.main import adverr

adverr.e17()
```

**Exception:** `SyntaxWarning`

---

### e18 - TimestampError

Invalid timestamp format or value.

```python
from stamp.main import adverr

adverr.e18()
```

**Exception:** `TimestampError`

---

### e19 - AttributeError

Attribute not found.

```python
from stamp.main import adverr

adverr.e19()
```

**Exception:** `AttributeError`

---

### e20 - WindowsError

Windows-specific error.

```python
from stamp.main import adverr

adverr.e20()
```

**Exception:** `WindowsError`

---

### e21 - IndexError

Sequence index out of range.

```python
from stamp.main import adverr

adverr.e21()
```

**Exception:** `IndexError`

---

### e22 - IndentationError

Improper indentation.

```python
from stamp.main import adverr

adverr.e22()
```

**Exception:** `IndentationError`

---

### e23 - KeyError

Mapping key not found.

```python
from stamp.main import adverr

adverr.e23()
```

**Exception:** `KeyError`

---

### e24 - UnicodeError

Unicode-related error.

```python
from stamp.main import adverr

adverr.e24()
```

**Exception:** `UnicodeError`

---

### e25 - UnicodeEncodeError

Unicode encoding error.

```python
from stamp.main import adverr

adverr.e25()
```

**Exception:** `UnicodeEncodeError`

---

### e26 - UnicodeDecodeError

Unicode decoding error.

```python
from stamp.main import adverr

adverr.e26()
```

**Exception:** `UnicodeDecodeError`

---

### e27 - UnicodeTranslateError

Unicode translation error.

```python
from stamp.main import adverr

adverr.e27()
```

**Exception:** `UnicodeTranslateError`

---

### e28 - UnicodeWarning

Unicode-related warning.

```python
from stamp.main import adverr

adverr.e28()
```

**Exception:** `UnicodeWarning`

---

### e29 - EnvironmentError

Environment-related error (alias for OSError).

```python
from stamp.main import adverr

adverr.e29()
```

**Exception:** `EnvironmentError`

---

### e30 - ConnectionResetError

Connection reset by peer.

```python
from stamp.main import adverr

adverr.e30()
```

**Exception:** `ConnectionResetError`

---

### e31 - ConnectionError

Connection-related error base class.

```python
from stamp.main import adverr

adverr.e31()
```

**Exception:** `ConnectionError`

---

### e32 - ConnectionAbortedError

Connection aborted.

```python
from stamp.main import adverr

adverr.e32()
```

**Exception:** `ConnectionAbortedError`

---

### e33 - ConnectionRefusedError

Connection refused.

```python
from stamp.main import adverr

adverr.e33()
```

**Exception:** `ConnectionRefusedError`

---

### e34 - TimeoutError

Operation timed out.

```python
from stamp.main import adverr

adverr.e34()
```

**Exception:** `TimeoutError`

---

### e35 - Exception

Base exception class.

**Parameters:**
- `e` (str): Exception message

```python
from stamp.main import adverr

adverr.e35("Unexpected error occurred")
```

**Exception:** `Exception`

---

## Control Class

The `Control` class provides programmatic control over error raising.

### Control.ct(adverrErrorInt, e="")

Raise error by code.

**Parameters:**
- `adverrErrorInt` (int): Error code (0-35)
- `e` (str): Exception message (for codes 11, 12, 35)

**Returns:** None (raises exception)

```python
from stamp.main import Control

# Basic usage
Control.ct(2)  # FileNotFoundError
Control.ct(7)  # ValueError
Control.ct(8)  # TypeError

# With message
Control.ct(11, "Module 'numpy' not found")
Control.ct(12, "Command failed with exit code 1")
Control.ct(35, "Custom error message")
```

### Using with try-except

```python
from stamp.main import Control, adverr

try:
    Control.ct(7)  # ValueError
except ValueError as e:
    print(f"Caught ValueError: {e}")

try:
    Control.ct(11, "Module not found")
except ImportError as e:
    print(f"Caught ImportError: {e}")
```

## Error Handling Patterns

### Basic Error Handling

```python
from stamp.main import adverr

try:
    # Some operation
    pass
except FileNotFoundError:
    adverr.e2()
except ValueError:
    adverr.e7()
except Exception as e:
    print(f"Unexpected error: {e}")
    adverr.e35(str(e))
```

### Conditional Error Raising

```python
from stamp.main import Control

def validate_input(value):
    if value < 0:
        Control.ct(7)  # ValueError
    elif value > 100:
        Control.ct(7)  # ValueError

validate_input(150)  # Raises ValueError
```

### Custom Error Messages

```python
from stamp.main import adverr, Control

def load_module(module_name):
    try:
        __import__(module_name)
    except ImportError as e:
        Control.ct(11, f"Module '{module_name}' not found: {e}")
```

## Error Code Reference Table

| Code | Exception | Needs Message |
|------|-----------|---------------|
| e0 | KeyboardInterrupt | No |
| e1 | NotADirectoryError | No |
| e2 | FileNotFoundError | No |
| e3 | PermissionError | No |
| e4 | DeprecationWarning | No |
| e5 | NotImplementedError | No |
| e6 | LookupError | No |
| e7 | ValueError | No |
| e8 | TypeError | No |
| e9 | OSError | No |
| e10 | IOError | No |
| e11 | ImportError | Yes |
| e12 | CalledProcessError | Yes |
| e13 | SystemError | No |
| e14 | SyntaxError | No |
| e15 | MemoryError | No |
| e16 | OverflowError | No |
| e17 | SyntaxWarning | No |
| e18 | TimestampError | No |
| e19 | AttributeError | No |
| e20 | WindowsError | No |
| e21 | IndexError | No |
| e22 | IndentationError | No |
| e23 | KeyError | No |
| e24 | UnicodeError | No |
| e25 | UnicodeEncodeError | No |
| e26 | UnicodeDecodeError | No |
| e27 | UnicodeTranslateError | No |
| e28 | UnicodeWarning | No |
| e29 | EnvironmentError | No |
| e30 | ConnectionResetError | No |
| e31 | ConnectionError | No |
| e32 | ConnectionAbortedError | No |
| e33 | ConnectionRefusedError | No |
| e34 | TimeoutError | No |
| e35 | Exception | Yes |

## Notes

- All errors are formatted with Rich for better readability
- Error codes e11, e12, and e35 accept optional message parameters
- Use `Control.ct()` for programmatic error raising
- Errors can be caught with standard try-except blocks
- Error formatting includes detailed traceback information

---

See [Core API](core.md) for main module documentation.
See [Error Handling Examples](../examples/error-handling.md) for usage examples.
