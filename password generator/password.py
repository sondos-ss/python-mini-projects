import random

def generator(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?"
    password = ''.join(random.choice(characters) for i in range(length))
    return password



if __name__ == "__main__":
    print("Welcom to password generator!")
    num = int(input("Enter the number of passwords you want to generate: "))
    length = int(input("Enter the length of the password: "))
    passwords = [generator(length) for _ in range(num)]
    print("Generated Passwords:")
    for password in passwords:
      print(password)
