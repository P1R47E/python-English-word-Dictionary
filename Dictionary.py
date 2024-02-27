import difflib #difflib is a library here
import json
from difflib import get_close_matches #optional as SequenceMatcher(Read it later)

"""get_close_matches module returns the ratio of the desired word with compared in the possibilities"""
data = json.load(open("data.json"))
def translator(words):
    words = words.lower()