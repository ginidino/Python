# A program that saves ID and password for login and registers as a member
# The ID is reflected in the txt file name, and the password is stored in the txt file.
print('sign up')
print('Membership registration in progress')

user_id = input("ID: ")
user_password = input("PASSWORD: ")

with open(f"/Users/injaelee/Desktop/userID_{user_id}.txt", "w") as f:
    f.writelines(user_password)

print('Membership registration is complete')
f.close()
print()

# A program to log in by finding an ID and password from the saved member list
import os

print('sign in')
print('login screen')

user_ID = input('ID: ')
user_PW = input('PASSWORD: ')

user_ID_file = "/Users/injaelee/Desktop/user_{}.txt".format(user_ID)

if os.path.exists(user_ID_file):
    user_data = open(user_ID_file, "r")
    user_data2 = user_data.read()

    if user_PW == user_data2:
        print('Login was successful')
    else:
        print('Login failed')
    user_data.close()
else:
    print('This is an unregistered ID')