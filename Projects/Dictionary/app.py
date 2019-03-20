import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        print("Did you mean %s instead?" % get_close_matches(word,data.keys())[0])
        while True:
            cmd = input("Yes(Y)/No(N)")
            cmd = cmd.lower()
            if cmd == 'y':
                return data[get_close_matches(word,data.keys())[0]]
            elif cmd == 'n':
                return "The word doesn't exist in your dictionary."
            else :
                print("Wrong input")
    else :
        return "The word doesn't exist in your dictionary."

while True:
    word = input("Enter word: ")
    word = word.lower()
    meaning = translate(word)
    if type(meaning) == list :
        for item in meaning:
            print(item)
    else :
        print(meaning)
