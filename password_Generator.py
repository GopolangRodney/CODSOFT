import string
import random

def generate_password(length):
    characters_combination = string.ascii_letters + string.digits + string.punctuation

    
    user_password = ''.join(random.choice(characters_combination) for _ in range(length))
    
    return user_password 

length = int(input("Enter the length of the password: "))


while length < 5:
    print("Password length must be 5 characters or more.")
    length = int(input("Enter the length of the password: "))


password = generate_password(length)
print(f"Your password is: {password}")
