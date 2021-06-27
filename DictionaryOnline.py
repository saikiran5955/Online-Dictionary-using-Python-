# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 11:23:03 2020

@author: SaiKiran
"""

import json
from difflib import get_close_matches #import get_close_matches from the difflib library.

data = json.load(open("data.json")) #To load json file.

def translate(w):
    w=w.lower() #for case sensitivity.
    #To check if word lies in the data.
    if w in data:
        return data[w]
    #To get close matching word.
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead?\nEnter Y if yes or N if no :\n"%get_close_matches(w,data.keys())[0])
        yn = yn.lower()
        if yn=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="n":
            return "The word doesn't exist! Please enter some valid word!"
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist. Please double check it."
    
word=input("Enter word:")
output = translate(word)
#To print meaning of the word.
if type(output) == list:
    for item in output:
        print(item)
        
else:
    print(output)
input('Press Enter to Exit')

        
    