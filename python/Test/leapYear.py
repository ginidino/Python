while True:
    print('Enter a year')
    year = int(input('Year: '))

    if year == '':
        break

    if (((year % 4 == 0) and (year % 100 != 0)) or ((year % 100 == 0) and (year % 400 == 0))):
        print('The year, %d is a leap year' % year)
        print()
    else:
        print('The year, %d is not a leap year' % year)
        print()