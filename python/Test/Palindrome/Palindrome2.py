word = input('Enter the word: ')

def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            return False
    return True

if is_palindrome(word):
    print("The text, " + word + ", is a palindrome!")
else:
    print("The text, " + word + ", is not a palindrome!")