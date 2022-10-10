# Passport-Powell
Portfolio 3 Assessment

A game based on Hangman targeted to people that like to play a guessing game.


![Responsive Image](https://github.com/passportpowell/project-2/blob/main/assets/images/readme.jpg?raw=true)



## User Stories
- Main page
As a visiting user I would like to see what the game is about and to have access to the quiz.


### Future Features
- Multiplayer
- Save top 10 Scores
- Wider Category Selection


## Main Screen

## Features
- Hangman selection in random order
- Category selection


### Game type
- Hangman style game
- Player types their choice of letters or word and is informed of whether or not they are correct through text.


![Responsive Image](https://github.com/passportpowell/project-2/blob/main/assets/images/right-answer.jpg?raw=true)

![Responsive Image](https://github.com/passportpowell/project-2/blob/main/assets/images/wrong-answer.jpg?raw=true)


- Correct letters revealed in real time after each correct guess.

- Option after the game ends allowing player to play again.

![Responsive Image](https://github.com/passportpowell/project-2/blob/main/assets/images/score-popup.jpg?raw=true)



## Technologies Used
Python - Used for Coding the game

While, if, def - used

Github - Used for hosting repository for easy sharing.

Gitpod - Used for writing the python code.

Heroku - Used for deployment


## Running Tests

### Playing the Game
- Tested the game in different browsers
- Gave incorrect answers
- Gave incorrect answers again to see list of used letters
- gave correct letter to see if letters were revealed in the word
- gave correct word outright to see if game ended with congratulations
- Checked text is understood
- checked for hangman picture to gradually be shown based on incorrect answers
- Checked for game to offer a new game with options Y or N


## Bugs Along The Way

- Decrement for attempts left show up twice, once with just the number and the other with attempts left: Fixed by deleting extra code written.

- last letter doesn't show when all answers are correct: Unsure of how it was fixed but I had started again and it was woking 2nd time around.

- If multiple of the same letter were in the word (e.g. GREECE) ONLY the 1st occurance of the letter was shown instead of all of them (e.g. GRE_C_): searching for a way to fix the issue online by making use of the enumerate() function.

- Game wouldn't end after correctly guessing all letters or word: Fixed by adding a "player_won" with a booleon value that triggered to True upon completion.

- Attempts_left would not decrement by 1 each time: Fixed by realising that I had not spell checked and kept missing the letter "S"

- Have image of a hangman progress each time answer is wrong: Originally tried to put it as a list but couldn't get it to call so created a DEF specifically for it and doing an == operator and if/elif statement against "attempts left". 

- Was having major issues with code not running past allowing player to enter their 1st guest: Fixed by realising I was trying to subract a "list" from a "list" and upon changing them to "sets" i had forgotten to change my "append" to "add". eventually scrapped that idea of sets and made it append a list for used letters and words instead.

- Game allowed me to enter numbers and punction which i didn't want: Fixed by using isalpha method as it returned True if the player input was A-Z. I could then code around this check.


## Deployment
Deployment was achieved via GitHub, Gitpod and Heroku pages using the following steps

## Github
 - In the GitHub repository go to the Settings tab,

 - Using the source section drop-down menu, select the Master/ or Main Branch,

 - Once completed a link will be provided that may take a few minutes to go live,

- Live link https://github.com/passportpowell/project-3

## gitpod
 - In the terminal type python3 -m http.server
 a pop up appears which upon clicking "open in browser will show a new tab with the site created.

## Heroku
- 

## Credits
- Code and explanantion for use of enumerate() function found: 
https://stackoverflow.com/questions/27662404/trying-to-find-the-same-item-in-a-list-with-the-context-of-hangman 
https://stackoverflow.com/questions/63922601/how-to-build-a-list-with-the-duplicated-letters-from-another-string-python-h

- Code for isalpha() method found: 
https://www.w3schools.com/python/ref_string_isalpha.asp

