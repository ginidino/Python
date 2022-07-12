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
