import random
import string

def generate_password(length):
    # Define characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def password_generator():
    print("Password Generator")

    # Prompt user for password length
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive length.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number for the length.")
        return

    # Generate and display the password
    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    password_generator()

