from load_words import Load_Words
from game import Game_String
from termcolor import colored

def main():
    while True:
        print(colored('''
    ____________________________________________\n
''', 'red', attrs=['bold']))
        print('            ', end='') 
        print(colored('Welcome to the Hangman Game', 'red', attrs=['bold']))
    
        print(colored('''
    ____________________________________________''', 'red', attrs=['bold'])) 

        print(colored('''
    Menu:
        ''', 'yellow'))
        print(colored('\t\tPlay Game        - \'g\'', 'green'))
        print(colored('\t\tInstructions     - \'i\'', 'blue'))
        print(colored('\t\tQuit             - \'q\'', 'magenta'))
        choice = input(': ').lower()

        if choice == 'g':
            hangman_words = Load_Words('words.txt')
            hangman_game = Game_String()
            word_display = []
            for i in range(len(hangman_words.random_word)):
                if hangman_words.random_word[i].isalpha():
                    word_display.append('____ ')
                else:
                    word_display.append(hangman_words.random_word[i])
            guessing_word = list(hangman_words.random_word)
            guessed_letters = []

            while hangman_game.lose == False and hangman_game.win == False:
                print(hangman_game.image[hangman_game.lives])
                for i in word_display:
                    print(' ' + i + '  ', end='')
                if len(guessed_letters) > 0:
                    print('\n\nGuessed letters: ')
                    for i in guessed_letters:
                        print(i, end=' ')
                while True:
                    letter_choice = input('\n\nGuess a letter: ').strip().lower()

                    if letter_choice.isnumeric():
                        print('Your guess must be a letter. Try again.')
                
                    if len(letter_choice) != 1:
                        print('You can only choose one letter. Try again.')
                        continue
                    
                    if letter_choice in guessed_letters:
                        print('You have already guessed this letter, try again!')
                        continue

                    break

                guessed_letters.extend(letter_choice)
                num_occur = guessing_word.count(letter_choice)
                if num_occur > 0:
                    i = 0
                    for i in range(len(guessing_word)):
                        if guessing_word[i] == letter_choice:
                            word_display[i] = guessing_word[i] 
                            guessing_word[i] = ' '
                            
                else:
                    hangman_game.lose_life()

                if word_display == list(hangman_words.random_word):
                    print(colored('\n\n\t\tY ', 'red', attrs=['bold']), end='')
                    print(colored('o ', 'light_red', attrs=['bold']), end='')
                    print(colored('u   ', 'yellow', attrs=['bold']), end='')
                    print(colored('w ', 'green', attrs=['bold']), end='')
                    print(colored('i ', 'blue', attrs=['bold']), end='')
                    print(colored('n ', 'light_magenta', attrs=['bold']), end='')
                    print(colored('!', 'magenta', attrs=['bold']))
                    hangman_game.game_win()
            
            print(f'\t\tThe word was {hangman_words.random_word}')
        elif choice == 'w':
            
        elif choice == 'i':
            print('\n\t\t', end='')
            print(colored('Welcome to Hangman!', 'blue', attrs=['bold', 'underline']))
            print(colored('''
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

Good luck and have fun playing Hangman!''', 'blue'))
            
        elif choice == 'q':
            quit()

        else:
            print('Invalid option. Please Try again.')

if __name__ == '__main__':
    main()