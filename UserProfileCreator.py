

def create_user_profile(first_name, last_name, role="student", is_active = True):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "role": role,
        "is_active": is_active
    }
f_name = input("Enter your first name: ").capitalize() .strip()
l_name = input("Enter your last name: ").capitalize() .strip()

profile = create_user_profile(f_name, l_name)
print(profile)