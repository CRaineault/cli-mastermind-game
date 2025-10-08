Traditionally, Mastermind is a two-player game in which one player creates a
code using colored pegs, secret to the other player. It is then up to the other
player to guess the correct code in a set number of attempts.

In this game, codes are instead generated randomly, and your task is to find
the correct code within a preset number of turns. It is also customizable
so you can choose whether you want to play with colors or numbers 1-10,
the length of the hidden code, and whether the same color/number can be in
multiple places in the code at once.

Simply follow the prompts on screen to get started.

GAMEPLAY TIPS:


Hits and Blows:

Hits: when you guess the correct color or number in the right position, that is hit.

Blows: when you guess the correct color or number in the wrong position, that is a blow.

What colors might appear in Original Mastermind?

There are only 6 colors that may appear, unless you are playing with more than
6 pegs and no repeats.

Original 6 colors: Blue, Red, Green, Yellow, Pink, White

Extra colors 7-10: Black, Orange, Brown, Purple

Make sure to enter the color name with the first letter capitalized!

Valid numbers for Number Mastermind are 1-10!

Guess counts by peg:

4-6 pegs: 8 guesses
7-8 pegs: 12 guesses
9-10 pegs: 16 guesses

You may read these instructions at any time in the attached README.TXT

(Mastermind colors and rules inspired by Clubhouse Games)

EXTRA CS171 THINGS (not loaded in the program instructions):

Possible improvements:

- More playtesting to balance what is the best amount of guesses per peg
- Different balance for numbers vs. colors
- Scoreboard text file
- Detect if it is the first time being run and do not prompt player to load settings if so
- Check for typos so players won't get a definite miss if they enter something that isn't a valid color/number


What score I think I got:

I believe I earned a 20/20 for these reasons:

- Enough meaningful functions

- All four easily testable functions have test functions

- Program shouldn't crash unless you don't have the README.txt file or if you try to load settings from a file that doesn't exist yet

- Lots of list usage and string conversion

- Prompt for instructions is right there at the beginning

- Checks for bad input during the setup phase, which is the crucial one (this is less important while playing because it justs means you'll get a definite miss)

- Keeps and prints score between games

- File I/O is used to print instructions and keep user settings between games for easy start time