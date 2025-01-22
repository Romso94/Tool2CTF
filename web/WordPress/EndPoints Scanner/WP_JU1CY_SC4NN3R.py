import sys
import threading
import time
from typing import Counter
from urllib.parse import urlparse
from tabulate import tabulate
import requests

WP_Ju1cy_3ndp01nts = [
    # Administration
    "wp-admin.php",
    "wp-admin/",
    "wp-login.php",
    "wp-signup.php",
    "wp-activate.php",
    
    # Configuration
    "wp-config.php",
    "wp-settings.php",
    "wp-load.php",
    "robots.txt",
    
    # Core WordPress
    "index.php",
    "wp-blog-header.php",
    "wp-links-opml.php",
    "wp-cron.php",
    "wp-mail.php",
    "wp-links.php",
    "wp-trackback.php",
    "xmlrpc.php",
    "readme.html",
    
    # Includes
    "wp-includes/",
    "wp-includes/version.php",
    "wp-includes/functions.php",
    
    # Content
    "wp-content/",
    "wp-content/uploads/",
    "wp-content/themes/",
    "wp-content/plugins/",
    "wp-content/mu-plugins/",
    "wp-content/languages/",
    "wp-content/upgrade/",
    "wp-content/cache/",
    
    # Debug & Logs
    "wp-content/debug.log",
    "wp-content/backup-db/",
    "wp-content/backups/",
    "wp-content/updraft/",
    
    # JSON API Endpoints
    "wp-json/",
    "wp-json/wp/v2/users",
    "wp-json/wp/v2/posts",
    "wp-json/wp/v2/pages",
    "wp-json/wp/v2/media",
    "wp-json/wp/v2/categories",
    "wp-json/wp/v2/tags",
    "wp-json/wp/v2/comments",
    
    # Advanced JSON Endpoints
    "wp-json/wp/v2/taxonomies",
    "wp-json/wp/v2/types",
    "wp-json/wp/v2/statuses",
    "wp-json/wp/v2/settings",
    "wp-json/wp/v2/themes",
    "wp-json/wp/v2/plugins",
    "wp-json/wp/v2/search",
    
    # User-Specific
    "wp-json/wp/v2/users/me",
    
    # Blocks & Patterns
    "wp-json/wp/v2/blocks",
    "wp-json/wp/v2/block-types",
    "wp-json/wp/v2/block-renderer",
    "wp-json/wp/v2/block-directory",
    "wp-json/wp/v2/pattern-directory",
    "wp-json/wp/v2/global-styles",
    
    # Advanced Endpoints
    "wp-json/wp/v2/templates",
    "wp-json/wp/v2/template-parts",
    "wp-json/wp/v2/navigation",
    "wp-json/wp/v2/menu-items",
    "wp-json/wp/v2/menu-locations",
    
    # Security & Management
    "wp-json/wp/v2/application-passwords",
    "wp-json/wp/v2/site-health",
    "wp-json/wp/v2/site",
    
    # Miscellaneous
    "wp-json/oembed/1.0/embed",
    "wp-json/oembed/1.0/proxy",
    
    # Additional Hidden/Less Known Endpoints
    "wp-json/wp/v2/autosaves",
    "wp-json/wp/v2/revisions",
    "wp-json/wp/v2/block-patterns",
    "wp-json/wp/v2/block-pattern-categories"
]

def animate():
    while True:
        for char in "/-\\|":
            print(f"\rSc4nn1ng 3n c0ur5 {char} ", end="", flush=True)
            time.sleep(0.2)

def H4X0R(L1ST3, URL, F1L3=None, OutPut=False, V3rb0s3=False):
    T3ST3D = []
    response_counts = Counter()
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
            status_code = response.status_code
            T3ST3D.append([full_url, status_code])
            response_counts[status_code] += 1
        except requests.RequestException as e:
            T3ST3D.append([full_url, str(e)])
            response_counts[str(e)] += 1
    
    if OutPut:
        OutPuT(T3ST3D, URL)

    # Arrêter l'animation
    print("\r" + " " * 20 + "\r", end="", flush=True)  # Effacer le message
    print(tabulate(T3ST3D, headers=["URL", "R3SP0NS3"], tablefmt="rounded_grid"))

    if V3rb0s3:
        print("\nSumm4ry 0f R3sp0ns3s:")
        summary = " / ".join([f"{count} r3sp0ns3s {code}" for code, count in response_counts.items()])
        print(summary)


def OutPuT(t4b, URL):
    parsed_url = urlparse(URL)
    domain = parsed_url.netloc
    html_content = f"""
    <html>
    <head>
        <title>XML-RPC Test Results</title>
        <style>
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            table, th, td {{
                border: 1px solid black;
            }}
            th, td {{
                padding: 10px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            pre {{
                white-space: pre-wrap;
                word-wrap: break-word;
            }}
        </style>
    </head>
    <body>
        <h1>Endpoint Scan Results {domain} </h1>
        {tabulate(t4b, headers=["URL", "R3SP0NS3"], tablefmt="unsafehtml")}
    </body>
    </html>
    """
    with open(f"./{domain}.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    return

def H3LP():
    help_text = """
    Usage: WP_JU1CY_SC4NN3R.py [options]

    Options:
    -h, --help, h, help      Sh0w th1s h3lp m3ssag3 4nd 3x1t
    -u URL, -U URL           Sp3c1fy th3 b4s3 URL t0 sc4n
    -f FILE, -F FILE         Sp3c1fy 4 TXT f1l3 c0nt41n1ng 4dd1t10n4l 3ndp01nts t0 sc4n
    -o, -O                   Sp3c1fy 1f Y0U W4nt 4n 0utput f1l3 1n HTML
    -v, -V                   4dd 4 Pr1nt T0 Sh0w 1nf0 4b0ut 4ll R3sp0ns3s

    Example:
    python WP_JU1CY_SC4NN3R.py -u https://example.com -f endpoints.txt -o -v
    """

    print(help_text)

def format_url(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = "https://" + url
    return url

if __name__ == "__main__":
    C0mm4nd3 = sys.argv
    URL, P4TH_TO_F1L3, Outputn, V3rb0s3 = None, None, False, False
    
    if len(sys.argv) < 2 or any(option in sys.argv for option in ["-h", "--help", "h", "help"]):
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
        Outputn = True
    
    if "-v" in C0mm4nd3 or "-V" in C0mm4nd3:
        V3rb0s3= True

    H4X0R(WP_Ju1cy_3ndp01nts, URL, P4TH_TO_F1L3, Outputn, V3rb0s3)



    
    
    