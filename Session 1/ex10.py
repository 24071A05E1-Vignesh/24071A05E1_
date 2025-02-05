#a function that generates a random password with a mix of uppercase, lowercase, digits, and special characters.
import random
import string

def generate_password(length=12):
    # Define the characters to choose from
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password has at least one character from each category
    password = [
        random.choice(string.ascii_lowercase), 
        random.choice(string.ascii_uppercase), 
        random.choice(string.digits), 
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the password with random characters
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password to randomize the order of characters
    random.shuffle(password)
    
    # Convert list to string and return
    return ''.join(password)

# Example usage
password = generate_password(12)
print(password)