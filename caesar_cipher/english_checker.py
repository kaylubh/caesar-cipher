from caesar_cipher.corpus import word_list, name_list


def count_english_words(text):
    """
    
    """

    candidate_words = []
    english_words_count = 0

    # remove all characters that are not letters
    for word in text.split(): 

        candidate_word = ""

        for char in word:
            
            if char.isalpha():
                candidate_word += char

        candidate_words.append(candidate_word)

    # check candidate word against english corpus
    for word in candidate_words:

        if word.lower() in word_list or word in name_list:
            english_words_count += 1

    return english_words_count
