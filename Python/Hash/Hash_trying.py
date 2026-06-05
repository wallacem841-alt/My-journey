import json
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

# login or register
while True:
    login_register = input("login l, register r: ")
    if login_register in ("l", "r"):
        break

user = input("Username: ")
password = input("Password: ")

def load_passwords():
    try:
        with open("Password.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_passwords(data):
    with open("Password.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def register(user, password):
    # WARNING:
    # This function OVERWRITES the password if the username already exists.
    # This is intentional for testing purposes and NOT secure for production.
    pass_file = load_passwords()
    pass_file[user] = ph.hash(password)
    save_passwords(pass_file)

if login_register == "r":
    register(user, password)
    print("User registered.")

else:
    pass_file = load_passwords()

    if user not in pass_file:
        print("Username doesn't exist.")
    else:
        try:
            stored_hash = pass_file[user]

            # Verify password
            ph.verify(stored_hash, password)

            # Rehash if parameters changed
            if ph.check_needs_rehash(stored_hash):
                pass_file[user] = ph.hash(password)
                save_passwords(pass_file)

            print("Login successful.")

        except VerifyMismatchError:
            print("Wrong password.")