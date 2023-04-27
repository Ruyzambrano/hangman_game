from load_words import Load_Words
from game import Game_String
from word_scramble import Word_Scramble

from termcolor import colored


def main():
    while True:
        print(
            colored(
                """
    ____________________________________________\n
""",
                "red",
                attrs=["bold"],
            )
        )
        print("            ", end="")
        print(colored("Welcome to the Game App", "red", attrs=["bold"]))

        print(
            colored(
                """
    ____________________________________________""",
                "red",
                attrs=["bold"],
            )
        )

        print(
            colored(
                """
    Menu:
        """,
                "yellow",
            )
        )
        print(colored("\t\tPlay Hangman         - 'h'", "green"))
        print(colored("\t\tPlay Word Scramble   - 'w'", "cyan"))
        print(colored("\t\tInstructions         - 'i'", "blue"))
        print(colored("\t\tQuit                 - 'q'", "magenta"))
        choice = input(": ").lower()

        if choice == "h":
            hangman_words = Load_Words("words.txt")
            hangman_game = Game_String()
            Game_String.play_game(hangman_game, hangman_words)

        elif choice == "w":
            word_words = Load_Words("words.txt")
            random_word = word_words.get_random_word()
            scramble_game = Word_Scramble(random_word)
            scramble_game.start_game()

        elif choice == "i":
            print("\n\t\t", end="")
            print(colored("Welcome to Hangman!", "blue", attrs=["bold", "underline"]))
            print(
                colored(
                    """
                    HANGMAN

The objective of this game is to guess a hidden word, one letter at a time, 
before the hangman is fully drawn. The word is chosen randomly from a list 
of words.

To make a guess, simply enter a letter using the keyboard. If the letter is
in the word, it will be revealed in the appropriate blank spaces. If the 
letter is not in the word, part of the hangman will be drawn. The game 
continues until you correctly guess the word, or the hangman is fully 
drawn, indicating that you have lost the game.

The game will provide hints about the word's length and any letters 
that you have correctly guessed so far. You will also be given a 
limited number of incorrect guesses before the hangman is fully drawn.

Good luck and have fun playing Hangman!""",
                    "blue",
                )
            )

        elif choice == "q":
            quit()

        else:
            print("Invalid option. Please Try again.")


if __name__ == "__main__":
    main()
