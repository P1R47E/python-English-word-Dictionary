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
        elif suggestion =="N":
            return "sorry the word doesn't exist,please check it again"
        else:
            return "sorry we didn't understand your response"
    else:
        return "sorry the word doesn't exist,please check it again"
word = input("Please Enter the word to translate: ")
output = (translator(word))

if type(output) == list:
    for item in output:#to ommit the list from when output the definition
        print(item)
else:
    print(output)