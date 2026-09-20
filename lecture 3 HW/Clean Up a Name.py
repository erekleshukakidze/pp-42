text = "My favorite thing is Python"
print(text.replace("thing","language"))
print(text.find("Python"))
print(text[12:])


first_name = input("First name: ")
last_name = input("Last name: ")

first_name = first_name.strip().capitalize()
last_name = last_name.strip().capitalize()
print(first_name, last_name)