import random
import string


# Function 1: Get valid password length
def get_password_length():

    while True:
        try:
            length = int(input("\nEnter password length: "))

            if length <= 0:
                print("Error: Password length must be greater than zero.")
            else:
                return length

        except ValueError:
            print("Invalid input! Please enter a whole number.")


# Function 2: Get user preferences
def get_preferences():

    while True:

        letters = input("Include letters? (yes/no): ").strip().lower()
        numbers = input("Include numbers? (yes/no): ").strip().lower()
        symbols = input("Include symbols? (yes/no): ").strip().lower()

        # Validate yes/no answers
        if letters not in ("yes", "no"):
            print("Please answer yes or no.")
            continue

        if numbers not in ("yes", "no"):
            print("Please answer yes or no.")
            continue

        if symbols not in ("yes", "no"):
            print("Please answer yes or no.")
            continue

        # Check if at least one type is selected
        if letters == "no" and numbers == "no" and symbols == "no":
            print("\nPlease select at least one character type!")
            continue

        return letters, numbers, symbols


# Function 3: Generate password
def generate_password(length, letters, numbers, symbols):

    characters = ""

    # Add selected character types
    if letters == "yes":
        characters += string.ascii_letters

    if numbers == "yes":
        characters += string.digits

    if symbols == "yes":
        characters += string.punctuation

    # Generate random password
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


# Function 4: Main program
def main():

    print("=" * 40)
    print("       RANDOM PASSWORD GENERATOR")
    print("=" * 40)

    while True:

        # Step 1: Get password length
        length = get_password_length()

        # Step 2: Get user preferences
        letters, numbers, symbols = get_preferences()

        # Step 3: Generate password
        password = generate_password(
            length, letters, numbers, symbols
        )

        # Step 4: Display password
        print("\n" + "=" * 40)
        print("Your Generated Password:", password)
        print("Password Length:", len(password))
        print("=" * 40)

        # Step 5: Ask user to generate again
        again = input("\nGenerate another password? (yes/no): ")
        again = again.strip().lower()

        while again not in ("yes", "no"):
            again = input("Please enter yes or no: ").strip().lower()

        if again == "no":
            print("\nThank you for using Password Generator!")
            break


# Start the program
if __name__ == "__main__":
    main()
