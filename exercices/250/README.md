# Square Drawing

Introduces: functions, print.

## Instructions

Write a script named `solution.py` that prints this square:

```
+ - - - -+ - - - -+
|        |        |
|        |        |
|        |        |
|        |        |
+ - - - -+ - - - -+
|        |        |
|        |        |
|        |        |
|        |        |
+ - - - -+ - - - -+
```

You should not try to print string of a length superior to 5.

## Advice

Use functions than call functions

```python
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)
```
## References
 - [functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
 - [print](https://docs.python.org/3/tutorial/index.html)
