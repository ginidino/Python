# File input-output

## File Input/Output Process
### Understanding file input and output
Input from the keyboard is called standard input, and output to the monitor is called standard output. The keyboard and monitor combined are called console.    

input() function and print() function are input/output of keyboard and monitor   
read(), readline(), and readlines() read the contents of a file   
  - read(): Reads the entire file as a string. Binary files (such as picture files) can also be read.
  - readline(): reads one line at a time
  - readlines(): Reads the entire file line by line and creates a list   

write(), writelines() writes content to a file
  - write() can also use binary files
  - writelines() only supports text
 
### File input/output basic process
Step 1: Open the file
  - In the open( ) function, specify the file name and whether to read or write.
  - The last parameter of the open( ) function is called Mode.

        For reading: variable name = open("file name", "r")
        For writing: variable name = open("file name", "w")

|file open mode|meaning|
|---|---|
|skip|same as r|
|r|Read Mode, Default value|
|w|Write Mode, If the file already exists, it will be overwritten.|
|r+|Read/Write Mode|
|a|Write Mode. If the file already exists, it is written over. Abbreviation for append|
|t|Text Mode. Process text files. Default value|
|b|Binary Mode. Process binary files (=binary files)|

Step 2: File Processing
  - Can write data to or read data from a file 

Step 3: Close the file

    variable name.close()
    
## Text file input/output method
### input from file
file -> File input related(`read()`, `readline()`, `readlines()`) -> Python Program -> Output related(`print()`) -> Standard Output Device

Reading one line at a time using the - readline() function
content of file
```
파이썬
python
University of Leicester
레스터 대학
University of Birmingham
버밍엄 대학
```
```py
infile = open("/Users/injaelee/Desktop/data1.txt", "r", encoding="utf-8")

inStr = infile.readline()
print(inStr, end="")

inStr = infile.readline()
print(inStr, end="")

inStr = infile.readline()
print(inStr, end="")

infile.close()
```
```
파이썬
python
University of Leicester
```
> The code above can only handle 3 lines of the file's contents. Must be modified to read all rows
> In the save window, the encoding must be selected as UTF-8 so that Korean is not broken in Python.

```py
infile = open("/Users/injaelee/Desktop/data1.txt", "r", encoding="utf-8")

while True:
    inStr = infile.readline()
    if inStr == "":
        break
    print(inStr, end="")

infile.close()
```
```
파이썬
python
University of Leicester
레스터 대학
University of Birmingham
버밍엄 대학
```

Read all at once - the readlines( ) function stores the contents of a file as a whole in a list
```py
infile = open("/Users/injaelee/Desktop/data1.txt", "r", encoding="utf-8")
inList = infile.readlines()
print(inList)

infile.close()
```
```
['파이썬\n', 'python\n', 'University of Leicester\n', '레스터 대학\n', 'University of Birmingham\n', '버밍엄 대학']
```
-> Modify the contents of the file to be output one line at a time
```py
inList = []
inStr = ""
infile = open("/Users/injaelee/Desktop/data1.txt", "r", encoding="utf-8")
inList = infile.readlines()
for inStr in inList:
    print(inStr, end="")

infile.close()
```
```
파이썬
python
University of Leicester
레스터 대학
University of Birmingham
버밍엄 대학
```
Outputs the contents of the specified file to the screen

content of text1.txt
```
if (3 > 4) {
System.out.println ("3 > 4.");
System.out.println ("Looks like we’re in trouble.");
} else
System.out.println ("OK");
```
```py
inList = []
inStr = ""

fName = input('Enter the file name: ')
inFp = open(fName, "r", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList:
    print(inStr, end="")

inFp.close()
```
```
Enter the file name: /Users/injaelee/Desktop/text1.txt
if (3 > 4) {
System.out.println ("3 > 4.");
System.out.println ("Looks like we’re in trouble.");
} else
System.out.println ("OK");
```

Error handling when opening files
- Avoid errors using os.path.exists(filename)
```py
import os.path

inList = []
inStr = ""

fName = input('Enter the file name: ')

if os.path.exists(fName):
    inFile = open(fName, "r", encoding="utf-8")

    inList = inFile.readlines()
    for inStr in inList:
        print(inStr, end="")

    inFile.close()
else:
    print('%s There is no file' % fName)
```
```
Enter the file name: /Users/injaelee/Desktop/txt1.txt
/Users/injaelee/Desktop/txt1.txt There is no file
```

### Output using a file
Standard input device -> input related(`input()`) -> Python Program -> file output related(`write()`, `writelines()`) -> File

Write to file one line at a time
- A program that uses the input( ) function repeatedly and ends writing to a file if you press `Enter` without inputting anything

```py
outfile = open("/Users/injaelee/Desktop/data2.txt", "w", encoding="utf-8")

while True:
    outStr = input('Enter content : ')
    if outStr != "":
        outfile.write(outStr + "\n")
    else:
        break

outfile.close()
print('----The file was written normally----')
```
```
Enter content : python
Enter content : university of leicester
Enter content : university of birmingham
Enter content : 
----The file was written normally----
```

Copy the given file to create one identical file

File input and file output for implementing the copy (cp on Mac) command   
File -> File input related(`read()`, `readline()`, `readlines()`) -> Python Program -> file output related(`write()`, `writelines()`) -> File
```py
inCont = ""

inF = open("/Users/injaelee/Desktop/text1.txt", "r", encoding="utf-8")
outF = open("/Users/injaelee/Desktop/text2.txt", "w", encoding="utf-8")

inLists = inF.readlines()
for inCont in inLists:
    outF.writelines(inCont)

inF.close()
outF.close()
print('The file was copied normally.')
```

## Complete file encryption and decryption programs
- ord() function: returns the unique number of a character
- chr() function returns the character corresponding to a number
```py
ord('a')
chr(97)
```
```
97
a
```
- Add 100 to the number in 'a' to encrypt
```py
num = ord('a')
chr(num + 100)
```
```
Å
```
```py
security = input('choose from 1. Encryption 2. Password Interpretation: ')
infileName = input('Enter the input file name: ')
outfileName = input('Enter the output file name: ')

if security == '1':
    secu = 100
elif security == '2':
    secu = -100

inFile = open(infileName, "r", encoding="utf-8")
outFile = open(infileName, "w", encoding="utf-8")

while True:
    inString = inFile.readline()
    if not inString:
        break

    outString = ""
    for i in range(0, len(inString)):
        char = inString[i]
        charNum = ord(char)
        charNum += secu
        char2 = chr(charNum)
        outString += char2

    outFile.write(outString)

outFile.close()
inFile.close()
print(' %s ---> %s Conversion complete' % (infileName, outfileName))
```

