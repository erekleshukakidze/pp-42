class User:
    status = "Active"

    def __init__(self,username, email, age) -> None:
        self.username = username
        self.email = email
        self.age = age
        
    def get_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Status: {self.status}")
    
    

customer1 = User("Eke", "eke@gmail.com", 17)
customer2 = User("Nika", "nika@gmail.com", 17)

customer1.get_info()
print("="*20)
customer2.get_info()