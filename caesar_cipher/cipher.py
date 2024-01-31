def encrypt(plain_text, shift_key):
    """
    
    """

    number_of_characters = 26
    upper_base_code = ord("A")
    lower_base_code = ord("a")

    encrypted_text = ""

    for char in plain_text:

        if char.isalpha():
            
            # find char unicode and the base case unicode depending on upper/lower case
            plain_code = ord(char)
            base_code = upper_base_code if char.isupper() else lower_base_code
            # determine index of char and the shifted char in alphabet
            plain_index = plain_code - base_code
            shifted_index = (plain_index + shift_key) % number_of_characters
            # find shifted char
            shifted_code = base_code + shifted_index
            encrypted_text += chr(shifted_code)

        else:

            encrypted_text += char

    return encrypted_text

def decrypt(encrypted_text, shift_key):
    """
    
    """

    return encrypt(encrypted_text, -shift_key)

def crack(encrypted_text):
    """
    
    """
