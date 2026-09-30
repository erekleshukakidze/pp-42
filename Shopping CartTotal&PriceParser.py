try:
    price = float(input("Please enter the price: "))
    quantity = int(input("please enter the quantity: "))
    total = price * quantity
    print(f"Your total is {total}")

except ValueError:
    print("Error:Both price and quantity must be valid numbers!")

else:
    print(f"The total cost is: ${total:.2f}")



