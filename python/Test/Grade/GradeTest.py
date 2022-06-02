while True:
    grade = int(input('Type the points [0-60]: '))

    if grade == -1:
        break

    if grade < 30:
        print('Grade: failed')
    elif 29 < grade < 35:
        print('Grade: 1')
    elif 34 < grade < 40:
        print('Grade: 2')
    elif 39 < grade < 45:
        print('Grade: 3')
    elif 44 < grade < 50:
        print('Grade: 4')
    else:
        print('Grade: 5')
