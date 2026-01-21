# Timestamp API Reference

Custom timestamp format and Fetch class.

## Import

```python
from stamp.main import Stamp
from stamp.__fetch__ import Fetch
```

## Stamp Timestamp Format

Stamp uses a unique timestamp format that breaks down time into components:

```
ML{millennia}-CT{century}-ST{sub_year_tens}{sub_year_ones}-M{month}-D{day}-H{hour}-MI{minute}-{am/pm}-S{second}
```

### Format Components

| Component | Format | Description | Range |
|-----------|--------|-------------|-------|
| `ML` | ML{N} | Millennium | 0-9 |
| `CT` | CT{N} | Century | 0-9 |
| `ST` | ST{N}{N} | Sub-year (tens + ones) | 00-99 |
| `M` | M{N} | Month | 01-12 |
| `D` | D{N} | Day | 01-31 |
| `H` | H{N} | Hour | 00-23 |
| `MI` | MI{N} | Minute | 00-59 |
| `--` | {am/pm} | AM/PM indicator | am, pm |
| `S` | S{N} | Second | 00-59 |

### Example

```
ML2-CT0-ST02-M09-D18-H12-MI05-pm-S30
```

Breakdown:
- Millennium: 2
- Century: 0
- Year: 2025 (20 = CT0 ST02)
- Month: 09 (September)
- Day: 18
- Hour: 12
- Minute: 05
- Period: pm
- Second: 30

## Stamp Class

### Stamp.stamp_()
Get current timestamp in Stamp format.

**Returns:** str - Timestamp string

```python
from stamp.main import Stamp

timestamp = Stamp.stamp_()
print(timestamp)
# Output: ML2-CT0-ST02-M09-D18-H12-MI05-pm-S30
```

## Fetch Class

### Fetch.stamp_()
Get current timestamp.

**Returns:** str - Timestamp string

```python
from stamp.__fetch__ import Fetch

timestamp = Fetch.stamp_()
print(timestamp)
# Output: ML2-CT0-ST02-M09-D18-H12-MI05-pm-S30
```

### Fetch.fetch()
Alias for `stamp_()`.

**Returns:** str - Timestamp string

```python
from stamp.__fetch__ import Fetch

timestamp = Fetch.fetch()
print(timestamp)
# Output: ML2-CT0-ST02-M09-D18-H12-MI05-pm-S30
```

### Fetch.date_()
Get date components.

**Returns:** dict - Date components

```python
from stamp.__fetch__ import Fetch

date = Fetch.date_()
print(date)
# Output:
# {
#     'millennium': 2,
#     'century': 0,
#     'sub_year_tens': 2,
#     'sub_year_ones': 5,
#     'year': 2025,
#     'month': 9,
#     'day': 18
# }
```

### Fetch.time_()
Get time components.

**Returns:** dict - Time components

```python
from stamp.__fetch__ import Fetch

time = Fetch.time_()
print(time)
# Output:
# {
#     'hour': 12,
#     'minute': 5,
#     'second': 30,
#     'period': 'pm'
# }
```

### Fetch.full_()
Get all components.

**Returns:** dict - All timestamp components

```python
from stamp.__fetch__ import Fetch

full = Fetch.full_()
print(full)
# Output:
# {
#     'millennium': 2,
#     'century': 0,
#     'sub_year_tens': 2,
#     'sub_year_ones': 5,
#     'year': 2025,
#     'month': 9,
#     'day': 18,
#     'hour': 12,
#     'minute': 5,
#     'second': 30,
#     'period': 'pm',
#     'timestamp': 'ML2-CT0-ST02-M09-D18-H12-MI05-pm-S30'
# }
```

### Fetch.format(format_str)
Format timestamp using custom format.

**Parameters:**
- `format_str` (str): Format string with placeholders

**Placeholders:**
- `%ML` - Millennium
- `%CT` - Century
- `%ST` - Sub-year (full)
- `%SY` - Sub-year tens
- `%SO` - Sub-year ones
- `%Y` - Full year
- `%M` - Month
- `%D` - Day
- `%H` - Hour
- `%MI` - Minute
- `%S` - Second
- `%P` - AM/PM
- `%T` - Full timestamp

```python
from stamp.__fetch__ import Fetch

# Custom format
formatted = Fetch.format("Today is %M/%D/%Y at %H:%MI:%S %P")
print(formatted)
# Output: Today is 9/18/2025 at 12:5:30 pm

# Just year
year = Fetch.format("%Y")
print(year)
# Output: 2025

# ISO-like format
iso = Fetch.format("%Y-%M-%D_%H-%MI-%S")
print(iso)
# Output: 2025-9-18_12-5-30
```

### Fetch.parse(timestamp_str)
Parse timestamp string into components.

**Parameters:**
- `timestamp_str` (str): Timestamp string to parse

**Returns:** dict - Parsed components

```python
from stamp.__fetch__ import Fetch

timestamp = "ML2-CT0-ST02-M09-D18-H12-MI05-pm-S30"
parsed = Fetch.parse(timestamp)
print(parsed)
# Output:
# {
#     'millennium': 2,
#     'century': 0,
#     'sub_year_tens': 2,
#     'sub_year_ones': 5,
#     'year': 2025,
#     'month': 9,
#     'day': 18,
#     'hour': 12,
#     'minute': 5,
#     'second': 30,
#     'period': 'pm'
# }
```

### Fetch.compare(ts1, ts2)
Compare two timestamps.

**Parameters:**
- `ts1` (str): First timestamp
- `ts2` (str): Second timestamp

**Returns:** int - Comparison result
- `-1` if ts1 < ts2
- `0` if ts1 == ts2
- `1` if ts1 > ts2

```python
from stamp.__fetch__ import Fetch

ts1 = "ML2-CT0-ST02-M09-D18-H12-MI00-pm-S00"
ts2 = "ML2-CT0-ST02-M09-D18-H12-MI05-pm-S00"

result = Fetch.compare(ts1, ts2)
print(result)
# Output: -1 (ts1 is earlier)

result = Fetch.compare(ts2, ts1)
print(result)
# Output: 1 (ts2 is later)

result = Fetch.compare(ts1, ts1)
print(result)
# Output: 0 (equal)
```

### Fetch.diff(ts1, ts2)
Calculate difference between two timestamps.

**Parameters:**
- `ts1` (str): First timestamp
- `ts2` (str): Second timestamp

**Returns:** dict - Time difference

```python
from stamp.__fetch__ import Fetch

ts1 = "ML2-CT0-ST02-M09-D18-H12-MI00-pm-S00"
ts2 = "ML2-CT0-ST02-M09-D18-H12-MI05-pm-S30"

diff = Fetch.diff(ts1, ts2)
print(diff)
# Output:
# {
#     'days': 0,
#     'hours': 0,
#     'minutes': 5,
#     'seconds': 30,
#     'total_seconds': 330
# }
```

### Fetch.add(ts, days=0, hours=0, minutes=0, seconds=0)
Add time to timestamp.

**Parameters:**
- `ts` (str): Base timestamp
- `days` (int): Days to add (default: 0)
- `hours` (int): Hours to add (default: 0)
- `minutes` (int): Minutes to add (default: 0)
- `seconds` (int): Seconds to add (default: 0)

**Returns:** str - New timestamp

```python
from stamp.__fetch__ import Fetch

timestamp = "ML2-CT0-ST02-M09-D18-H12-MI00-pm-S00"

# Add 5 minutes
new_ts = Fetch.add(timestamp, minutes=5)
print(new_ts)
# Output: ML2-CT0-ST02-M09-D18-H12-MI05-pm-S00

# Add 1 hour
new_ts = Fetch.add(timestamp, hours=1)
print(new_ts)
# Output: ML2-CT0-ST02-M09-D18-H01-MI00-pm-S00

# Add 1 day, 2 hours, 30 minutes
new_ts = Fetch.add(timestamp, days=1, hours=2, minutes=30)
print(new_ts)
# Output: ML2-CT0-ST02-M09-D19-H02-MI30-pm-S00
```

### Fetch.subtract(ts, days=0, hours=0, minutes=0, seconds=0)
Subtract time from timestamp.

**Parameters:**
- `ts` (str): Base timestamp
- `days` (int): Days to subtract (default: 0)
- `hours` (int): Hours to subtract (default: 0)
- `minutes` (int): Minutes to subtract (default: 0)
- `seconds` (int): Seconds to subtract (default: 0)

**Returns:** str - New timestamp

```python
from stamp.__fetch__ import Fetch

timestamp = "ML2-CT0-ST02-M09-D18-H12-MI05-pm-S30"

# Subtract 5 minutes
new_ts = Fetch.subtract(timestamp, minutes=5)
print(new_ts)
# Output: ML2-CT0-ST02-M09-D18-H12-MI00-pm-S30

# Subtract 1 hour
new_ts = Fetch.subtract(timestamp, hours=1)
print(new_ts)
# Output: ML2-CT0-ST02-M09-D18-H11-MI05-pm-S30
```

## Timestamp Error

### TimeError

Raised for timestamp-related errors.

```python
from stamp.main import TimeError

try:
    # Some operation that fails
    pass
except TimeError as e:
    print(f"Timestamp error: {e}")
```

## Usage Examples

### Basic Usage

```python
from stamp.main import Stamp

# Get timestamp
timestamp = Stamp.stamp_()
print(f"Current time: {timestamp}")
```

### Logging with Timestamps

```python
from stamp.main import Stamp
from stamp.__fetch__ import Fetch

# Add timestamp to log
timestamp = Stamp.stamp_()
print(f"[{timestamp}] Application started")

# Format for log file
log_entry = Fetch.format("[%Y-%M-%D %H:%MI:%S] Event occurred")
print(log_entry)
# Output: [2025-9-18 12:5:30] Event occurred
```

### Calculating Duration

```python
from stamp.main import Stamp
from stamp.__fetch__ import Fetch

# Start time
start = Stamp.stamp_()

# Do some work
import time
time.sleep(2)

# End time
end = Stamp.stamp_()

# Calculate duration
diff = Fetch.diff(start, end)
print(f"Duration: {diff['total_seconds']} seconds")
```

### Timestamp in Filename

```python
from stamp.main import Stamp

# Create timestamped filename
timestamp = Stamp.stamp_()
filename = f"log_{timestamp}.txt"

with open(filename, 'w') as f:
    f.write("Log entry")
```

## Notes

- Timestamps are in local time
- Months are 1-indexed (01-12)
- Hours are 24-hour format (00-23)
- Period (am/pm) is preserved from original time
- All operations handle rollover correctly (e.g., 59 minutes + 1 minute = next hour)

---

See [Core API](core.md) for main module documentation.
See [Timestamp Examples](../examples/timestamps.md) for more examples.
