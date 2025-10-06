import base64

def hex_to_base64(hex_str):
    """
    Convert a hex string to a base64 encoded string.
    """
    # Remove possible whitespace and lowercase
    hex_str = hex_str.strip().lower()
    # Convert hex to bytes
    byte_data = bytes.fromhex(hex_str)
    print(byte_data)
    # Encode bytes to base64
    base64_str = base64.b64encode(byte_data).decode('utf-8')
    return base64_str

if __name__ == "__main__":
    # Example usage
    hex_input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(hex_to_base64(hex_input))