user_name = input("Please enter your User Name :\n")
password = input("Plaese enter your Password :\n")

# print("Hey", user_name + ",", "your password", "*"*12, "is", len(password), "letters long.")

print(f"""Hey {user_name}, your password {"*" * len(password)} is {len(password)} letters long.""")