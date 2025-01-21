import html
import sys
import threading
import time
from typing import Counter
from urllib.parse import urlparse
from xml.sax import parseString
from tabulate import tabulate
import requests


def animate():
    while True:
        for char in "/-\\|":
            print(f"\rSc4nn1ng 3n c0ur5 {char} ", end="", flush=True)
            time.sleep(0.2)


def H4X0R(URL=None, F1L3=None, OutPut=False, V3rb0s3=False, N4M3=None):
    T3ST3D = []
    response_counts = Counter()
    # Démarrer l'animation dans un thread séparé
    animation_thread = threading.Thread(target=animate)
    animation_thread.daemon = True
    animation_thread.start()

    headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Content-Type": "text/xml"
                }

    payload = """<?xml version="1.0" encoding="utf-8"?>
                <methodCall>
                <methodName>system.listMethods</methodName>
                <params></params>
                </methodCall>"""

    if F1L3:
        try:
            with open(F1L3, 'r') as file:
                L1ST3 = [line.strip() for line in file]
        except FileNotFoundError:
            sys.exit(f"3rr0r : F1l3 n0t f0und - {F1L3}")

        for _3L3M3NT5 in L1ST3:
            full_url = f"{_3L3M3NT5}/xmlrpc.php"
            try:
                response = requests.post(full_url, headers=headers, data=payload)
                status_code = response.status_code
                formatted_response = format_xml(response.text)
                T3ST3D.append([full_url, status_code, f"<pre>{formatted_response}</pre>"])
                response_counts[status_code] += 1
            except requests.RequestException as e:
                T3ST3D.append([full_url, str(e), str(e)])
                response_counts[str(e)] += 1
    if URL:
        try:
            response = requests.post(f"{URL}/xmlrpc.php", headers=headers, data=payload)
            status_code = response.status_code
            formatted_response = format_xml(response.text)
            T3ST3D.append([f"{URL}/xmlrpc.php", status_code, f"<pre>{formatted_response}</pre>"])
            response_counts[status_code] += 1
        except requests.RequestException as e:
            T3ST3D.append([f"{URL}/xmlrpc.php", str(e), str(e)])
            response_counts[str(e)] += 1


    if OutPut:
        OutPuT(T3ST3D, URL, N4M3)

    # Arrêter l'animation
    print("\r" + " " * 20 + "\r", end="", flush=True)  # Effacer le message
    print(tabulate(T3ST3D, headers=["URL","C0D3", "R3SP0NS3"], tablefmt="rounded_grid"))

    if V3rb0s3:
        print("\nSumm4ry 0f R3sp0ns3s:")
        summary = " / ".join([f"{count} r3sp0ns3s {code}" for code, count in response_counts.items()])
        print(summary)


def OutPuT(t4b, URL, N4M3):
    parsed_url = urlparse(URL)
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
        <h1>XML-RPC Test Results  </h1>
        {tabulate(t4b, headers=["URL", "C0D3", "R3SP0NS3"], tablefmt="unsafehtml")}
    </body>
    </html>
    """
    with open(f"./{N4M3}.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    return

def H3LP():
    help_text = """
    Usage: .py [options]

    Options:
    -h, --help, h, help      Sh0w th1s h3lp m3ssag3 4nd 3x1t
    -u URL, -U URL           Sp3c1fy th3 b4s3 URL t0 sc4n
    -f FILE, -F FILE         Sp3c1fy 4 TXT f1l3 c0nt41n1ng URL t0 sc4n
    -o, -O                   Sp3c1fy 1f Y0U W4nt 4n 0utput f1l3 1n HTML
    -v, -V                   4dd 4 Pr1nt T0 Sh0w 1nf0 4b0ut 4ll R3sp0ns3s

    Example:
    python .py  -f url.txt -o N4M3 -v
    """

    print(help_text)

def format_url(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = "https://" + url
    return url


import sys
import threading
import time
from typing import Counter
from urllib.parse import urlparse
from xml.sax import parseString
from tabulate import tabulate
import requests


def animate():
    while True:
        for char in "/-\\|":
            print(f"\rSc4nn1ng 3n c0ur5 {char} ", end="", flush=True)
            time.sleep(0.2)


def H4X0R(URL=None, F1L3=None, OutPut=False, V3rb0s3=False, N4M3=None):
    T3ST3D = []
    response_counts = Counter()
    # Démarrer l'animation dans un thread séparé
    animation_thread = threading.Thread(target=animate)
    animation_thread.daemon = True
    animation_thread.start()

    headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Content-Type": "text/xml"
                }

    payload = """<?xml version="1.0" encoding="utf-8"?>
                <methodCall>
                <methodName>system.listMethods</methodName>
                <params></params>
                </methodCall>"""

    if F1L3:
        try:
            with open(F1L3, 'r') as file:
                L1ST3 = [line.strip() for line in file]
        except FileNotFoundError:
            sys.exit(f"3rr0r : F1l3 n0t f0und - {F1L3}")

        for _3L3M3NT5 in L1ST3:
            full_url = f"{_3L3M3NT5}/xmlrpc.php"
            if  full_url != "/xmlrpc.php":
                try:
                    response = requests.post(full_url, headers=headers, data=payload)
                    status_code = response.status_code
                    formatted_response = format_xml(response.text)
                    escaped_response = html.escape(formatted_response)
                    T3ST3D.append([full_url, status_code, f"<pre>{escaped_response}</pre>"])
                    response_counts[status_code] += 1
                except requests.RequestException as e:
                    T3ST3D.append([full_url, str(e), str(e)])
                    response_counts[str(e)] += 1
    elif URL:
        try:
            response = requests.post(f"{URL}/xmlrpc.php", headers=headers, data=payload)
            status_code = response.status_code
            formatted_response = format_xml(response.text)
            escaped_response = html.escape(formatted_response)
            T3ST3D.append([f"{URL}/xmlrpc.php", status_code, f"<pre>{escaped_response}</pre>"])
            response_counts[status_code] += 1
        except requests.RequestException as e:
            T3ST3D.append([f"{URL}/xmlrpc.php", str(e), str(e)])
            response_counts[str(e)] += 1


    if OutPut:
        OutPuT(T3ST3D, URL, N4M3)

    # Arrêter l'animation
    print("\r" + " " * 20 + "\r", end="", flush=True)  # Effacer le message
    # print(tabulate(T3ST3D, headers=["URL","C0D3", "R3SP0NS3"], tablefmt="rounded_grid"))
    print(f"F1L3 G3N3R4T3D ./{N4M3}.html")

    if V3rb0s3:
        print("\nSumm4ry 0f R3sp0ns3s:")
        summary = " / ".join([f"{count} r3sp0ns3s {code}" for code, count in response_counts.items()])
        print(summary)


def OutPuT(t4b, URL, N4M3):
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
        <h1>XML-RPC Test Results  </h1>
        {tabulate(t4b, headers=["URL", "C0D3", "R3SP0NS3"], tablefmt="unsafehtml")}
    </body>
    </html>
    """
    with open(f"./{N4M3}.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    return

def H3LP():
    help_text = """
    Us4g3: xmlrpc_f1nd3r.py [0pti0ns]

    0pti0ns:
    -h, --help, h, help      Sh0w this h3lp m3ss4g3 4nd 3xit
    -u URL, -U URL           Sp3c1fy 4 s1ngl3 URL t0 sc4n
    -f F1L3, -F F1L3         Sp3c1fy 4 TXT f1l3 c0nt41n1ng URLs t0 sc4n
    -o N4m3, -O N4m3         Sp3c1fy th3 n4m3 0f th3 0utput f1l3 1n HTML
    -v, -V                   4dd 4 pr1nt t0 sh0w 1nf0 4b0ut 4ll r3sp0ns3s

    N0t3:
    Y0u must us3 31th3r -u w1th 4 s1ngl3 URL 0r -f w1th 4 f1l3 c0nt41n1ng URLs.
    Y0u c4nn0t us3 b0th 0pti0ns s1mult4n30usly.

    Ex4mpl3:
    python xmlrpc_f1nd3r.py -u https://example.com -o r3sults -v
    python xmlrpc_f1nd3r.py -f url.txt -o r3sults -v
    """
    print(help_text)

def format_url(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = "https://" + url
    return url


def format_xml(xml_string):
    try:
        dom = parseString(xml_string)
        return dom.toprettyxml()
    except Exception as e:
        return xml_string


if __name__ == "__main__":
    C0mm4nd3 = sys.argv
    URL, P4TH_TO_F1L3, Outputn, V3rb0s3, N4M3 = None, None, False, False, None
    
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
        Ind3x = C0mm4nd3.index("-o") + 1 if "-o" in C0mm4nd3 else C0mm4nd3.index("-O") + 1
        if Ind3x < len(C0mm4nd3):
            N4M3 = C0mm4nd3[Ind3x]
        else:
            sys.exit("3rr0r : N0 f1l3 n4m3 f0und 4ft3r 0pt10n '-o'")
    
    if "-v" in C0mm4nd3 or "-V" in C0mm4nd3:
        V3rb0s3= True

    H4X0R(URL, P4TH_TO_F1L3, Outputn, V3rb0s3, N4M3)

