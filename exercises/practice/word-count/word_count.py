import re
import string
from collections import Counter, defaultdict


def count_words(sentence):
    result = defaultdict(int)
    curr_word = ""
    for char in sentence:
        if char.isdigit() or char.isalpha() or char in "'":
            curr_word += char
        else:
            result[curr_word.lower().strip("'")] += 1
            curr_word = ""

    result[curr_word.lower().strip("'")] += 1
    result.pop("", None)
    return result
