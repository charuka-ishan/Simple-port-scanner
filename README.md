# Simple-port-scanner
port scanner (Python)
# TITUS Port Scanner 

A simple TCP port scanner written in Python for learning and educational purposes.  
This tool scans a target IP address and identifies open ports along with their common services.

 **Disclaimer**  
 This tool is intended for **educational use only**.  
 Scan **only systems you own or have explicit permission to test**.

---

##  Features

- TCP Connect port scanning
- Scans common ports (1–1024 by default)
- Displays open ports with service names
- Clean Linux-style ASCII banner
- Safe and stable (no aggressive threading)
- Beginner-friendly and exam-ready

---

##  Screenshot / Banner
<img width="897" height="284" alt="image" src="https://github.com/user-attachments/assets/146876b7-ce79-4a21-9a44-dec6008fda46" />

---

## 🚀 How It Works

- Uses Python’s built-in `socket` module
- Attempts TCP connections to each port
- If the connection succeeds, the port is marked as **OPEN**
- Attempts to resolve the service name using `getservbyport()`

---

##  Requirements

- Python 3.x
- No external libraries required

---

##  Usage

1. Clone the repository:
```bash
git clone https://github.com//charuka-ishan/Simple-port-scanner.git
cd titus-port-scanner
```
## Run Scanner 
python scanner.py


