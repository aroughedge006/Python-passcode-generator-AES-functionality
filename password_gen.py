
import random
import string

def generate_password(length, mode):
    """
    Generate a secure password of the specified length based on the mode.
    
    Args:
    - length (int): Length of the password (must be between 1 and 16).
    - mode (str): 'letters' for letters only, 'numbers_special' for numbers and special chars only,
                  'aes' for AES-level (letters + numbers + special chars).
    
    Returns:
    - str: The generated password.
    
    Raises:
    - ValueError: If length is not between 1 and 16, or if mode is invalid.
    """
    if length < 1 or length > 16:
        raise ValueError("Password length must be between 1 and 16.")
    
    charset = ''
    if mode == 'letters':
        charset = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif mode == 'numbers_special':
        charset = string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"  # Numbers + special chars
    elif mode == 'aes':
        charset = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"  # Full AES-level charset
    else:
        raise ValueError("Invalid mode. Use 'letters', 'numbers_special', or 'aes'.")
    
    if not charset:
        raise ValueError("Charset cannot be empty.")
    
    # Generate password using random.choices for Python 3.6+
    password = ''.join(random.choices(charset, k=length))
    return password

def main():
    """
    Interactive main function to generate passwords with mode selection.
    Modes:
    - 'letters': All letters only
    - 'numbers_special': All numbers and special characters only
    - 'aes': AES-level strength (full charset: letters, numbers, special chars)
    """
    print("Password Generator (Modes: Letters Only, Numbers+Special, or AES-Level)")
    print("Supports lengths 1-16.")
    
    try:
        length = int(input("Enter password length (1-16): "))
        
        print("\nSelect mode:")
        print("1. All letters")
        print("2. All numbers and special characters")
        print("3. AES encryption level (full strength)")
        
        choice = input("Enter choice (1/2/3): ").strip()
        if choice == '1':
            mode = 'letters'
            mode_desc = "Letters only"
        elif choice == '2':
            mode = 'numbers_special'
            mode_desc = "Numbers and special characters only"
        elif choice == '3':
            mode = 'aes'
            mode_desc = "AES-level (letters + numbers + special)"
        else:
            raise ValueError("Invalid choice. Please select 1, 2, or 3.")
        
        password = generate_password(length, mode)
        print(f"\nGenerated Password: {password}")
        print(f"Length: {len(password)}")
        print(f"Mode: {mode_desc}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
