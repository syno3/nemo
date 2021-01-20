import re
from mnemonics import loading, mnemonics
import random


#get file used
def wordGen(result):
    word_choice = []
    try:
        file = open("words.txt", "r")
        file_content = file.read()
        #iterate over value and convert to independent words
        file_content = re.sub("[^\w]", " ",  file_content).split()
    except UnboundLocalError:
        print("file does not exist")
    #iterrate over the words in results
    #find first letters of string and compare to result
    #check if word has more than 3 and less than 6 letters
    for k in result:
        for word in file_content: 
            if word[0] == k and len(word) >3 and len(word) < 7:
                word = re.sub("[^\w]", " ",  word).split()
                word_choice += word
#pick random
#pick random and store in new string
#return the result

