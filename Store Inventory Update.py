inventory = ["apple", "banana", "orange", "apple", "kivi", "apple"]
new_items = ["mango", "grape"]

apple_count = inventory.count("apple")
print(f"Count of 'apple': {apple_count}")

orange_index = inventory. index("orange")
print(f"Index of first 'orange': {orange_index}")

inventory.extend(new_items)
print(f"Updated inventory: {inventory}")

print(f"Rreversed inventory: {inventory[::-1]}")