print(" Even & Odd Number Checker ")


count = int(input("How many numbers do you want to check? "))

even_count = 0
odd_count = 0

for i in range(1, count + 1):
    try:
        number = int(input(f"Enter number {i}: "))
        
        if number % 2 == 0:
            print(f"{number} is Even.\n")
            even_count += 1
        else:
            print(f" {number} is Odd.\n")
            odd_count += 1

    except ValueError:
        print("Invalid input. Please enter an integer.\n")

# summary
print(" Summary:")
print(f"Total Even Numbers: {even_count}")
print(f"Total Odd Numbers: {odd_count}")
