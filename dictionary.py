import json

#a library for closely matched spellings. E.g., Did you mean?
import difflib

#SequenceMatcher(None,'rainn','rain').ratio()
#first argument isjunk, if compare two blocks of texts, can define what to ignore

#get_close_matches(word, possibilities,n=3,cutoff=0.6)
#return the 3 most similar strings as the word; ration >= .6
from difflib import SequenceMatcher, get_close_matches

data=json.load(open('data.json'))

key=input('Enter the word: ')
key=key.lower()
dym=get_close_matches(key,data.keys(),n=3)

def find_meaning():
    if key in data:
        return data[key]
    if key.title() in data:
        return data[key.title()]
    elif len(dym)>0:
        for i in dym:
            choice=input('Did you mean '+i + ' Y/N ')
            if choice=='N' or choice=='n':
                if dym.index(i)==2:
                    return 'No close match'
                continue
            elif choice=='Y' or choice=='y':
                return data[i]
                break
            else:
                return 'Only Y or N are allowed as input!'

    else:
        return 'Word does not exist!'

print(find_meaning())
