# Task 8: Bill Splitter
total_bill = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people: "))

if num_people == 0:
    print("Number of people cannot be zero.")
else:
    per_person = total_bill / num_people
    print(f"Each person should pay: Rs {per_person:.2f}")