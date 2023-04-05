# frange: An alternative to range with support for floats

## Requirements
Python 3.6>=

## Installation
```bash
# Linux
python3 -m pip install frange
# Windows
python -m pip install frange
```

## Usage
```python
import frange

frange.frange(10.0) # frange(0, 10, 1)
frange.frange(0.5, 10.5) # frange(0.5, 10.5, 1)
len(frange.frange(0.5, 10.5)) # 10
frange.frange(0.5, 10.5)[0] # 0.5
frange.frange(0.5, 10.5)[-1] # 9.5
frange.frange(0.5, 10.5)[1:5] # frange(1.5, 5.5)
for i in frange.frange(0.5, 10.5):
    print(i) 
"""
0.5
1.5
2.5
3.5
4.5
5.5
6.5
7.5
8.5
9.5
"""
```

### Monkey patching the built-in range function
```python
from frange import frange as range
```

## To Do
* [ ] Rewrite in C