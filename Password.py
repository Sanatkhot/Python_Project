import random
import string

class PasswordGenerator:
    def generate_password(self, length=12, uppercase=True, lowercase=True, numbers=True, special_chars=True):
        characters = ''

        if uppercase:
            characters += string.ascii_uppercase
        if lowercase:
            characters += string.ascii_lowercase
        if numbers:
            characters += string.digits
        if special_chars:
            characters += string.punctuation

        if not characters:
            print("Error: Please enable at least one character type.")
            return None

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

def main():
    password_generator = PasswordGenerator()

    print("Welcome to the Password Generator!\n")

    try:
        length = int(input("Enter the length of the password: "))
        uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
        special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

        generated_password = password_generator.generate_password(length, uppercase, lowercase, numbers, special_chars)

        if generated_password:
            print(f"\nGenerated Password: {generated_password}")
        else:
            print("Password generation failed. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
