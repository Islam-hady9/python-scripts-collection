# Strong Password Generator Script

This is a Python-based password generator that creates a secure, random password with a user-defined length. The generated password includes a mix of lowercase letters, uppercase letters, digits, and special characters to ensure a strong and secure password.

## How It Works

1. **Character Sets:** The program uses four character sets:
   - Lowercase letters (`a-z`)
   - Uppercase letters (`A-Z`)
   - Digits (`0-9`)
   - Special characters (e.g., `!@#$%^&*`)

2. **User Input:** The user is prompted to enter the desired length of the password. The program ensures that the password length is at least 6 characters.

3. **Password Generation:**
   - 30% of the password consists of lowercase letters.
   - 30% consists of uppercase letters.
   - 20% consists of digits.
   - 20% consists of special characters.
   - If the calculated percentages do not perfectly sum up to the desired length, the program adjusts the final password by adding additional random characters from the combined character sets to meet the exact length.

4. **Shuffling:** After selecting the characters, the program shuffles them to ensure the password is unpredictable.

5. **Output:** The final password is displayed to the user.

## Example Use Case

Imagine you need to create a strong password for a new online account. You can use this program to quickly generate a password that includes a secure mix of letters, digits, and special characters.

### Example:
- **Input:** `12` (as the desired password length)
- **Output:** A random password like `G6$hT1!wKp3*`

## Requirements

- Python 3.x

No external libraries are required to run this program. It uses Python's built-in `string` and `random` modules.
