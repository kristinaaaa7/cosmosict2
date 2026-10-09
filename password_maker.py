
import secrets
import string

def generate_password(length, use_numbers, use_symbols):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()-_=+?"

    characters = letters
    password = []

    # Ensure required character types are included
    password.append(secrets.choice(string.ascii_lowercase))
    password.append(secrets.choice(string.ascii_uppercase))

    if use_numbers:
        characters += numbers
        password.append(secrets.choice(numbers))

    if use_symbols:
        characters += symbols
        password.append(secrets.choice(symbols))

    # Fill the remaining password length
    for i in range(length - len(password)):
        password.append(secrets.choice(characters))

    # Shuffle the characters securely
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


print("===== ADVANCED PASSWORD GENERATOR =====")

length = int(input("Enter password length (minimum 8): "))

if length < 8:
    print("Password must be at least 8 characters!")
else:
    numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    symbols = input("Include symbols? (yes/no): ").lower() == "yes"

    password = generate_password(length, numbers, symbols)

    print("\nYour generated password is:", password)
    print("Password length:", len(password))



