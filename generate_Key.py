from cryptography.fernet import Fernet

# Generate and save key
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

print("✅ Key generated and saved as secret.key")
