# Print()

## Format print()
### How to use the print( ) function
  code: 

```python
print("Hello")  # Hello
print("100")    # 100(String)
print("%d" % 100)   # 100(number)

print("100 + 100")    # 100 + 100(String)
print("%d" % (100 + 100))   # 200(number)
```

  output

```
Hello
100
100
100 + 100
200
```

※ The number of formats must be equal to the number of digits (or characters) after %
```python
print("%d" % (100, 200))
print("%d %d" % 100)
```
    ➔ Error Occurred   
      In the first row there is only one %d, but there are two numbers (100, 200)    
      In the second row there are two %d, but there is only one number (100)

Formats frequently used other than integer (%d)
```py
print("%d / %d = %d" % (100, 200, 0.5))
```
    ➔ 100/200=0 instead of 100/200=0.5
      The third number 0.5 is a real number (a number with a decimal point), but the way it is displayed is an integer


Format used by print()

|Format|Example of values|Explanation|
|-----|-----|-----|
|%d, %x, %o|10, 100, 1234|Integer(10진수, 16진수, 8진수)|
|%f|0.5, 1.0, 3.14|Real number (number with a decimal point)|
|%c|"b", "한"|single character|
|%s|"Hello", "abcdef", "a"|a string of one or more characters|

- Edit with %f instead of 3rd %d
```py
print("%d / %d = %5.1f" % (100, 200, 0.5))
```
```
100 / 200 =   0.5
```

### Format printing practice
```py
print("%d" % 123)
print("%5d" % 123)
print("%05d" % 123, '\n')

print("%f" % 123.45)
print("%7.1f" % 123.45)
print("%7.3f" % 123.45, '\n')

print("%s" % 'Python')
print("%10s" % 'Python')
```
output
```
123
  123
00123 

123.450000
  123.5
123.450 

Python
    Python
```

Formatting Integer Data  

    "%d"   ➔ 1 2 3                         -> sort by number of digits   
    "%5d   ➔ _ _ 1 2 3 (5 spaces secured)  -> Paste to the right to align   
    "%05d" ➔ 0 0 1 2 3 (5 spaces secured)  -> Paste to the right to align, fill in the blanks with zeros 

Formatting real data

    "%f"    ➔ 1 2 3 . 4 5 0 0 0 0             -> Output to 6 decimal places
    "%7.1f" ➔ _ _ 1 2 3 . 5 (Secure 7 spaces) -> Output only one decimal place, round to two decimal places
    "%7.3f" ➔ 1 2 3 . 4 5 0 (Secure 7 spaces) -> Print to the third decimal place, fill in the blanks to the right with zeros

> The second %7.1f means that it will reserve seven digits, including the decimal point, and occupy only one place after the decimal point.

Formatting string data

    "%s"   ➔ P y t h o n                            -> output as many digits
    "%10s" ➔ _ _ _ _ P y t h o n (Secure 10 spaces) -> right align

### Using the format( ) function
```py
print("%d %5d %05d" % (123, 123, 123))
print("{0:d} {1:5d} {2:05d}".format(123, 123, 123))
```
```
123   123 00123
123   123 00123
```

    ➔ Both rows output the same result.
      In the second line, 0, 1, and 2 in { } correspond to the 0, 1, and 2 values in format( ). 
      Remove % from %d and display as d.
      
### various escape characters
- The print( ) statement passes one line after printing the contents

```py
print('one line. and one line.')
print('one line. \nand one line')
```
```
one line. and one line.
one line. 
and one line
```

escape characters
|Escape Characters|Role|Explanation|
|-----|-----|-----|
|\n|move to new line|The effect of pressing the Enter key|
|\t|go to next tab|The effext of pressing the Tab key|
|\b|Move one space back|The effect of pressing the Backspace key|
|\\\ |print \\ ||
|\\'|print '||
|\\"|print "||

Using Escape Characters
```py
print('\npractice \nchanging the lines')
print('\tpractice \tTab key')
print("\"The effect of\" highlighting letters1")
print("\'The effect of\' highlighting letters2")
print('\\\\\\ print 3 backslash')
print(r"print \n \t \" \\ as it is")
```
```
practice 
changing the lines
	practice 	Tab key
"The effect of" highlighting letters1
'The effect of' highlighting letters2
\\\ print 3 backslash
print \n \t \" \\ as it is
```
