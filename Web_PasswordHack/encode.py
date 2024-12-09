import hashlib

def hash_password(password):
    # Encode the password to bytes
    password_bytes = password.encode('utf-8')
    # Use a hashing algorithm, e.g., SHA256
    hash_object = hashlib.sha256(password_bytes)
    # Get the hexadecimal representation of the hash
    return hash_object.hexdigest()

USER_CREDENTIALS = {
    #ADD HERE TO ENCODE
}

images = ""
users = ""
flags = ""

for username, password in USER_CREDENTIALS.items():
    users = users + f'"{username}": "{hash_password(password)}",\n'
    flag = str(hash_password(username))
    flag = flag[-4:]
    images = images + "success-"+flag+".gif\n"
    flags = flags + flag + '\n'

print("USERS:\n", users)
print("IMAGES:\n", images)
print("FLAGS:\n", flags)