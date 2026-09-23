age = int(input("Enter your age: "))
if age < 0:
    print("Your age is invaled. ")
elif age < 5:
    print("Your ticket price is free. ")
elif age <= 12:
    print("Your ticket  price is $8. ")
elif age <= 64:
    print("Your ticket price is $15. ")
else:
    print("Your ticket price is $10. ")
     