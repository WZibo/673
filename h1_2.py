def is_palindrome(s):
    s = s.replace(" ", "").lower()
    # Compares whether the reverse order of string is the same as s
    return s == s[::-1]


while 1:
    user_input = input("Enter a string:")

    # Check if it is palindrome
    if is_palindrome(user_input):
        print(f"The string '{user_input}' is a palindrome")
    else:
        print(f"The string '{user_input}' is not a palindrome")

    # Typing q to exit program
    if user_input == 'q':
        print("Program exits.")
        break

