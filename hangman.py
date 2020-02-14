#import PyDictionary as pyd
import random
import requests
import json
from os.path import dirname

print(dirname(__file__))

word_length_str = input("what length should the word be (3-10)?")
try:
    word_length = int(word_length_str)
    if word_length < 3 or word_length > 10:
        1/0
except:
    print("Please input valid number")

guess_tries = input("How many guesses would you like(2-10)")
try:
    guess_tries = int(guess_tries)
    if guess_tries < 2 or guess_tries > 10:
        1/0
except:
    print("Please input valid number")

dictionary = []
url = "https://raw.githubusercontent.com/adambom/dictionary/master/dictionary.json"
r = requests.get(url)
response = r.json()
# filename = "c:/Users/mark/pyworkspace/hangman/output.json"
# with open(filename, "w") as f:
#     json.dump(response, f, indent=4)
dictionary = list(response.keys())
# print(len(dictionary[0]))

def filter_words(word):
    if len(word) == word_length:
        return True
    else:
        return False
available_words = []
filtered_dict = filter(filter_words, dictionary)

for word in filtered_dict:
    available_words.append(word)
print(available_words[0])
print(available_words[1])
print(len(available_words))




