n = int(input("Enter a positive integer n: "))
tottal_sum = 0

for i in range(2, n + 1,  2):
    tottal_sum += i
print(f"sum of the even numbers from 1 to {n} is: {tottal_sum}")