def get_available_words(word_length, dictionary):
    available_words = []
    for word in dictionary:
        if len(word) == word_length:
            available_words.append(word)
    return available_words

def guess_letter(word_length, selected_word, guessed_word):
    char_guess = input("Guess a letter: ")
    while not(char_guess >= 'a' and char_guess <= "z"):
        char_guess = input("Please enter valid letter: ")
    # if char_guess >= 'a' and char_guess <= "z":
    for x in range(word_length):
        guess_word_index = selected_word.find(char_guess, x)
        if guess_word_index != -1:
            guessed_word[guess_word_index] = char_guess
    return guessed_word
