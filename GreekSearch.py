import json
from Class_Alphabet import Alphabet

# Anything with a # is something I got online
# from https://realpython.com/python-json/#reading
# -json-with-python

# Also saw image online as to how a json file
# should look like 

def verb_search(word: str): 

    with open("Shelmerdine_verbs.json", 'r') as file: #
        verbs = json.load(file) # 
        if word in verbs.keys():
            return verbs[word]
        return "Not Found"
        


def noun_search(word: str): 

    with open("Shelmerdine_nouns.json", 'r') as file: #
        nouns = json.load(file) #
        if word in nouns.keys():
            return nouns[word]
        return "Not Found"


        
def catagorey_checker(word:str):
    attempts = 0
    valid = ['nouns', 'verbs', 'END', '1', '2', '3']
    while attempts <= 3:
        word1 = word.strip().lower()
        if word1 in valid:
            print('')
            return word1
        else:
            attempts += 1 
            if attempts == 4:
                break
            word = input(
                f"Please enter a valid entry (Attempt {attempts}/3) --> ")
    raise TypeError(
        "MAX Attempts Reached. Please Start Program Again to Search.")
                


    

def main_sequence(WorD):

    count = 0
    while count < 999:

        WorD = catagorey_checker(
            input(
        "What are you looking for?  Nouns (1), Verbs (2), END (3)? "))
    
        if WorD == 'END' or WorD == '3':
            count = 999
            return print("Program Has Ended.") 

        elif WorD == 'nouns' or WorD == '1':
            WorD = input("What's the greek word? ")
            value = noun_search(WorD)
            WorD = Alphabet(value)
            value = WorD.file_checker(value)
            print('')
            print('')
            print(f'FOUND: >>> {value} <<<')
            count += 1
            print('')
            print('')
            print('')
            print("Wanna search again? ") 

        elif WorD == 'verbs' or WorD == '2':
            WorD = input("What's the greek word? ")
            value = verb_search(WorD)
            WorD = Alphabet(value)
            value = WorD.file_checker(value)
            print('')
            print('')
            print(f'Found: >>> {value} <<<')
            count += 1
            print('')
            print('')
            print('')
            print("Wanna search again? ") 
    print(
    "MAX Search Limit Reached. Restart Program to Keep Searching.")




def main():
    print('Hello and Welcome to εὑρίσκω! A vocabulary search tool', end=' ')
    print("for Shelmerdine & Shelmerdine's Introduction to Greek", end=' ')
    print("(3rd Edition) textbook. With this tool, you can search", end=' ')
    print("for verbs and nouns from up to Chapter 3", end=' ')
    print("and discover not only english definitions, but also", end=' ')
    print("important accompanying information about the terms searched!")
    print('')
    print("Structure of Verb Definitions: Person / Number / Tense /", end=' ')
    print("Mood / Voice of (Sing/1st/Indicitive form of variant word", end=' ')
    print("searched, if applicable) - 'English Definition, Alternative", end=' ')
    print("English Definition (same meaning, different word) (if applicable);", end=' ')
    print("Alternative Definition (related to definition prior to the", end=' ')
    print("semicolon but with potentially a different meaning) (if applicable)")
    print('')
    print("Structure of Noun Definitions: Case Name / Person / Gender", end=' ')
    print("- 'English definition 1' and/or 'English definition 2' (if applicable)")
    print('')
    input('<< Press ENTER to start program >> ')
    print('')
    WorD = ""
    main_sequence(WorD)
    print(
    "Thank you for using εὑρίσκω!")
        




if __name__ == "__main__":
    main()
