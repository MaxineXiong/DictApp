# Hint1: SequenceMatcher
# Check https://docs.python.org/3/library/index.html to look up a standard library to import
import difflib
from difflib import SequenceMatcher
SequenceMatcher(None, 'rainn', 'rain').ratio()     #to return similarity ratio between 'rainn' and 'rain'
SequenceMatcher(lambda x: x == ' ', 'rain n', 'rain').ratio()    #ignore the junk ' '

# Hint2: get_close_matches
from difflib import get_close_matches
get_close_matches('rainn', ['rain', 'paranormal', 'as', 'cloud', 'rainy'], n=5, cutoff=0.8)  # n=5: return 5 closest matches  #cutoff=0.8: similarity ratio must be at least 80%


# SOLUTION:

# Load .json file
import json    #.json file contains a huge list
data = json.load(open('data.json'))

word = input('Enter word: ').lower()
if word in data.keys():
    for i in data[word]:
        print('Meaning', data[word].index(i)+1)
        print(i)

elif word.title() in data.keys():
    for i in data[word.title()]:
        print('Meaning', data[word.title()].index(i)+1)
        print(i)

elif word.upper() in data.keys():
    for i in data[word.upper()]:
        print('Meaning', data[word.upper()].index(i)+1)
        print(i)

elif get_close_matches(word, data.keys(), cutoff=0.8) != []:
    matchlist = get_close_matches(word, data.keys(), n=5, cutoff=0.8)
    m = 0
    YorN_list = []
    while m < len(matchlist):
        match = matchlist[m]
        YorN = input('Did you mean {} instead? Enter Y if yes, or N if no: '.format(match))
        YorN_list.append(YorN)
        if YorN == 'Y':
            for i in data[match]:
                print('Meaning', data[match].index(i)+1)
                print(i)
            break
        elif YorN == 'N':
            m = m + 1
            continue
        else:
            continue

    if YorN_list[-1] == 'N':
        print('The word does not exist. Please double check it.')

else:
    print('The word does not exist. Please double check it')
