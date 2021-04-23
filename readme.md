# Hybrid Logical Clock

*`Forked to provided support for Python 3.6x`*

Python implementation.

Based on:
https://www.cse.buffalo.edu/tech-reports/2014-04.pdf

Inspired by:
  * https://www.youtube.com/watch?v=iEFcmfmdh2w
  * https://github.com/adsharma/hlcpy (based on but heavily rewritten)
  * https://bartoszsypytkowski.com/hybrid-logical-clocks/



## Install
`python3.6 setup.py install`

## Use
### Import
`from hlcpy import HLC`

### Create Clock
```python
h1 = HLC()
```

### Set Clock
From current wall clock nanoseconds
```python
h1.set_nanos(int(time.time() * 1000000000))
```

From string timestamp
```python
h1.from_str('2021-04-23T15:43:55.951047936Z_0')
```

### Merge Events
Merge new timestamps as you become aware of into your hlc clock
event_timestamp can be a string or nanos
```python
h1.merge(event_timestamp)
```

### Sync Clock
Call sync to generate a new timestamp when you need to timestamp something.
This will give you your wall clock if it's greater than the hlc clock or an
incremented hlc clock if it is greater.
```python
h1.sync()
myobj = {'timestamp': str(h1), 'payload':{}}
```

