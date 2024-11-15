import base64
import gzip
import sys

def decode_input(encoded_input):
    # Décode le Base64
    decoded = base64.b64decode(encoded_input)
    
    # Décompresse avec gzip
    decompressed = gzip.decompress(decoded)
    
    # Retourne le résultat décodé en tant que chaîne
    return decompressed.decode('utf-8')

def encode_input(input_string):
    # Encode la chaîne en bytes
    input_bytes = input_string.encode('utf-8')
    
    # Compresse avec gzip
    compressed = gzip.compress(input_bytes)
    
    # Encode en Base64
    encoded = base64.b64encode(compressed)
    
    # Retourne le résultat encodé en tant que chaîne
    return encoded.decode('utf-8')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py [encode/decode] [input]")
        sys.exit(1)

    action = sys.argv[1]
    input_data = sys.argv[2]

    if action == "decode":
        result = decode_input(input_data)
        print(f"Decoded: {result}")
    elif action == "encode":
        result = encode_input(input_data)
        print(f"Encoded: {result}")
    else:
        print("Invalid action. Use 'encode' or 'decode'.")
