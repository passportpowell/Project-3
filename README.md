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
- Category Selection


## Main Page

## Features
- Quiz in random order
- Reset Quiz
- Current Score update
- Score out of 50 points

### Game type
- Multiple choice quiz based on countries.

- Player types their choice and is informed of whether or not they are correct through text.



![Responsive Image](https://github.com/passportpowell/project-2/blob/main/assets/images/right-answer.jpg?raw=true)

![Responsive Image](https://github.com/passportpowell/project-2/blob/main/assets/images/wrong-answer.jpg?raw=true)


- correct letters revealed update in real time after each correct guess.

- option after the game ends allowing player to play again.

![Responsive Image](https://github.com/passportpowell/project-2/blob/main/assets/images/score-popup.jpg?raw=true)



## Technologies Used
Python - used for Coding the game

while, if, def - used

github - Used for hosting repository for easy sharing.

gitpod -  Used for writing the python code.

Heroku - used for deployment

## Running Tests

### Playing the Game
- Tested the game in different browsers
- Gave incorrect answers
- Gave incorrect answers again to see list of used letters
- gave correct letter to see if letters were revealed in the word
- gave correct word outright to see if game ended with congratulations
- Checked text is understood
- check for hangman picture to gradually be shown based on incorrect answers


## Bugs Along The Way

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
# to fix - Want this code for elif G to pick a random word from all the above countries
Code wasn't working after i completed my unctions as i forgot to call the function at the end

Was having major issues with code not running past allowing player to enter their 1st guest. I was trying to subract a "list" from a "list" and upon changing them to "sets" i had forgotten to change my "append" to "add"

Attempts left would not decrement instead just shows -1 Fixed by finding out that i was printing the wrong code.

Game allows me to enter numbers and punction which idon't want. fixed by -

Game wont allow me to show len + text in text fixed by putting text outside of my F string {} as i had it inside seperated by a ','. e.g. i put (f({len(word), Letters} )) instead of (f"{len(word)} Letters)

last letter doesn't show when all answers are correct a solution was to print the word (country) in the congraulations section.

## Deployment
Deployment was achieved via GitHub and gitpod and Heroku pages using the following steps

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

