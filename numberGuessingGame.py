import random
print("----Number Guessing Game----")

while True:
    user_input = input("Press Y to proceed and see the instructions: ")

    if user_input.lower() == 'y':
        print("---Instructions---")
        print("1. Enter any number between 1 and 100.")
        print("2. If the entered number is correct, you win!")
        print("3. If the number is higher or lower, you will be informed and given another chance to guess.")

        start_game = input("Press Y to start the game: ")
        if start_game.lower() == 'y': 
            secret_number = random.randint(1, 100)
            flag = True
            maxAttempts = 10
            count = 1

            while flag and count <= maxAttempts:
                try:
                    print(f"Attempt Number: {count}/{maxAttempts}")
                    entered_number = int(input("Enter a number to guess: "))

                    if entered_number == secret_number:
                        print(f" Congratulations! You have won in {count} attempts!")
                        flag = False
                    elif entered_number > secret_number:
                        print("------------")
                        print("Too High.")
                        print("------------")
                    else:
                        print("------------")
                        print("Too Low.")
                        print("------------")

                    if flag:
                        count += 1

                except ValueError:
                    print("Enter a valid integer.")

            if flag:
                print(f"Game Over! The correct number was {secret_number}.")

        else:
            print("You chose not to start the game. Goodbye.")
    else:
        print("You chose not to proceed. Goodbye.")

    playAgain = input("\nDo you want to play again? (Y/N): ")
    if playAgain.lower() != 'y':
        print("Thanks for playing. Goodbye!")
        break
