import string
import random

def generate_password(characters_number):
    # Define character sets
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    # Shuffle the character sets
    random.shuffle(lowercase)
    random.shuffle(uppercase)
    random.shuffle(digits)
    random.shuffle(punctuation)

    # Calculate the number of characters for each part
    num_lower_upper = round(characters_number * 0.3)
    num_digits_punctuation = round(characters_number * 0.2)

    # Generate the password by selecting characters from each set
    password = (
        lowercase[:num_lower_upper] +
        uppercase[:num_lower_upper] +
        digits[:num_digits_punctuation] +
        punctuation[:num_digits_punctuation]
    )

    # If the total length is not equal to characters_number, add random characters to meet the exact length
    while len(password) < characters_number:
        password.append(random.choice(lowercase + uppercase + digits + punctuation))

    # Shuffle the final password and join it into a string
    random.shuffle(password)
    return "".join(password)

def get_password_length():
    while True:
        try:
            characters_number = int(input("How many characters for the password? (min 6): "))
            if characters_number < 6:
                print("You need at least 6 characters. Please try again.")
            else:
                return characters_number
        except ValueError:
            print("Invalid input. Please enter numbers only.")

# Main execution
if __name__ == "__main__":
    password_length = get_password_length()
    password = generate_password(password_length)
    print("The generated password is:\t" + password)