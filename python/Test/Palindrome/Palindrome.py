while True:
    word = input('Enter the word: ')
    check = True

    if word == '':
        break

    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            check = False

    if check == True:
        print("The text, " + word + ", is a palindrome!" + '\n')
    else:
        print("The text, " + word + ", is not a palindrome!" + '\n')
