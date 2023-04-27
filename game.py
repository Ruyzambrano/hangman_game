from termcolor import colored
class Game_String:
    def __init__(self):
        self.lives = 0
        self.lose = False
        self.win = False
        self.image = [
            """
        ___________
        |        |
        |        
        |        
        |        
        |        
     ___|___
     
     Lives Left: 6

     """,
            """
        ___________
        |        |
        |        O
        |        
        |        
        |        
     ___|___
     
     Lives Left: 5
     
     """,
            """
        ___________
        |        |
        |        O
        |        |
        |        |
        |        
     ___|___
     
     Lives Left: 4

     """,
            """
        ___________
        |        |
        |        O
        |       /|
        |        |
        |        
     ___|___
     
     Lives Left: 3

     """,
            """
        ___________
        |        |
        |        O
        |       /|\\
        |        |
        |        
     ___|___
    
    Lives Left: 2

     """,
            """
        ___________
        |        |
        |        O
        |       /|\\
        |        |
        |       / 
     ___|___      

     Lives Left: 1

     """,
        ]

    def __str__(self):
        return self.image

    def game_over(self):
        self.image = """
        ___________
        |        |
        |        O
        |       /|\\
        |        |
        |       / \\
     ___|___
     
    ____________________________________________

                   
                   GAME OVER

    ____________________________________________
    
    """
        self.lose = True

    def lose_life(self):
        self.lives += 1
        if self.lives == 6:
            self.game_over()
            print(self.image)

    def game_win(self):
        self.win = True

    def play_game(hangman_game, hangman_words):
        word_display = []
        for i in range(len(hangman_words.random_word)):
            if hangman_words.random_word[i].isalpha():
                word_display.append("____ ")
            else:
                word_display.append(hangman_words.random_word[i])
        guessing_word = list(hangman_words.random_word)
        guessed_letters = []

        while hangman_game.lose == False and hangman_game.win == False:
            print(hangman_game.image[hangman_game.lives])
            for i in word_display:
                print(" " + i + "  ", end="")
            if len(guessed_letters) > 0:
                print("\n\nGuessed letters: ")
                for i in guessed_letters:
                    print(i, end=" ")
            while True:
                letter_choice = input("\n\nGuess a letter: ").strip().lower()

                if letter_choice.isnumeric():
                    print("Your guess must be a letter. Try again.")

                if len(letter_choice) != 1:
                    print("You can only choose one letter. Try again.")
                    continue

                if letter_choice in guessed_letters:
                    print("You have already guessed this letter, try again!")
                    continue

                break

            guessed_letters.extend(letter_choice)
            num_occur = guessing_word.count(letter_choice)
            if num_occur > 0:
                i = 0
                for i in range(len(guessing_word)):
                    if guessing_word[i] == letter_choice:
                        word_display[i] = guessing_word[i]
                        guessing_word[i] = " "

            else:
                hangman_game.lose_life()

            if word_display == list(hangman_words.random_word):
                print(colored("\n\n\t\tY ", "red", attrs=["bold"]), end="")
                print(colored("o ", "light_red", attrs=["bold"]), end="")
                print(colored("u   ", "yellow", attrs=["bold"]), end="")
                print(colored("w ", "green", attrs=["bold"]), end="")
                print(colored("i ", "blue", attrs=["bold"]), end="")
                print(colored("n ", "light_magenta", attrs=["bold"]), end="")
                print(colored("!", "magenta", attrs=["bold"]))
                hangman_game.game_win()

        print(f"\t\tThe word was {hangman_words.random_word}")
