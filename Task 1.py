def make_counter(start_value=0):
    count = start_value

    def wrapper():
        nonlocal count
        count += 1
        return count
    return wrapper

counter = make_counter(start_value=10)
print(counter())
print(counter())
print(counter())