# Day 22-23: Building a Simple Port Scanner
# Build a basic port scanner that checks if a port is open on a target server.


import socket

def scan_ports(target_ip, start_port, end_port):
    print(f"Scanning {target_ip} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # timeout in seconds

        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"✅ Port {port} is OPEN")
        sock.close()

if __name__ == "__main__":
    target = input("Enter target IP address (e.g., 192.168.1.1): ")
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))

    scan_ports(target, start, end)
