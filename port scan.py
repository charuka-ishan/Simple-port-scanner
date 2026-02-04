import socket

print("""
████████╗██╗████████╗██╗   ██╗███████╗
╚══██╔══╝██║╚══██╔══╝██║   ██║██╔════╝
   ██║   ██║   ██║   ██║   ██║███████╗
   ██║   ██║   ██║   ██║   ██║╚════██║
   ██║   ██║   ██║   ╚██████╔╝███████║
   ╚═╝   ╚═╝   ╚═╝    ╚═════╝ ╚══════╝
""")


target = "127.0.0.1" # enter the IP Address you want to scan

for port in range(1, 1025):# port range (change up to 65535 if needed)
    try:
        s = socket.socket()
        s.settimeout(0.3)
        if s.connect_ex((target, port)) == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            print(f"[OPEN] Port {port} ({service})")
        s.close()
    except KeyboardInterrupt:
        print("\nScan stopped.")
        break
