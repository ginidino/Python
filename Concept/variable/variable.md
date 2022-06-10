# variable
### Declaration of a variable
Variable is the memory space for storing a value

The most frequently used variable
```py
intVar, boolVar, floatVar, strVar = 0, True, 0.0, ""
```

### The type( ) function
The type( ) function is a function that checks the type of a variable
```py
type(intVar), type(boolVar), type(floatVar), type(strVar)
print(type(intVar),', ', type(boolVar),', ', type(floatVar),', ', type(strVar))
```
print result
```
<class 'int'> ,  <class 'bool'> ,  <class 'float'> ,  <class 'str'>
```
In Python, the data type of a variable is a flexible structure that can change whenever a value is put in.

    myVar = 100 ➔ Create an integer variable
    type(myVar) ➔ print <class 'int'> 
    myVar = 100.0 ➔ Changed to real variable at this moment
    type(myVar) ➔ print <class 'float'>
    
### How to put a value in a variable
```py
boolVar = False
intVar = 100
floatVar = 123.45
strVar = 'Hello'
```
```
False 100 123.45 Hello 
```

### Putting the value of a variable into a variable
```py
print('Putting the value of a variable into a variable')
var2 = 200
var1 = var2
print('var1: ', var1)
print('var2: ', var2)
```

```
var1:  200
var2:  200
```

### Put the calculation result into a variable
```py
var3 = 100 + 100
print('var3: ', var3)
```

```
var3:  200
```

### Putting calculations of variables and numbers into variables
```py
var4 = var1 + 100
print('var4: ', var4)
```

```
var4:  300 
```

### How to substitute consecutive values
```py
var5 = var6 = var7 = var8 = 100
print('var5: ', var5)
print('var6: ', var6)
print('var7: ', var7)
print('var8: ', var8)
```

```
var5:  100
var6:  100
var7:  100
var8:  100
```

### A method of substituting calculation results into own values
```py
val1 = var1 + 200
print('var1: ', var1)
```

```
var1:  200
```

### Location of substitution operators and variables
    wrong sentence
    10 = 100
    
    correct sentence
    Declare a variable on the left
    variable = 100
