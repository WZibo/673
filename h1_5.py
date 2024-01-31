while 1:
    user_input = input("Enter year: ")

    # Check if the input is a non-negative integer
    if user_input.isdigit():
        year = int(user_input)

        # Exclude 0
        if year > 0:
            # Determine whether the conditions for leap year are met
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
            break
        else:
            print("The year entered should be greater than 0.")
    else:
        print("Please enter a valid year.")