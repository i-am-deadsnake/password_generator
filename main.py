import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    """
    Generate a random password based on specified parameters.

    Args:
        length (int): Length of the password.
        use_uppercase (bool): Include uppercase letters.
        use_digits (bool): Include digits.
        use_special_chars (bool): Include special characters.

    Returns:
        str: Generated password.
    """
    chars = get_character_set(use_uppercase, use_digits, use_special_chars)
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def get_character_set(use_uppercase=True, use_digits=True, use_special_chars=True):
    """
    Get the character set based on user preferences.

    Args:
        use_uppercase (bool): Include uppercase letters.
        use_digits (bool): Include digits.
        use_special_chars (bool): Include special characters.

    Returns:
        str: Combined character set.
    """
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation
    return chars

def get_user_input():
    """
    Get user input for password generation parameters.

    Returns:
        tuple: Length and boolean values for uppercase, digits, and special characters.
    """
    length = int(input("Enter the password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    return length, use_uppercase, use_digits, use_special_chars

def main():
    """
    Main function to execute the password generation program.
    """
    length, use_uppercase, use_digits, use_special_chars = get_user_input()
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
