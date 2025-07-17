num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        if num % 2 == 0:
            print("The number is positive and even.")
        else:
            print("The number is positive and odd.")
else:
    print("The number is negative.")

    '''git branch -M main
git push -u origin main'''