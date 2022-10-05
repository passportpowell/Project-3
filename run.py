#Attempt to use DEF
#attempt to use refactoring
#attempt to decrement scores/timer
#attempt to allow user to enter their name
#attempt to add instruction on how to play
#attempt to have correct letters show in terminal while game is playing
#attempt to have player not be able to choose same letter multiple times per game
#attempt to restrict player from using numbers and punctation.

# to fix - decrement for attempts left show up twice. one with just the number and 
# the other time w attempts left
#to fix - last letter doesn't show when all answers are correct
# to fix - use DEF function in code

import random

#countries of europe to choose from
# country =  ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia',
# 'Denmark','Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland',
# 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands','Poland', 
# 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden']

country = ['Slovakia', 'Slovenia', 'Spain', 'Sweden'] # to fix - use code above for country as this is for testing purpose

# print(country)

word = random.choice(country).lower()
# print(word) # to fix - remove this as it will show the answer


right_guess = []
wrong_guess = []
attempts_left = 6
hang_count = -1


while attempts_left > 0:
    chosen_letter = ''
    for letter in word:
        if letter in right_guess:
            chosen_letter += letter
        else:
            chosen_letter += '_ '
    if chosen_letter == word:
        break
    print(f"Guess the word, (Clue - {len(word)} Letters): ",chosen_letter)
    print(attempts_left," chances left \n")
    guess = input("Enter Guess Here: \n").lower()
    # code below is checking if we've already used a letter before 
    # regardlesws if it was correct or not
    if guess in right_guess or guess in wrong_guess:
        print("Already guessed", guess)

    #code below checks if guessed letter is in the word
    elif guess in word:
        print("Awesome Job! You guessed the correct letter!")
        right_guess.append(guess)

    #code below if for a incorrect guess and will decremnt the attempts by 1
    else:
        print("Sorry! You have guessed a wrong letter!")
        hangman_count = hang_count + 1
        attempts_left = attempts_left - 1 # to fix - attempts left wont decrement instead just shows -1
        wrong_guess.append(guess)
        print(attempts_left) # to fix - Print an image of hangman for each wrong answer

if attempts_left > 0:
    print(f"You Got The Country {word.upper()}, Congratulations!!!")
else:
    print("Your Attempts Are Over. You Were So Close Try again.")