# #Attempt to use DEF
# #attempt to use refactoring
# #attempt to decrement scores/timer
# #attempt to allow user to enter their name
# #attempt to add instruction on how to play
# #attempt to have correct letters show in terminal while game is playing
# #attempt to have player not be able to choose same letter multiple times per game
# #attempt to restrict player from using numbers and punctation.

# # to fix - decrement for attempts left show up twice. one with just the number and
# # the other time w attempts left


# #countries of europe to choose from
country = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia',]
# 'Denmark','Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland',
# 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands','Poland',
# 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden']

    # word = valid_country(country)
    # letters_in_word = [(word)]
    # guessed_letters = []
    # alphab = [set(string.ascii_uppercase)]
    # right_guess = []
    # wrong_guess = []
    # attempts_left = 6
    # hang_count = -1
    # player_guess = []

import random
import string
 
 
def pick_country(country):
    word = random.choice(country)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(country)
    print(word)
    return word.upper()
 
 
def hang_game():
    word = pick_country(country)
    letters_in_word = [(word)]
    guessed_letters = []
    alphab = set(string.ascii_uppercase)
    right_guess = []
    wrong_guess = []
    attempts_left = 6
    hang_count = -1
    player_guess = set() # this was a list which i tried to subtract from a set "alphab = set(string.ascii_uppercase)" - changed to set
 
    attempts_left = 50
 
    # getting user input
    while len(letters_in_word) > 0 and attempts_left > 0:
        # letters used
        # Used ' '.join(player_guess)) so it converts my set into individual letters --> 'e t c'
        print(attempts_left, ' Attempts left - So far you have chosen the letters: ', ' '.join(player_guess))
 
        # Puts the chosen country as "_" for each letter in the word 
        word_list = [letter if letter in player_guess else '_' for letter in word]
        print('Country: ', ' '.join(word_list))

        # Forcing player input the be uppercase for equality check later ==
        player_letter = input('Guess a letter: ').upper()
 
        # to fix - keep failing when got to this point. problem is that i apparently cant subtract list from a list or set to list
        if player_letter in alphab - player_guess:
 
            # to fix cant append as  i've changed from a list to a set. must add
            player_guess.add(player_letter)
            if player_letter in letters_in_word:
                letters_in_word.remove(player_letter)
                print('')
 
            else:
                attempts_left = attempts_left - 1  # takes away a life if incorrect
                print('\n',player_letter, 'is not in the chosen Country. Try again!')
        # Wont reduce attempts left if player uses a letter again
        elif player_letter in player_guess:
            print('\nYou have already tried that letter. Try again!')
        # due to import string and alphab = set(string.ascii_uppercase) player can only use letters a - z
        else:
            print('\nThat is not a valid letter. Try again!')
 
    # Game over or Congratulations code
    if attempts_left == 0:
        print("Your Attempts Are Over. You Were So Close, Try again.")
        print('The word was', word)
    else:
        print('YAY! You guessed the word', word.upper(), '!!')
 
hang_game()
