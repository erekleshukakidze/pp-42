text = input("Enter a string: ")
result = ""

for chair in text:
    if chair.isdigit():
      continue 
    result += chair

print(result)