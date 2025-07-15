print("Name Tag Generator")

name = input("Please enter your name: ")

# Validate name input
if name.strip() == "":
    print("Invalid input. Name cannot be empty.")
else:
    print("\nGenerated Name Tag:\n")

    # Print a decorative border using range
    for _ in range(2):
        print("*" * 30)

    # Center the name within the same width
    print(name.center(30, ' '))

    for _ in range(2):
        print("*" * 30)
