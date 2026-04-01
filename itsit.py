import requests
import psutil
import time
import sys
import os
import platform

from colorama import Fore, Style, init
init(autoreset=True)

def colored(text, color):
    return f"{color}{text}{Style.RESET_ALL}"

# Get base directory
def get_base_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


# Website Check
def check_website():
    url = input("Enter a website url: ").strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        end = time.time()

        response_time = round(end - start, 3)

        print(colored("\nWebsite Status: ", Fore.CYAN))
        print("Status Code: ", response.status_code)
        print("Response Time: ", response_time, "seconds")

        if response.status_code == 200 and response_time < 1.5:
            print(colored("✔  Status: HEALTHY", Fore.GREEN))
        elif response.status_code == 200 and response_time < 3:
            print(colored("⚠  Status: WARNING (Slow response)", Fore.YELLOW))
        elif response.status_code == 200:
            print(colored("✖  Status: CRITICAL (Very slow response)", Fore.RED))
        else:
            print(colored("✖  Status: CRITICAL", Fore.RED))
    
    except requests.exceptions.RequestException:
        print(colored("✖  Status: CRITICAL (Website Down)", Fore.RED))


# System Health Check
def check_system_health():
    # Check CPU usage
    cpu = psutil.cpu_percent(interval=1)

    # Check Memory usage
    memory = psutil.virtual_memory().percent

    # Check Disk usage
    disk = psutil.disk_usage(os.path.abspath('/')).percent

    # platform module works reliably on Windows, Mac, and Linux
    system_name = platform.node()        # Computer/hostname
    os_name     = platform.system()      # Windows, Darwin (Mac), Linux
    os_version  = platform.version()     # Detailed OS version

    print(colored("\nSystem Info:", Fore.CYAN))
    print(f"System Name : {system_name}")
    print(f"OS          : {os_name}")
    print(f"OS Version  : {os_version}")

    print(colored("\nSystem Health:", Fore.CYAN))
    print(f"CPU Usage   : {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage  : {disk}%")

    if cpu > 90 or memory > 90 or disk > 90:
        print(colored("✖  Overall Status: CRITICAL", Fore.RED))
    elif cpu > 80 or memory > 88 or disk > 85:
        print(colored("⚠  Overall Status: WARNING", Fore.YELLOW))
    else:
        print(colored("✔  Overall Status: HEALTHY", Fore.GREEN))


# Log Analyzer
def analyze_logs():
    file_name = input("Enter log file name or full path: ").strip()

    # Normalize path separators for the current OS
    # This converts both / and \ to the correct separator automatically
    file_name = os.path.normpath(file_name)

    if os.path.isabs(file_name):
        # User typed a full path — use it directly
        if not os.path.exists(file_name):
            print(colored("Error: File not found at the given path.", Fore.RED))
            print("Make sure the path is correct and the file exists.")
            return
    else:
        found = None
        base_dir = get_base_dir()

        # Walk through base directory and ALL subfolders (including 'logs')
        # os.walk works the same on Windows, Mac, and Linux
        for root, dirs, files in os.walk(base_dir):
            # Case-insensitive file matching to handle differences across OS
            # Windows is case-insensitive, Mac/Linux are case-sensitive
            for f in files:
                if f.lower() == file_name.lower():
                    found = os.path.join(root, f)
                    break
            if found:
                break

        if not found:
            print(colored(f"Error: '{file_name}' not found.", Fore.RED))
            print(f"\nMake sure '{file_name}' exists in:")
            print(colored(f"  {base_dir}", Fore.YELLOW))
            print(colored(f"  {os.path.join(base_dir, 'logs')}  <-- or inside a 'logs' subfolder", Fore.YELLOW))
            print("\nOr enter the full path instead, e.g.:")
            if os.name == 'nt':  # Windows
                print(colored("  C:\\Users\\yourname\\logs\\logfile", Fore.YELLOW))
            else:  # Mac and Linux
                print(colored("  /home/yourname/logs/logfile", Fore.YELLOW))
            return

        print(colored(f"✔  Found: {found}", Fore.GREEN))
        file_name = found

    try:
        error_count = 0
        warning_count = 0
        info_count = 0

        with open(file_name, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                line = line.lower()

                if "error" in line:
                    error_count += 1
                elif "warn" in line:
                    warning_count += 1
                elif "info" in line:
                    info_count += 1 
        
        print(colored("\nLog Summary:", Fore.CYAN))
        print(f"ERROR: {error_count}")
        print(f"WARNING: {warning_count}")
        print(f"INFO: {info_count}")

        total = error_count + warning_count + info_count

        if total == 0:
            print("No logs found.")
            return
        
        error_ratio = error_count / total
        warning_ratio = warning_count / total

        print(f"Error Rate : {error_ratio:.2%}")
        print(f"Warning Rate: {warning_ratio:.2%}")

        if error_ratio > 0.3:
            print(colored("✖  Status: CRITICAL", Fore.RED))
        elif error_ratio > 0.1 or warning_ratio > 0.3:
            print(colored("⚠  Status: WARNING", Fore.YELLOW))
        else:
            print(colored("✔  Status: HEALTHY", Fore.GREEN))

    except FileNotFoundError:
        print(colored("Error: File not found.", Fore.RED))
    except PermissionError:
        print(colored("Error: Permission denied. Cannot read this file.", Fore.RED))
    except Exception as e:
        print(colored(f"Unexpected error: {e}", Fore.RED))
        

# Menu
subtitle = "IT Support & Infrastructure Toolkit"

def show_menu():
    print()
    print(Fore.CYAN + Style.BRIGHT + "ITSIT".center(50))
    print(Style.DIM + "\033[3m" + subtitle.center(50) + "\033[0m")
    print(Fore.WHITE + "-" * 50)

    print(Fore.GREEN + "[1] Check Website Uptime")
    print(Fore.GREEN + "[2] Check System Health")
    print(Fore.GREEN + "[3] Analyze Logs")
    print(Fore.RED + "[4] Exit")

def main():
    while True:
        show_menu()
        choice = input("\nEnter choice: ")

        if choice == "1":
            check_website()
        elif choice == "2":
            check_system_health()
        elif choice == "3":
            analyze_logs()
        elif choice == "4":
            print("Thank you for using ITSIT. Goodbye!")
            break
        else:
            print(colored("Invalid choice. Try again.", Fore.RED))

main()