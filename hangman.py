#import PyDictionary as pyd
import random
import requests
import json
from os.path import dirname
import filter_words

print(dirname(__file__))

word_length_str = input("what length should the word be (3-10)?")
try:
    word_length = int(word_length_str)
    if word_length < 3 or word_length > 10:
        1/0
except:
    print("Please input valid number")

guess_limit_str = input("How many guesses would you like(2-10)")
try:
    guess_limit = int(guess_limit_str)
    if guess_limit < 2 or guess_tries > 10:
        1/0
except:
    print("Please input valid number")

#initialize word guess list
guessed_word = []
for x in range(word_length):
    guessed_word.append(" ")
dictionary = []
# url = "https://raw.githubusercontent.com/adambom/dictionary/master/dictionary.json"
# r = requests.get(url)
# response = r.json()
filename = "c:/Users/mark/pyworkspace/hangman/output.json"
# with open(filename, "w") as f:
#     json.dump(response, f, indent=4)
with open(filename, "r") as f:
    response = json.load(f)
dictionary = list(response.keys())
available_words = filter_words.get_available_words(word_length, dictionary)


print(available_words[0])
print(available_words[1])
print(len(available_words))

word_index = random.randint(0, len(available_words))
# selected_word = available_words[word_index]
selected_word = "test"
guess_tries = 0
while guess_tries < guess_limit:
    guessed_word = filter_words.guess_letter(word_length, selected_word, guessed_word)
    print("".join(guessed_word))
    guess_tries = guess_tries + 1
    if selected_word == "".join(guessed_word):
        print("Congrats: You Did It!!!")
        break




    




