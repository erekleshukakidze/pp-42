scores = []
scores. append(45)
scores. append(88)
scores.append(92)
scores. append(60)
scores. append(75)

scores.remove(45)

average_score = sum(scores) / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

print(f"Average score: {average_score}")
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")

scores. sort()
print(f"sorted.scores: {scores}")

passed_scores = [score for score in scores if score >= 60]
print(f"Passed scores (>= 60): {passed_scores}")