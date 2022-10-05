Attempts left would not decrement instead just shows -1
Fixed by finding out that i was printing the wrong code.

Game allows me to enter numbers and punction which idon't want.
fixed by -

Game wont allow me to show len + text in text
fixed by putting text outside of my F string {} as i had it inside seperated by a ','. e.g. i put (f({len(word), Letters} )) instead of (f"{len(word)} Letters)

last letter doesn't show when all answers are correct
a solution was to print the word (country) in the congraulations section.