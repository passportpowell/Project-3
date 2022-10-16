import random

#  countries of europe to choose from
country = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia',
'Denmark','Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland',
'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands','Poland',
'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden']

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
'Laos', 'Lebanon', 'Macau', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 
'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 
'Timor-Leste', 'Timor', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen']

Oceana = ['Australia', 'Fiji', 'Kiribati', 'Marshall', 'Islands', 'Micronesia', 'Nauru', 'New Zealand', 'Palau', 'Papua New Guinea', 'Samoa', 'Solomon', 'Islands', 'Tonga', 'Tuvalu', 'Vanuatu']


def hangman_pic(attempts_left):

    #  Code should show each phaze of the hangman depending upon how many attempts the player has left
    if attempts_left == 7:
        print("  |         \n")
        print("  |      \n")
        print("  |      \n")
        print("  |      \n")
        print("  |      \n")
        print("__|__\n")

    if attempts_left == 6:
        print("   _________ \n")
        print("  |         \n")
        print("  |      \n")
        print("  |      \n")
        print("  |      \n")
        print("  |      \n")
        print("__|__\n")

    if attempts_left == 5:
        print("   _________ \n")
        print("  |        | \n")
        print("  |        | \n")
        print("  |        O \n")
        print("  |         \n")
        print("  |      \n")
        print("__|__\n")

    if attempts_left == 4:
        print("   _________ \n")
        print("  |        | \n")
        print("  |        | \n")
        print("  |        O \n")
        print("  |         \n")
        print("  |      \n")
        print("__|__\n")

    if attempts_left == 3:        
        print("   _________ \n")
        print("  |        | \n")
        print("  |        | \n")
        print("  |        O \n")
        print("  |       / \ \n")
        print("  |      \n")
        print("__|__\n")

    if attempts_left == 2:    
        print("   _________ \n")
        print("  |        | \n")
        print("  |        | \n")
        print("  |        O \n")
        print("  |       /|\ \n")
        print("  |      \n")
        print("__|__\n")

    if attempts_left == 1:
        print("   _________ \n")
        print("  |        | \n")
        print("  |        | \n")
        print("  |        O \n")
        print("  |       /|\ \n")
        print("  |       /  \n")
        print("__|__\n")

    if attempts_left == 0:
        print("   _________ \n")
        print("  |        | \n")
        print("  |        | \n")
        print("  |        O \n")
        print("  |       /|\ \n")
        print("  |       / \ \n")
        print("__|__\n")


#  Code below if for the random selection of a country for the game based upon what category the player chooses.
#  Also removed options for word with punctuations and spaces inbetween using a while
def pick_country():
    print("-----------------------------------------------------------------")
    print("Welcome to Hangman!")
    print("----------------------------------------------------------------- \n")
    category = input("What Category would you like to play? \nA - Europe, \nB - South america \nC - Central America \nD - Africa \nE - Asia \nF - Oceana \nG - All: ".upper())

    if category.upper() == "A" or category.upper() == "":
        word = random.choice(country_europe)
        while '-' in word or ' ' in word:
            word = random.choice(country_europe)
        return word.upper()

    elif category.upper() == "B":
        word = random.choice(country_south_america)
        while '-' in word or ' ' in word:
            word = random.choice(country_south_america)
        return word.upper()

    elif category.upper() == "C":
        word = random.choice(country_central_america)
        while '-' in word or ' ' in word:
            word = random.choice(country_central_america)
        return word.upper()

    elif category.upper() == "D":
        word = random.choice(country_africa)
        while '-' in word or ' ' in word:
            word = random.choice(country_africa)
        return word.upper()

    elif category.upper() == "E":
        word = random.choice(country_asia)
        while '-' in word or ' ' in word:
            word = random.choice(country_asia)
        return word.upper()

    elif category.upper() == "F":
        word = random.choice(Oceana)
        while '-' in word or ' ' in word:
            word = random.choice(Oceana)
        return word.upper()

    elif category.upper() == "G":
        word = random.choice(Oceana + country_europe + country_africa + country_asia + country_south_america + country_central_america)
        while '-' in word or ' ' in word:
            word = random.choice(Oceana + country_europe + country_africa + country_asia + country_south_america + country_central_america)
        return word.upper()

    else:
        print("Invalid Category. Please Try Again!....")
        pick_country()


def hang_game(word):

    # Puts the chosen country as "_" for each letter in the word
    country_chosen = "_ " * len(word)
    # for use when changed to True upon completion and used to allow game to end
    player_won = False
    #  Used letters and word list used to store player choices and used to show back to player upon using the same letter again.
    used_letters = []
    used_words = []
    attempts_left = 10

    print("-----------------------------------------------------------------")
    print("Welcome to Hangman!")
    print("You have", attempts_left, "attempts to guess the country name")
    print("----------------------------------------------------------------- \n")

    print("\n")

    while not player_won and attempts_left > 0:
        # Forcing player input the be uppercase for equality check later == 
        print(len(word), "Letters in the word")    
        player_guess = input("Please guess a letter or word: ").upper()

        # if loop for 3 conditions (Word, Letter or other which should result in an invalid message))
        # also checks if the player guess is a letter character and a letter a-z (.isalpha)
        if len(player_guess) == 1 and player_guess.isalpha():
            if player_guess in used_letters:
                # Used ' '.join(player_guess)) so it converts my set into individual letters --> 'e t c'
                print("You've already tried the letter: ", player_guess)
                print("So far you have chosen the letters: ", " ".join(used_letters))
               
            elif player_guess not in word:
                print(player_guess, "is not in the chosen Country. Try again!")
                attempts_left -= 1
                print("You Have", attempts_left, "attempts remaining!")
                if attempts_left <= 7:
                    hangman_pic(attempts_left)
                # adds letter chosen by player to list of used letters
                used_letters.append(player_guess)  

            else:
                # Code below ends the game if the player got character correct
                print("Excellent,", player_guess, "'is in the chosen Country. Keep Going!")
                used_letters.append(player_guess)
                word_as_list = list(country_chosen)
                indices = [i for i, letter in enumerate(word) if letter == player_guess]
                for index in indices:
                    word_as_list[index] = player_guess
                country_chosen = "".join(word_as_list)
                if "_" not in country_chosen:
                    player_won = True

        # code for if player wants guess is a whole word and characters are from a-z (.isalpha)              
        elif len(player_guess) == len(word) and player_guess.isalpha():

            if player_guess in used_words:
                print("You already Tried the Country", player_guess)

            elif player_guess != word:
                print(player_guess, "is not the Country.")
                attempts_left -= 1
                if attempts_left <= 7:
                    hangman_pic(attempts_left)
                print("You Have", attempts_left, "attempts remaining!")
                used_words.append(player_guess)

            else:
                # If player manages to work out the country the game should end here.
                player_won = True  
                country_chosen = word

        else:
            #  For invalid Guesses. e.e.g numbers, punctuation etc.
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
    # Code below is for starting a new game
    word = pick_country()
    hang_game(word)

    new_game = input("Start A New Game? (Y-YES/N-NO): \n" )

    if new_game.upper() == "Y" or new_game.upper() == "YES" or new_game.upper() == "":
        print("Startin new game")
        main()

    else:
        print("Thanks For Playing.....")
        exit()


if __name__ == "__main__":
    main()
