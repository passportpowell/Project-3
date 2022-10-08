# attempt to use DEF
# attempt to import somthing and use it
# attempt to use refactoring
# attempt to decrement scores/timer
# attempt to allow user to enter their name
# attempt to add instruction on how to play
# attempt to have correct letters show in terminal while game is playing
# attempt to have player not be able to choose same letter multiple times per game
# attempt to restrict player from using numbers and punctation.

# to fix - decrement for attempts left show up twice. one with just the number and 
# the other time w attempts left
# to fix - last letter doesn't show when all answers are correct
# to fix - use DEF function in code
# to fix - if multiple of the same letter ONLY the 1st occurance is shown instead of all. Fixed by finding out i had to use 
# enumerate() function. solutions found her https://stackoverflow.com/questions/27662404/trying-to-find-the-same-item-in-a-list-with-the-context-of-hangman 
# https://stackoverflow.com/questions/63922601/how-to-build-a-list-with-the-duplicated-letters-from-another-string-python-h

# to fix - Game wont end after correctly guessing
# to fix - attempts won decrement. Fixed by realising that i had not spell checked.
# To fix - have image of a hangman progress each time answer is wrong
# to fix - Want this code for elif G to pick a random word fromm all the above countries



import random
import string


country_europe = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia',
'Denmark','Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland',
'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands','Poland',
'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden']

country_south_america = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'French Guiana', 
'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']

country_central_america = ['Belize', 'Costa Rica', 'El Salvador', 'Guatemala', 'Honduras', 'Nicaragua', 'Panama']

country_africa = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cape Verde', 'Cameroon', 
'Central', 'Chad', 'Comoros', 'Congo', 'Djibouti', 'Egypt', 'Guinea', 
'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'The', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Ivory Coast', 'Kenya', 'Lesotho', 
'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 
'Rwanda', 'Sao', 'Tome Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South', 'Sudan', 'Sudan', 
'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']

country_asia = [ 'Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'British', 'Indian', 'Brunei', 'Cambodia', 'China', 
'Georgia,', 'Hong', 'Kong', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 
'Laos', 'Lebanon', 'Macau', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North', 'Korea', 'Oman', 'Pakistan', 'Palestine', 
'Philippines', 'Qatar', 'Saudi', 'Arabia', 'Singapore', 'South', 'Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 
'Timor-Leste', 'Timor', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen']

Oceana = ['Australia', 'Fiji', 'Kiribati', 'Marshall', 'Islands', 'Micronesia', 'Nauru', 'New', 'Zealand', 'Palau', 'Papua', 'New', 
'Guinea', 'Samoa', 'Solomon', 'Islands', 'Tonga', 'Tuvalu', 'Vanuatu']

# This code picks a random country depending on the category that the player chooses
def pick_country():
    print("-----------------------------------------------------------------")
    print("Welcome to Hangman!")
    print("----------------------------------------------------------------- \n")
    category = input("What Category would you like to play? \nA - Europe, \nB - South america \nC - Central America \nD - Africa \nE - Asia \nF - Oceana \nG - All \n: ".upper())

    # while category not in ("A", "B", "C", "D", "E", "F"):
    # while True:
    if category.upper() == "A":
        word = random.choice(country_europe)    
        while '-' in word or ' ' in word:
            word = random.choice(country_europe)
        print(word)  #  print(word) # to fix - remove this as it will show the answer
        return word.upper()
    elif category.upper() == "B":
        word = random.choice(country_south_america)    
        while '-' in word or ' ' in word:
            word = random.choice(country_south_america)
        print(word)  #  print(word) # to fix - remove this as it will show the answer
        return word.upper()

    elif category.upper() == "C":
        word = random.choice(country_central_america)    
        while '-' in word or ' ' in word:
            word = random.choice(country_central_america)
        print(word)  #  print(word) # to fix - remove this as it will show the answer
        return word.upper()

    elif category.upper() == "D":
        word = random.choice(country_africa)    
        while '-' in word or ' ' in word:
            word = random.choice(country_africa)
        print(word)  #  print(word) # to fix - remove this as it will show the answer
        return word.upper()

    elif category.upper() == "E":
        word = random.choice(country_asia)    
        while '-' in word or ' ' in word:
            word = random.choice(country_asia)
        print(word)  #  print(word) # to fix - remove this as it will show the answer
        return word.upper()

    elif category.upper() == "F":
        word = random.choice(Oceana)    
        while '-' in word or ' ' in word:
            word = random.choice(Oceana)
        print(word)  #  print(word) # to fix - remove this as it will show the answer
        return word.upper()

    # to fix - Want this code to pick a random word fromm all the above countries
    # elif category.upper() == "G":
    #     word = random.choice(country_south_america, country_europe, country_central_america, country_africa, country_asia, Oceana)    
    #     while '-' in word or ' ' in word:
    #         word = random.choice(country_south_america, country_europe, country_central_america, country_africa, country_asia, Oceana)
    #     print(word)  #  print(word) # to fix - remove this as it will show the answer
    #     return word.upper()                     

    else:
        print("Invalid Category. Please Try Again!....")
        pick_country()
        # exit()
    
 
def hang_game(word):
    country_chosen = "_" * len(word)  # Puts the chosen country as "_" for each letter in the word 

    player_won = False
    used_letters = []
    used_words = []
    attempts_left = 10

    print(f"You have", {attempts_left}, "attempts to guess the country name")
    print("----------------------------------------------------------------- \n")

    print(word)
    print("\n")

    while not player_won and attempts_left > 0:



        # Forcing player input the be uppercase for equality check later ==     
        player_guess = input("Please guess a letter or word: \n").upper()

        # if loop for 3 conditions (Word, Letter or other which should result in an invalid message))

        # if guess is a letter character and a letter a-z (.isalpha)
        if len(player_guess) == 1 and player_guess.isalpha():
            if player_guess in used_letters:
                # Used ' '.join(player_guess)) so it converts my set into individual letters --> 'e t c'
                print("You've already tried the letter: ", player_guess)
                print("So far you have chosen the letters: ", " ".join(used_letters))
                
            elif player_guess not in word:
                print(player_guess, "is not in the chosen Country. Try again!")
                # Use += or -+
                attempts_left -= 1
                print("You Have", attempts_left)
                #  print()   To fix - have image of a hangman each time answer is wrong                
                used_letters.append(player_guess)  # adds letter chosen to list

            else:
                print("Excellent,", player_guess, "'is in the chosen Country. Keep Going!")
                used_letters.append(player_guess)
                # word_list = [letter if letter in used_letters or used_words else '_' for letter in word_completion]
                # print('Country: ', ' '.join(word_list))
 
                # To update the country_chosen variable and show the player where the correct chosen letters appear
                country_as_list = list(country_chosen)
                #  Want the index and letter at the index. code should replace "_" with the correct guesses
                indices = [i for i, letter in enumerate(word) if letter == player_guess]
                for index in indices:
                    country_as_list[index] = player_guess
                country_chosen = "".join(country_as_list)
                if "_" not in country_chosen:
                    player_won = True

        # if guess is a whole word and characters are from a-z (.isalpha)              
        elif len(player_guess) == len(word) and player_guess.isalpha():

            if player_guess in used_words:
                print("You already Tried the Country", player_guess)

            elif player_guess != word:
                print(player_guess, "is not the Country.")
                attempts_left -= 1
                print("You Have", attempts_left)
                #  print()   To fix - have image of a hangman each time answer is wrong
                used_words.append(player_guess)

            else:
                player_won = True  # If player manages to work out the country the game should end here and offer a new game
                country_chosen = word

        else:
            print("Not a valid guess.")
        print(country_chosen)
        print("\n")

    if player_won:
        print('YAY! You guessed the word', word.upper(), '!!')

    # Game over or Congratulations code
    else:
        print("Your Attempts Are Over. You Were So Close, Try again.")
        print('The word was: ', word.upper()) 
 
def main():
    word = pick_country()
    hang_game(word)

    # While loop to get game to restart from the beginning if player put Y or YES in
    while input("hang_game Again? (Y-YES/N-NO) \n").upper() == "Y" or "YES":
        word = pick_country()
        hang_game(word)
 
 
if __name__ == "__main__":
    main()