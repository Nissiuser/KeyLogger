from cryptography.fernet import Fernet

def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

key = load_key()
fernet = Fernet(key)

text = ""

with open("log.txt", "rb") as f:
    for line in f:
        decrypted = fernet.decrypt(line.strip()).decode()

        if decrypted.startswith("--- Session"):
            text += f"\n{decrypted}\n"
        else:
            text += decrypted  

with open("decrypted_log.txt", "w") as f:
    f.write(text)

print("✅ Decrypted log saved to decrypted_log.txt")
