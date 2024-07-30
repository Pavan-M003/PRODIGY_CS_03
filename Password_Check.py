# Password Complexity Checker
import string

def pswd_check():
    password = input("Enter your password: ")
    strength = 5

    lower_count = upper_count = num_count = special_count = 0

    for i in list(password):
        if i in string.ascii_lowercase:
            lower_count += 1
        elif i in string.ascii_uppercase:
            upper_count += 1
        elif i in string.digits:
            num_count += 1
        else:
            special_count += 1

    if len(password) < 8:
        print("\nPassword must contain atleast 8 charecters.")
        strength -= 1
    if lower_count <= 0:
        print("\nYour password doesn't contain any Lowercase latters [a-z],\nUse atleast one lowercse letter.")
        strength -= 1
    if upper_count <= 0:
        print("\nYour password doesn't contain any Uppercase latters [A-Z],\nUse atleast one Uppercase letter.")
        strength -= 1
    if num_count <= 0:
        print("\nYour password doesn't contain any integer [0-9],\nUse atleast one number")
        strength -= 1
    if special_count <= 0:
        print("\nYour password doesn't cantain any special charecters [@ # $ % & * !],\nUse atleast one speacial charecter")
        strength -= 1
    if strength == 5:
        print("\nPassword is Strong :)")


# Main Function
pswd_check()
