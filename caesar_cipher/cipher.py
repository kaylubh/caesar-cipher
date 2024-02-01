from caesar_cipher.english_checker import count_english_words

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

    # stores the decrypted text candidates and their associated counts of english words for evaluation
    decrypted_text_candidates = {}

    # run the text through decrypt with all possible shift values
    for shift_key_candidate in range(26):

        decrypted_text_candidate = decrypt(encrypted_text, shift_key_candidate)
        decrypted_text_candidates[decrypted_text_candidate] = None

    # count the english words in each possible decryption
    for candidate in decrypted_text_candidates:

        english_word_count = count_english_words(candidate)
        decrypted_text_candidates[candidate] = english_word_count

    # find the decrypted text candidate with the highest english word count
    # likely is the correct decryption
    likely_decrypted_text = max(decrypted_text_candidates, key=decrypted_text_candidates.get)

    # check the likely decrypted text to ensure it is mostly english words
    # return an empty string "" if the most likely decrypted text contains less than 50% english words
    decrypted_text = ""
    likely_decrypted_text_words = likely_decrypted_text.split()
    english_word_count = decrypted_text_candidates[likely_decrypted_text]
    english_words_percentage = (english_word_count / len(likely_decrypted_text_words)) * 100

    if english_words_percentage >= 50:
        decrypted_text = likely_decrypted_text

    return decrypted_text
