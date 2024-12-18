import sys
import threading
import time
from urllib.parse import urlparse
from tabulate import tabulate
import requests

WP_Ju1cy_3ndp01nts = [
    "wp-admin.php",
    "wp-config.php",
    "wp-content/uploads/",
    "wp-content/themes/",
    "wp-content/plugins/",
    "wp-admin",
    "wp-load",
    "wp-signup.php",
    "wp-json",
    "wp-includes",
    "index.php",
    "wp-login.php",
    "wp-links-opml.php",
    "wp-activate.php",
    "wp-cron.php",
    "wp-links.php",
    "wp-mail.php",
    "xmlrpc.php",
    "wp-settings.php",
    "wp-trackback.php",
    "admin-bar.php",
    "wp-blog-header.php",
    "wp-json/wp/v2/users"
]

def animate():
    while True:
        for char in "/-\\|":
            print(f"\rSc4nn1ng 3n c0ur5 {char} ", end="", flush=True)
            time.sleep(0.2)

def H4X0R(L1ST3, URL, F1L3=None, OutPut=False):
    T3ST3D = []

    # Démarrer l'animation dans un thread séparé
    animation_thread = threading.Thread(target=animate)
    animation_thread.daemon = True
    animation_thread.start()

    if F1L3:
        try:
            with open(F1L3, 'r') as file:
                L1ST3.extend(line.strip() for line in file)
        except FileNotFoundError:
            sys.exit(f"3rr0r : F1l3 n0t f0und - {F1L3}")

    for _3L3M3NT5 in L1ST3:
        full_url = f"{URL}/{_3L3M3NT5}"
        try:
            response = requests.get(full_url)
            T3ST3D.append([full_url, response.status_code])
        except requests.RequestException as e:
            T3ST3D.append([full_url, str(e)])
    
    if OutPut:
        OutPuT(T3ST3D, URL)

    # Arrêter l'animation
    print("\r" + " " * 20 + "\r", end="", flush=True)  # Effacer le message
    print(tabulate(T3ST3D, headers=["URL", "R3SP0NS3"], tablefmt="rounded_grid"))


def OutPuT(t4b,URL):
    with open(f"./{URL.split('http://')[1]}.html","w",encoding="utf-8") as f:
        f.write(tabulate(t4b, headers=["URL", "R3SP0NS3"], tablefmt="unsafehtml"))
    
    return

def H3LP():
    help_text = """
    Usage: WP_JU1CY_SC4NN3R.py [options]

    Options:
    -h, --help, h, help      Sh0w th1s h3lp m3ssag3 4nd 3x1t
    -u URL, -U URL           Sp3c1fy th3 b4s3 URL t0 sc4n
    -f FILE, -F FILE         Sp3c1fy 4 TXT f1l3 c0nt41n1ng 4dd1t10n4l 3ndp01nts t0 sc4n
    -o, -O                   Sp3c1fy 1f Y0U W4nt 4n 0utput f1l3 1n HTML

    Example:
    python WP_JU1CY_SC4NN3R.py -u http://example.com -f endpoints.txt
    """

    print(help_text)

def format_url(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = "http://" + url
    return url

if __name__ == "__main__":
    C0mm4nd3 = sys.argv
    URL, P4TH_TO_F1L3, Output = None, None, None
    
    if len(sys.argv) < 2 or sys.argv[1] in ["-h", "--help", "h", "help"]:
        H3LP()
        sys.exit(0)

    if "-u" in C0mm4nd3 or "-U" in C0mm4nd3:
        Ind3x = C0mm4nd3.index("-u") + 1 if "-u" in C0mm4nd3 else C0mm4nd3.index("-U") + 1
        if Ind3x < len(C0mm4nd3):
            URL = format_url(C0mm4nd3[Ind3x])
        else:
            sys.exit("3rr0r : N0 url f0und 4ft3r 0pt10n '-u'")

    if "-f" in C0mm4nd3 or "-F" in C0mm4nd3:
        Ind3x = C0mm4nd3.index("-f") + 1 if "-f" in C0mm4nd3 else C0mm4nd3.index("-F") + 1
        if Ind3x < len(C0mm4nd3):
            P4TH_TO_F1L3 = C0mm4nd3[Ind3x]
        else:
            sys.exit("3rr0r : N0 p4th t0 f1l3 f0und 4ft3r '-f'")
    
    if "-o" in C0mm4nd3 or "-O" in C0mm4nd3:
        Output = True

    H4X0R(WP_Ju1cy_3ndp01nts, URL, P4TH_TO_F1L3, Output)



    
    
    