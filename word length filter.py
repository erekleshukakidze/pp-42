words = ["python", "generator", "yield", "code", "ai", "developer"]

def filtered_words(word_list):
    for word in word_list:
        if len(word) > 4:
            yield word.upper()

for word in filtered_words(words):
    print(word)