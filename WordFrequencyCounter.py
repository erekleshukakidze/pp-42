words = ["apple", "banana", "apple", "cherry", "banana", "apple", "orange"]
word_counts = {}

for w in words:
    word_counts[w] = word_counts.get(w, 0) + 1

print("word count:", word_counts)

print("words that appear more than ones: ")
for word, count in word_counts.items():
    if count > 1:
        print(f"{word}: {count}")

