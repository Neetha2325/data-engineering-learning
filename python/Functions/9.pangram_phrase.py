import re

def check_if_pangram(phrase):
    letters=re.sub('[^a-zA-Z]','',phrase)
    letters_set=set(letters.lower())
    if len(letters_set)==26:
        return True
    else:
        return False

pan=check_if_pangram("The quick brown fox jumps over the lazy dog")
print(pan)
