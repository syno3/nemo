from colorama import Fore
from random_word import RandomWords

# some variables
r = RandomWords()

green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW

f_letter = list()

#banner for website
def banner():
    banner_text = '''
 ______   __     __   __     _____     __     __   __     ______        __   __     ______     __    __     ______    
/\  ___\ /\ \   /\ "-.\ \   /\  __-.  /\ \   /\ "-.\ \   /\  ___\      /\ "-.\ \   /\  ___\   /\ "-./  \   /\  __ \   
\ \  __\ \ \ \  \ \ \-.  \  \ \ \/\ \ \ \ \  \ \ \-.  \  \ \ \__ \     \ \ \-.  \  \ \  __\   \ \ \-./\ \  \ \ \/\ \  
 \ \_\    \ \_\  \ \_\\"\_\  \ \____-  \ \_\  \ \_\\"\_\  \ \_____\     \ \_\\"\_\  \ \_____\  \ \_\ \ \_\  \ \_____\ 
  \/_/     \/_/   \/_/ \/_/   \/____/   \/_/   \/_/ \/_/   \/_____/      \/_/ \/_/   \/_____/   \/_/  \/_/   \/_____/ 
                                                                                                                                                                                                                                           
NAME: Finding Nemo
VERSION: v1.0.1
DATE: 16/1/2021
CREATOR: festus murimi
EMAIL: synotechxvista@gmail.com
    '''
    #print(f"{green}{banner_text}")
    print(green+banner_text)

# collect user inputs from user
#check if input has only words
#strips spaces and store in new list called new_data
#separate words in new data to different strings
#get first letter of every word and store in new variable
#generate words based on letters

def mnemonics():
    data = input("please enter the words(use commas):  ")
    res = isinstance(data, str)
    if res is True:           
        new_data = [data.replace(' ', '')]
        #print(new_data)
    else:
       print("please only include letter")


banner()
mnemonics() 
    