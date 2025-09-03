
<img width="1839" height="907" alt="image" src="https://github.com/user-attachments/assets/d476a997-49ed-4673-8049-4f968e6d646c" />
# 🔐 Keylogger PoC (Educational Use Only)

> ⚠️ This project is for **educational and cybersecurity learning purposes only**.  
> Do **not** use it on systems you don’t own or without permission.

---

## 📌 Features
- Capture keystrokes using `pynput`
- Encrypt keystrokes with `cryptography.Fernet`
- Store encrypted logs locally with timestamps
- Decrypt logs locally or send them to a Flask server
- Server receives encrypted data, decrypts, and stores logs

---

## 📂 Files
- `generate_key.py` → Generate a Fernet key (`secret.key`)
- `write.py` → Keylogger (captures, encrypts, logs, sends to server)
- `server.py` → Flask server (receives + decrypts)
- `decrypt_logs.py` → Decrypt local logs (`log.txt → decrypted.txt`)
- `log.txt` → Encrypted local keystrokes (**ignored in git**)
- `decrypted_log.txt` → Local decrypted logs (**ignored in git**)
- `server_log.txt` → Server decrypted logs (**ignored in git**)

---

## 🚀 Setup & Usage

### 1️⃣ Clone Repo
git clone https://github.com/Nissiuser/KeyLogger-POC.git
cd KeyLogger-POC

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Generate Encryption Key
python3 generatekey.py

4️⃣ Start the Server (Terminal A)
python3 server.py

5️⃣ Start the Keylogger (Terminal B)
python3 write.py

6️⃣ (Optional) Decrypt Local Logs
python3 decrypt.py

✅ Example Output
serverlog.txt

--- Session started: 2025-09-03 22:00:01 ---
hello world
--- Session ended: 2025-09-03 22:01:12 ---

⚠️ Disclaimer
This project is strictly for learning:

Cybersecurity students
Ethical hacking labs
Researchers
Do not deploy on machines without explicit permission.

---

👉 This is lightweight, beginner-friendly, and gets straight to the point.  
