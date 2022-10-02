# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
# pip install country_list

#Looking for whole words for simplicity with no spaces or punctutaion
# All guesses are to be upper case alongside country names

def whole_word(country_list):
    word = random.choice(country_list) #should choose random word from the country list i installed
    while '-' in word or ' ' in word or '.' in word:
        word = random.choice(country_list)

    return word.upper() #I wan tcapital letters 


#to fix - allows me to put in numbers, punctuation which i do not want
def country_hangman():
    word = whole_word(country_list)
    letters = set(country_list) #this should be used save all guesses/ might need it as an array instead
    guessed_letters = set() #players guessed letter saved here

    if player in letter - guessed_letters:
        guessed_letters.add(player)
        if player in letters:
            letters.remove(player)
            
    elif player in guessed_letters:
        print("You Have Already Tried This Letter!")

    else: 
        print("You've Not Chosen A Letter! Try Again")

player = input("Guess a letter: \n").upper() #upper to conver letter in upper case
print(player) 
