# How to use the print( ) function
print('How to use the print( ) function')
print("Hello")  # Hello
print("100")    # 100(String)
print("%d" % 100)   # 100(number)

print("100 + 100")    # 100 + 100(String)
print("%d" % (100 + 100))   # 200(number)
print()

print("%d / %d = %0.1f" % (100, 200, 0.5), '\n')

print("%d" % 123)
print("%5d" % 123)
print("%05d" % 123, '\n')

print("%f" % 123.45)
print("%7.1f" % 123.45)
print("%7.3f" % 123.45, '\n')

print("%s" % 'Python')
print("%10s" % 'Python', '\n')

# Using the format( ) function
print('Using the format( ) function')
print("%d %5d %05d" % (123, 123, 123))
print("{0:d} {1:5d} {2:05d}".format(123, 123, 123))
print()

# various escape characters
print('various escape characters')
print('one line. and one line.')
print('one line. \nand one line', '\n')

print('\npractice \nchanging the lines')
print('\tpractice \tTab key')
print("\"The effect of\" highlighting letters1")
print("\'The effect of\' highlighting letters2")
print('\\\\\\ print 3 backslash')
print(r"print \n \t \" \\ as it is")
