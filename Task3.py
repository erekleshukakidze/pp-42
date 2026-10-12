def required_role(allowed_role="admin"):
    def decoratore_role(func):
        def wrapper(*args, **kwargs):
            user_role = kwargs.get("user_role")

            if user_role == allowed_role:
                return func(*args, **kwargs)
            else:
                print("Permission Denied: User is not an admin.")
                return None

        return wrapper
    return decoratore_role

@required_role(allowed_role="admin")
def delete_database(user_role):
    print("Database deleted successfully!")

print("---Test 1: Admin ---")
delete_database(user_role="admin")

print("\n---Test 2: Guest ---")
delete_database(user_role="guest")