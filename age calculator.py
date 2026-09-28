try:
    birth_year = int(input("Enter your birth_year: "))
    birth_year = 2026 - birth_year 
    print(birth_year)


except ValueError:
    print("Please enter only digits!")


 