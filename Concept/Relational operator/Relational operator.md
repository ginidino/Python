# Relational operator
### Relational operator
- To compare if something is greater, less than, or equal, the result is True or False
- Mainly used in conditional statements (if ) or loop statements (for, while)
- a < b = True or False

### Types of Relational Operators
|Relational Operators|Meaning|Explanation|
|------|---|---|
|==|equal|True if the two values are the equal|
|!=|not equal|True if the two values are different|
|>|greater|True if the left side is greater|
|<|less|True if left is less than|
|>=|greater than or equal to|True if left is greater than or equal to|
|<=|less than or equal to|True if left is less than or equal to|

### Examples of Relational Operators
```py
a = 100
b = 200
print('a == b:', a == b)
print('a != b:', a != b)
print('a > b:', a > b)
print('a < b:', a < b)
print('a >= b:', a >= b)
print('a <= b:', a <= b)
```
```
a == b: False
a != b: True
a > b: False
a < b: True
a >= b: False
a <= b: True
```

    Error occurs → When using the relational operator == to compare a and b, if only one = is used
      a = b means substitute the value of b for a, not the relational operator
