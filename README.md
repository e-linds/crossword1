**ReadMe: CrossWord**

This project is a quick-to-play yet multi-faceted word game, built with Python and SQLAlchemy and run completely on a CLI. It began with the goal of building a traditional crossword puzzle to run in the CLI, but has morphed into a combination of Sudoku, Scrabble and a crossword.

The steps to play the game should be fairly clear when running the program. It functions very similar to a regular crossword: you'll be provided clues, and you'll need to guess the word which fits into the grid based on other letters around it. 
You'll also have the option to create your own 5x5 puzzle, which is a challenge in and of itself (this is where sudoku comes into play). 

To run the program:
1. Fork and clone the repo and run on your own machine.
2. Run pipenv install and pipenv shell to enter the virtual environment.
3. Run pip install sqlalchemy to install SQLAlchemy, the main dependency of this project.
4. Run python lib/app.py to begin the program. As you'll see in the menu, you can choose to create a new 5x5 puzzle, solve an existing 5x5 puzzle, or edit/delete an existing 5x5 puzzle.
5. Coming soon, you'll also be able to create and solve traditional crossword puzzles!

**Dependencies:**
SQLAlchemy
