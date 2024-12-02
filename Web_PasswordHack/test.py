import hashlib

def hash_password(password):
    # Encode the password to bytes
    password_bytes = password.encode('utf-8')
    # Use a hashing algorithm, e.g., SHA256
    hash_object = hashlib.sha256(password_bytes)
    # Get the hexadecimal representation of the hash
    return hash_object.hexdigest()

USER_CREDENTIALS = {
    "student1": "mississippi",
    "student2": "batman",
    "hacker1": "dragster",
    "hacker2": "sunlight",
    "teacher1": "goldeneye",
    "teacher2": "playstation",
    "admin": "mutant37",
    "superadmin": "restart75",
    "demo": "password123"
}

for username, password in USER_CREDENTIALS.items():
    print(f'"{username}": "{hash_password(password)}",')