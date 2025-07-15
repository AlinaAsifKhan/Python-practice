print("---Even Odd Checker---")

while True:
    user_input = input("Enter a number (or 'q' to quit): ").strip().lower()

    if user_input == "q":
        print("Goodbye!")
        break

    try:
        number = int(user_input)
        if number % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
    except ValueError:
        print("Invalid input! Please enter a valid integer or 'q' to quit.")
