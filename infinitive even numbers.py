def even_numbers(n=0):
    while True:
        yield n
        n += 2

count = 0
for n in even_numbers(n=0):
    print(n)
    count += 1
    if count >= 10:
        break    
