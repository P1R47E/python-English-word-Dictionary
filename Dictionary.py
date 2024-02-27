import difflib #difflib is a library here
import json
from difflib import get_close_matches #optional as SequenceMatcher(Read it later)

"""get_close_matches module returns the ratio of the desired word with compared in the possibilities"""
data = json.load(open("data.json"))
def translator(words):
    words = words.lower()
    if words in data:
        
        return data[words]
    elif len(get_close_matches(words,data.keys())) > 0:#means if the returned list is not empty
        suggestion = input("Did you mean %s instead? Enter Y if yes or N if no: " %get_close_matches(words,data.keys())[0])
        suggestion = suggestion.upper()
        if suggestion == "Y":
            return data[get_close_matches(words,data.keys())[0]]