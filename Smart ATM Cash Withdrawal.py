correct_pin = 3550
balance = 67000

entered_pin = int(input("Enter your PIN: "))

if entered_pin == correct_pin:
    requested_amount = float(input("Enter amount to withdraw: "))

    if requested_amount <= balance:
        balance -= requested_amount
        print(f"Withdrawal successful! Remaining balance: ${balance: .2f}")
    else:
        print("Amount of your balance isn't enough. ")
else:
    print("Incorrect PIN. Access Denied")
