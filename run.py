import random

import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def hangman_rules():
    """
    How to play the game.
    """
    print('Welcome to the rules of Hang-Hangman')
    print('The aim of this game is to guess the hidden name of a country')
    print('Guess 1 letter at a time or guess the entire word')
    print('If you guess the wrong letter you loose a life')


def get_random_word():
    """
    Picks a random word from words.txt 
    """
    random_word = random.choice(open("words.txt", "r").read().split('\n'))
    return get_random_word()

def hangman_lives(lives):
    """
    Displays Hang-Hangman visuals to show lives being used
    """
    lives_left = [
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |\\
        ========
        """,
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        /
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |        /|\\
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |        /|
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |         |
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |
        ========
        """,
        """
        |/
        |
        |
        |
        |
        |
        ========
        """,

        """
        |
        |
        |
        |
        |
        ========
        """,
        """
        """
    ]
    return lives_left[lives]

def choose_game_level():
    """
    Lets the User select the level of Hang-Hangman.
    The user can select to play E for Easy, M for Medium or H for Hard.
    """
    print("Select the level you wish to play at.")
    print("Press E for Easy")
    print("Press M for Medium")
    print("Press H for Hard")
    difficulty = False
    while not difficulty:
        options = input("\n ").upper()
        if options == "E":
            difficulty = True
            num_lives = 10
            return num_lives
        elif options == "M":
            difficulty = True
            num_lives = 7
            return num_lives
        elif options == "H":
            difficulty = True
            num_lives = 5
            return num_lives
        else:
            print("Please select a level E , M or H to make your Choice")


def main():
    """
    Runs the game 
    """
    print("Lets get started")
    
main()
