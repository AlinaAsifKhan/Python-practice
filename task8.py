def bill_splitter():
    print("\n--- Bill Splitter ---\n")
    
    try:
        total_bill = float(input("Enter the total bill amount: Rs "))
        num_people = int(input("Enter the number of people sharing the bill: "))

        if num_people <= 0:
            print("Error: The number of people must be greater than zero.")
        else:
            per_person = total_bill / num_people
            print(f"\nEach person should pay: Rs {per_person:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values only.")

def main():
    print("Welcome to the Bill Splitting System")
    bill_splitter()
    print("\nThank you for using the system.")

if __name__ == "__main__":
    main()
