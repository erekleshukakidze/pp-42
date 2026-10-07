names = ["Laptop", "Phone", "Headphones", "Monitor"]
prices = [1200, 800, 150, 300]
ratings = [4.8, 4.5, 4.2, 4.9]

combine = list(zip(names, prices, ratings))
print(combine)

sorted_by_price = sorted(combine, key = lambda item: item[1], reverse=True)
print("Sorted by price (highest to lowest):")
print(sorted_by_price)

sorted_by_rating = sorted(combine, key=lambda item: item[2])
print("Sorted by rating(lowest to highest):")
print(sorted_by_rating)