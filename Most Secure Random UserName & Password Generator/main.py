# Importing the secrets library for generating cryptographically secure random numbers
import secrets

# Importing the string library for character sets
import string

# Defining a function that generates a password with a mix of characters and a given length
def generate_password(length):
  # Initializing an empty string for the password
  password = ""
  # Looping through the length of the password
  for _ in range(length):
    # Choosing a random character set from the four options
    char_set = secrets.choice([string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation])
    # Choosing a random character from the chosen set and appending it to the password
    password += secrets.choice(char_set)
  # Returning the password
  return password

# Defining a function that generates a username with a mix of characters and two given lengths separated by a dash (-)
def generate_username(length1, length2):
  # Initializing an empty string for the username
  username = ""
  # Looping through the first length of the username
  for _ in range(length1):
    # Choosing a random character set from the three options (excluding punctuation)
    char_set = secrets.choice([string.ascii_uppercase, string.ascii_lowercase, string.digits])
    # Choosing a random character from the chosen set and appending it to the username
    username += secrets.choice(char_set)
  # Adding a dash to separate the two parts of the username
  username += "-"
  # Looping through the second length of the username
  for _ in range(length2):
    # Choosing a random character set from the three options (excluding punctuation)
    char_set = secrets.choice([string.ascii_uppercase, string.ascii_lowercase, string.digits])
    # Choosing a random character from the chosen set and appending it to the username
    username += secrets.choice(char_set)
  # Returning the username
  return username

# Asking for the input from the user twice and converting it to an integer
length1 = int(input("Enter the first part of username length: "))
length2 = int(input("Enter the second part of username length: "))

# Generating a random username using alphanumeric characters with two parts separated by a dash (-)
username = generate_username(length1, length2)

# Printing the generated username
print("Your username is:", username)

# Asking for the input from the user and converting it to an integer
password_length = int(input("Enter the length of password: "))

# Generating a random password using hexadecimal characters with the given length
password = generate_password(password_length)

# Printing the generated password
print("Your password is:", password)