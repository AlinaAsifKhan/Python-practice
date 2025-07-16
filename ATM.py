'''2. Create a basic ATM-like system with a preset balance.
Features to include:

- Check current balance
- Withdraw money (only if enough balance)
- Deposit money
- Exit the program
- Use one list or variable to track the balance
- Write separate functions for each operation
'''

def check_balance(balance):
    print(f"Your balance is Rs. {balance}")

def deposit_money(balance):
    while True:
        try:
            deposit = int(input("Enter the amount you want to deposit: "))
            if deposit > 0:
                balance += deposit
                print(f"Your new balance is: Rs.{balance}")
                break 
            else:
                print("Amount must be positive. Try again.")
        except ValueError:
            print("Enter a valid amount. Try again.")
    return balance

def withdraw_money(balance):
    while True:
        try:
            withdrawl = int(input("Enter the amount you want to withdraw: "))
            if withdrawl <= 0:
                print("Amount must be positive. Try again.")
            elif balance >= withdrawl:
                balance -= withdrawl
                print(f"Rs.{withdrawl} has been withdrawn. Remaining balance is Rs.{balance}.")
                break 
            else:
                print("Balance is insufficient.")
                break 
        except ValueError:
            print("Invalid amount. Try again.")
    return balance

# Initial balance
balance = 1000

print("----ATM----")
print("1. Check Balance.")
print("2. Deposit Money.")
print("3. Withdraw Money.")
print("4. Exit.")

while True:
    choice = input("Enter your choice from options: ")
    if choice == '1':
        check_balance(balance)
    elif choice == '2':
        balance = deposit_money(balance)
    elif choice == '3':
        balance = withdraw_money(balance)
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Please enter a valid option.")
