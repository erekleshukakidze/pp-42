frontend_skills = {"HTML", "CSS", "JavaScript", "React"}
backend_skills = {"Python", "JavaScript", "SQL", "React"}

union = frontend_skills | backend_skills
intersection = frontend_skills | backend_skills
frontend_only_difference = frontend_skills - backend_skills
symmetric_difference = frontend_skills ^ backend_skills


print(f"union: {union}")
print(f"intersection: {intersection}")
print(f"frontend_only_difference: {frontend_only_difference}")
print(f"symmetric_difference: {symmetric_difference}")