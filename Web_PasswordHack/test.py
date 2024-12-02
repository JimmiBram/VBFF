import hashlib

def hash_password(password):
    # Encode the password to bytes
    password_bytes = password.encode('utf-8')
    # Use a hashing algorithm, e.g., SHA256
    hash_object = hashlib.sha256(password_bytes)
    # Get the hexadecimal representation of the hash
    return hash_object.hexdigest()

USER_CREDENTIALS = {
    "student1": "4c713b660433b668d55b00b87f5c64ce2ad5aeb94207d3fbfc51634feefe9088",
    "student2": "1532e76dbe9d43d0dea98c331ca5ae8a65c5e8e8b99d3e2a42ae989356f6242a",
    "hacker1": "7a7801334db4cb75baa54b9a4d7c136212d3abe882abcb88de94e5615d71cb48",
    "hacker2": "921a95e8b614f668981d9eee4d24a3ffdb6821162246bb8036f73f4fd7d20564",
    "teacher1": "a3918628a8f2821ae8abe7bbe1d817241df2cb93dccd4cfae83b2d8c64107c43",
    "teacher2": "501d5acb4acc06d85d1fe1979a5d36b68f2becc069756164f763fc8bd275d0f0",
    "admin": "a8589dbb7121f100b2fe2abb201e5f927275d060168156a1421a3ffa36d0319c",
    "superadmin": "abdb9dec52c7936258206899e60d5d5ebc277469c847ac2a04c49d2f579b4601",
    "demo": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"
}

for username, password in USER_CREDENTIALS.items():
    #print(f'"{username}": "{hash_password(password)}",')
    flag = str(hash_password(username))
    flag = flag[-4:]
    print("success-"+flag+".gif")
