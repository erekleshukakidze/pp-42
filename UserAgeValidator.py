try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
    elif age < 18:
        raise ValueError("User must be at least 18 to register.")

except ValueError as e:
    print(e)

finally: 
    print("registration procces completed")

