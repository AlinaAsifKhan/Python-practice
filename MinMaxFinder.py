'''3. Min-Max Finder; Let the user enter multiple numbers and show the highest and lowest.

Features to include:
- Ask the user how many numbers they want to enter
- Collect numbers into a list
- Find the maximum and minimum values
- Show both results
- Use a function to do the checking'''

def find_min_max(numbers):
    return min(numbers), max(numbers)


print("---Min-Max Finder---")
numbers = []

try:
    count = int(input("How many numbers do you want to enter? "))
    if count <= 0:
        print("Please enter a positive number.")
    else:
        for i in range(count):
            while True:
                try:
                    num = float(input(f"Enter number {i+1}: "))
                    numbers.append(num)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        
        # Get min and max using the function
        minimum, maximum = find_min_max(numbers)
        print(f"\nNumbers entered: {numbers}")
        print(f"Minimum value: {minimum}")
        print(f"Maximum value: {maximum}")

except ValueError:
    print("Invalid input. Please enter a number for the count.")
