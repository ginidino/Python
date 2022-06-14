# Lgical Operator

### Types of Lgical Operator
|Lgical Operator|Meaning|Explanation|Usage example|
|------|---|---|---|
|and|~이고, AND|Both must be true|(a>100) and (a<200)|
|or|~이거나, OR|true even if only one of the two is true|(a==100) or (a==200)|
|not|~아니다, NOT|false if true, true if false|not(a<100)|

### Truth Table
|A|B|A and B|A or B|not A|
|---|---|---|---|---|
|True|True|True|True|False|
|True|False|False|True|False|
|False|True|False|True|True|
|False|False|False|False|True|

### Example of Lgical Operator
```py
a = 99
print('(a>100) and (a<200):', (a > 100) and (a < 200))
print('(a>100) or (a<200):', (a > 100) or (a < 200))
print('not(a==100):', not(a == 100))
```
```
(a>100) and (a<200): False
(a>100) or (a<200): True
not(a==100): True
```
