def sum_of_digits_single(n):
    if n < 10:
        return n
    return (n % 10) + sum_of_digits_single(n // 10)


def sum_of_digits(*args):
    return [sum_of_digits_single(num) for num in args]

print(sum_of_digits(1234, 567, 89))
