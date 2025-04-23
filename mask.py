import os
import time
import requests
import re
from colorama import init, Fore, Style

init()

def clear_screen():
    os.system('clear')

def banner():
    print(Fore.RED + """
    ██████╗  █████╗ ██████╗ ██╗  ██╗    ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗
    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██╔══██╗██║  ██║██║██╔════╝██║  ██║████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
    ██║  ██║███████║██████╔╝█████╔╝     ██████╔╝███████║██║███████╗███████║██╔████╔██║███████║█████╗     ██║   █████╗  ██████╔╝
    ██║  ██║██╔══██║██╔══██╗██╔═██╗     ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║╚██╔╝██║██╔══██║██╔══╝     ██║   ██╔══╝  ██╔══██╗
    ██████╔╝██║  ██║██║  ██║██║  ██╗    ██║     ██║  ██║██║███████║██║  ██║██║ ╚═╝ ██║██║  ██║███████╗   ██║   ███████╗██║  ██║
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
    """ + Style.RESET_ALL)
    print(Fore.YELLOW + "MASK X - @darkhub__a1" + Style.RESET_ALL)
    print(Fore.GREEN + "TEAM - DARK" + Style.RESET_ALL)

def url_checker(url):
    if not re.match(r'^https?://', url):
        print(Fore.RED + "[!] Invalid URL. Please use http or https." + Style.RESET_ALL)
        exit(1)

def shorten_url(phish_link):
    try:
        response = requests.get(f"https://is.gd/create.php?format=simple&url={phish_link}", timeout=10)
        return response.text.strip()
    except requests.RequestException as e:
        print(Fore.RED + f"[!] Error shortening URL: {e}" + Style.RESET_ALL)
        return phish_link

def mask_x():
    clear_screen()
    banner()
    print(Fore.YELLOW + "[*] 🔥 MASK X  Activated..." + Style.RESET_ALL)
    time.sleep(1)
    
    print(Fore.CYAN + "\n### Phishing URL ###" + Style.RESET_ALL)
    phish = input(Fore.WHITE + "Paste Phishing URL here (with http or https): " + Style.RESET_ALL)
    url_checker(phish)
    time.sleep(1)
    print(Fore.CYAN + "Processing and Modifying Phishing URL..." + Style.RESET_ALL)
    short_url = shorten_url(phish)
    shorter_url = short_url.replace("https://", "")
    
    print(Fore.CYAN + "\n### Masking Domain ###" + Style.RESET_ALL)
    mask = input(Fore.WHITE + "Domain to mask the Phishing URL (with http or https, e.g., https://google.com): " + Style.RESET_ALL)
    url_checker(mask)
    
    print(Fore.CYAN + '\nType social engineering words (like free-money, best-pubg-tricks):' + Style.RESET_ALL)
    print(Fore.RED + "Don't use space, just use '-' between words" + Style.RESET_ALL)
    words = input(Fore.GREEN + "=> " + Style.RESET_ALL).strip()
    
    if not words or ' ' in words:
        print(Fore.RED + "[!] No words or invalid input. Using default mask." + Style.RESET_ALL)
        final_link = f"{mask}@{shorter_url}"
    else:
        final_link = f"{mask}-{words}@{shorter_url}"
    
    print(Fore.CYAN + "\nGenerating MaskPhish Link..." + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.GREEN + f"Here is the MaskPhish URL: {final_link}" + Style.RESET_ALL)
    print(Fore.YELLOW + "\nTest it locally in your browser! (Demo Mode)" + Style.RESET_ALL)
    
    print(Fore.RED + "[!] Self-destructing in 15 seconds..." + Style.RESET_ALL)
    time.sleep(15)
    print(Fore.GREEN + "[+] 🎉 MASK X DEMO Stopped!" + Style.RESET_ALL)

def main():
    clear_screen()
    banner()
    mask_x()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Exiting..." + Style.RESET_ALL)
        exit()