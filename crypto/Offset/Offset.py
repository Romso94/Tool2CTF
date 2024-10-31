import argparse

def encrypt(data, key):
    response =""
    for char in data:
        if ord(char) + key >127:
            valeur = ord(char) - key 
        else :
            valeur = ord(char) + key
        response += chr(valeur)
    print(f"Flag Encrypted, key : {key}")        
    return response



def decrypt(data, key=None, flag=None):
    response = ""
    if key!=None:
        for char in data:
                if ord(char) + key >127:
                    valeur = ord(char) - key 
                else :
                    valeur = ord(char) + key
                response += chr(valeur)
        print(f"Flag Decrypted, key : {key}")        
        return response
    if flag!=None:
        _key = ord(flag[0])-ord(data[0])
        if ord(flag[1])-ord(data[1])!=_key : 
            return "Can't decrypt this !" 
        else : 
            for char in data:
                if ord(char) + _key >127:
                    valeur = ord(char) - _key 
                else :
                    valeur = ord(char) + _key
                response += chr(valeur)
            print(f"Flag Decrypted, key : {_key}")
            return response

def help_message():
    print("""
Simple Offset Tool
Description : This script provides a simple command-line tool for encrypting and decrypting data using a specified Offset or part (at least 2 char minimum) from the decrypted text.

Usage: Offset.py [options] ( -e | -d )

Options:
  -h, --help       Show this help message and exit
  -e, --encrypt DATA  Data to encrypt
  -d, --decrypt DATA  Data to decrypt
  -key KEY          Key for encryption (required if -e is used)
  -flag FLAG        Optional flag for decryption

Exemple : 
 python3 .\Offset.py -d '$E2Cw24<LrbDcccC0cF0|JDEbCb05b0=c0$c=c5bN' -flag "StarHack{"
 python3 .\Offset.py -e '$E2Cw24<LrbDcccC0cF0|JDEbCb05b0=c0$c=c5bN' -key 47
""")

def main():
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt data based on the provided option.",
        epilog="Examples:\n"
            " python3 Offset.py -d '$E2Cw24<LrbDcccC0cF0|JDEbCb05b0=c0$c=c5bN' -flag \"StarHack{\"\n"
            " python3 Offset.py -e '$E2Cw24<LrbDcccC0cF0|JDEbCb05b0=c0$c=c5bN' -key 47",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", "--encrypt", metavar="DATA", type=str, 
                        help="Data to encrypt (required if -e is used)")
    group.add_argument("-d", "--decrypt", metavar="DATA", type=str, 
                        help="Data to decrypt (required if -d is used)")
    
    parser.add_argument("-key", metavar="KEY", type=int, 
                        help="Key for encryption (required if -e is used)")
    
    parser.add_argument("-flag", metavar="FLAG", type=str, 
                        help="Optional flag for decryption")

    args = parser.parse_args()


    if args.encrypt and args.decrypt:
        parser.error("Please use either -e for encryption or -d for decryption, not both.")
    
        
    if args.encrypt:
        if not args.key:
            parser.error("The -key option is required when using -e for encryption.")
        result = encrypt(args.encrypt, args.key)
        print(result)


    elif args.decrypt:
        if not args.key and not args.flag : 
            parser.error("For decryption, you need to specify at least one argument: either -key or -flag.")
        result = decrypt(args.decrypt, args.key, args.flag)
        print(result)

if __name__ == "__main__":
    main()