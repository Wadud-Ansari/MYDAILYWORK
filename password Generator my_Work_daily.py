import random
import string

def generate_password(length):
    if length < 4:
        return "Error: Password length should be at least 4."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 4:
                print("Password length should be at least 4.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        password = generate_password(length)
        print(f"Generated Password: {password}")

        another_password = input("Do you want to generate another password? (yes/no): ")
        if another_password.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
