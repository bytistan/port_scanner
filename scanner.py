import socket
from datetime import datetime
from termcolor import colored
import sys

info_text = colored("INFO" ,"green")
error_text = colored("ERROR" ,"red")
warn_text = colored("WARNING", "yellow")
open_text = colored("OPEN", "green", attrs = ["bold"])

def get_time():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H.%M.%S")
    colored_text = colored(formatted_time, "cyan")

    return colored_text 

def port_scanner(target, start_port, end_port):
    current_time = get_time()

    print(f"[{current_time}] [{info_text}] Scanning target: {target}")
    print(f"[{current_time}] [{info_text}] Scanning ports from {start_port} to {end_port}")
    
    start_time = datetime.now()

    try:
        for port in range(start_port, end_port):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((target, port))
                if result == 0:
                    current_time = get_time()
                    print(f"[{current_time}] [{open_text}] {port}")

    except KeyboardInterrupt:
        current_time = get_time() 
        print(f"[{current_time}] [{info_text}] Bye.")
        return
    except socket.gaierror:
        current_time = get_time()
        print(f"[{current_time}] [{error_text}] Hostname could not be resolved.")
        return
    except socket.error:
        current_time = get_time()
        print(f"[{current_time}] [{error_text}] Couldn't connect to the server.")
        return

    end_time = datetime.now()
    current_time = get_time()

    print(f"[{current_time}] [{info_text}] Scanning completed in {colored(end_time - start_time, 'green')}")

if __name__ == "__main__":
    arguments = sys.argv
    ip = arguments[1]
    port_scanner(ip, 0, 65536)
