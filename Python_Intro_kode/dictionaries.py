# Initial dictionary
konti = {
    "123456": {"balance": 5000, "pin": "1234"},
    "654321": {"balance": 3000, "pin": "5678"}
}

# 1. Adding a New Record
konti["789012"] = {"balance": 7000, "pin": "9012"}
print("After adding:", konti)
# Output: {'123456': {'balance': 5000, 'pin': '1234'}, '654321': {'balance': 3000, 'pin': '5678'}, '789012': {'balance': 7000, 'pin': '9012'}}

# 2. Editing an Existing Record (e.g., changing balance for account "123456")
konti["123456"]["balance"] = 6000
konti["123456"]["pin"] = "4321"  # Changing the pin as well
print("After editing:", konti)
# Output: {'123456': {'balance': 6000, 'pin': '4321'}, '654321': {'balance': 3000, 'pin': '5678'}, '789012': {'balance': 7000, 'pin': '9012'}}

# 3. Deleting a Record (e.g., removing account "654321")
del konti["654321"]
print("After deleting:", konti)
# Output: {'123456': {'balance': 6000, 'pin': '4321'}, '789012': {'balance': 7000, 'pin': '9012'}}

# Iterating over all records
for account_number, details in konti.items():
    print(f"Account Number: {account_number}")
    print(f"  Balance: {details['balance']}")
    print(f"  PIN: {details['pin']}")
    print()  # Blank line for better readability

# Checking if a key exists
account_number = "123456"

if account_number in konti:
    print(f"Account {account_number} exists.")
else:
    print(f"Account {account_number} does not exist.")