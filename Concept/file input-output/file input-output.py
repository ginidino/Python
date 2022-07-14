infile = open("/Users/injaelee/Desktop/data1.txt", "r", encoding="utf-8")

inStr = infile.readline()
print(inStr, end="")

inStr = infile.readline()
print(inStr, end="")

inStr = infile.readline()
print(inStr, end="")
print()
infile.close()

infile = open("/Users/injaelee/Desktop/data2.txt", "r", encoding="utf-8")

while True:
    inStr = infile.readline()
    if inStr == "":
        break
    print(inStr, end="")
print()
infile.close()

print()
inList = []
inStr = ""
infile = open("/Users/injaelee/Desktop/text1.txt", "r", encoding="utf-8")
'''inList = infile.readlines()
print(inList)'''
inList = infile.readlines()
for inStr in inList:
    print(inStr, end="")

infile.close()

inList = []
inStr = ""

fName = input('Enter the file name: ')
inFp = open(fName, "r", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList:
    print(inStr, end="")

inFp.close()

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

outfile = open("/Users/injaelee/Desktop/data2.txt", "w", encoding="utf-8")

while True:
    outStr = input('Enter content : ')
    if outStr != "":
        outfile.write(outStr + "\n")
    else:
        break

outfile.close()
print('----The file was written normally----')

inCont = ""

inF = open("/Users/injaelee/Desktop/text1.txt", "r", encoding="utf-8")
outF = open("/Users/injaelee/Desktop/text2.txt", "w", encoding="utf-8")

inLists = inF.readlines()
for inCont in inLists:
    outF.writelines(inCont)

inF.close()
outF.close()
print('The file was copied normally.')
print()

ord('a')
chr(97)
print(ord('a'))
print(chr(97))
print()

num = ord('a')
chr(num + 100)
print(chr(num + 100))
print()

infileName = None
outfileName = None
i = 0

security = input('choose from 1. Encryption 2. Password Interpretation: ')
infileName = input('Enter the input file name: ')
outfileName = input('Enter the output file name: ')

if security == "1":
    secu = 100
elif security == "2":
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
