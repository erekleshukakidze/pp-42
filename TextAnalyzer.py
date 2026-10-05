def analyze_text(text, min_length=3, ignore_stopwords=None):
    if ignore_stopwords is None:
        ignore_stopwords = set()

    words = text.split()
    valid_words_count = 0
    for word in words:
        if len(word) >= min_length and word not in ignore_stopwords:
            valid_words_count +=1

    return valid_words_count

sample_text = "Python is an amazing programming language for beginners"

print(analyze_text(sample_text))

stopwords = {"Python", "for"}
print(analyze_text(sample_text, min_length=5, ignore_stopwords=stopwords))