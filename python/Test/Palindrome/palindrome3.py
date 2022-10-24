while True:
    word = input('Enter the word: ')
    check = True

    if word == '':
        break

    for i in range(len(word)):
        if word[i] != word[len(word) - i - 1]:
            check = False

    if check == True:
        print("The text, %s, is a palindrome!" % word)
    else:
        print("The text, %s, is not a palindrome!" % word)
