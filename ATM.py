pin = "1234"

user_pin = input("Enter PIN: ")

if user_pin == pin:
    print("Login Successful!")

    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")

    bal = 5000
    ch = input("Choose: ")

    if ch == "1":
        print("Balance =", bal)

    elif ch == "2":
        amt = int(input("Amount: "))
        if amt <= bal:
            bal -= amt
            print("Withdraw Successful. New Balance =", bal)
        else:
            print("Not enough balance.")

    elif ch == "3":
        amt = int(input("Amount: "))
        bal += amt
        print("Deposit Successful. New Balance =", bal)

    else:
        print("Invalid Option")

else:
    print("Wrong PIN!")

