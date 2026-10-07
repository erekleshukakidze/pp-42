score = [45, 82, 67, 38, 90, 55, 72]
filtered_score = list(filter(lambda score: score >=50, score))
mapped_score = list(map(lambda score: 100 if score + 5 > 100 else score + 5, filtered_score)) 

print(filtered_score)
print(mapped_score)



