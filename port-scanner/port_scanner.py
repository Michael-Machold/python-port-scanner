import socket
import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from colorama import Fore, Style, init

init()

# Common ports and services
common_services = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 139: "NetBIOS",
    143: "IMAP", 443: "HTTPS"
}

results = []

# Scan function
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target_ip, port))
        if result == 0:
            service = common_services.get(port, "Unknown")

            banner = ""
            try:
                if port == 80:
                    s.send(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
                    banner = s.recv(1024).decode(errors="ignore").strip()
                else:
                    banner = s.recv(1024).decode(errors="ignore").strip()
            except:
                banner = "No banner"

            print(Fore.GREEN + f"[OPEN] Port {port} ({service})" + Style.RESET_ALL)

            results.append({
                "port": port,
                "service": service,
                "banner": banner
            })

        s.close()
    except:
        pass


# Argument parser
parser = argparse.ArgumentParser(description="Advanced Python Port Scanner")
parser.add_argument("target", help="Target IP or domain")
parser.add_argument("-p", "--ports", default="1-1024", help="Port range (e.g. 20-100)")
parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads")
parser.add_argument("-o", "--output", default="results.json", help="Output file")

args = parser.parse_args()

# Resolve target
try:
    target_ip = socket.gethostbyname(args.target)
except socket.gaierror:
    print(Fore.RED + "Invalid target" + Style.RESET_ALL)
    exit()

# Parse ports
start_port, end_port = map(int, args.ports.split("-"))

print(Fore.CYAN + f"\nTarget: {args.target} ({target_ip})" + Style.RESET_ALL)
print(Fore.YELLOW + f"Scanning ports {start_port}-{end_port} with {args.threads} threads\n" + Style.RESET_ALL)

start_time = datetime.now()

# Run scanner
with ThreadPoolExecutor(max_workers=args.threads) as executor:
    executor.map(scan_port, range(start_port, end_port + 1))

end_time = datetime.now()

# Save results
with open(args.output, "w") as f:
    json.dump(results, f, indent=4)

# Summary
print(Fore.CYAN + "\nScan complete." + Style.RESET_ALL)
print(Fore.CYAN + f"Time taken: {end_time - start_time}" + Style.RESET_ALL)
print(Fore.CYAN + f"Results saved to {args.output}" + Style.RESET_ALL)
