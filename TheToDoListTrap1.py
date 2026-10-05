def add_task(task_name, task_list=[]):
    task_list.append(task_name)
    return task_list

print(add_task("task 1"))
print(add_task("task 2"))
print(add_task("task 3"))

#ეს სია არის ერთხელ შექმნილი ამიტომ მოცემულ არგუმენტს შემდგომი ელემენტები უბრალოდ ემატება და ერთ სიაში ექცევა
    
