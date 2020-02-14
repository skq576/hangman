import PyDictionary as pyd
import random
import requests
import json

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

dictionary = {}
url = "https://github.com/adambom/dictionary/blob/master/dictionary.json"
r = requests.get(url)
dictionary = r.json()
print(dictionary[1])

