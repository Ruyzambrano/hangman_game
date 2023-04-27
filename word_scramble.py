import random

from termcolor import colored


class Word_Scramble:

    def __init__(self, random_word):
        self.lives = 5
        self.lose = False
        self.win = False
        self.random_word = random_word
        self.image = ['\u2665', '\u2665', '\u2665', '\u2665', '\u2665',
                      '\u2665']


    def start_game(self):
        word_chars = list(self.random_word)
        self.random_chars = random.sample(word_chars, len(word_chars))
        self.right_word = []
        print(self.random_word)
        for i in self.random_word:
            self.right_word.append('')
        print(self.right_word)
        while self.lose == False and self.win == False:
            for letter in self.random_chars:
                print(f"  {letter}  ", end=' ')
            guess = input("\nGuess the word: ")
            if len(guess) != len(self.random_word):
                print(f"You must choose a word that is {len(self.random_word)} letters long. Try again.")
                continue
            for count, item in enumerate(guess, 0):
                if guess[count] == word_chars[count]:
                    self.right_word[count] = item
            if self.random_chars == self.right_word:
                self.win_game()
            else:
                self.lose_life()
            
            for item in self.random_chars:
                pass

                            
            print(self.right_word)
                
                

        



    def lose_life(self):
        self.image[self.lives] = '\u2661'
        self.lives -= 1
        if self.lives == 0:
            game_over()

    def win_game(self):
        print(colored('\n\n\t\tY ', 'red', attrs=['bold']), end='')
        print(colored('o ', 'light_red', attrs=['bold']), end='')
        print(colored('u   ', 'yellow', attrs=['bold']), end='')
        print(colored('w ', 'green', attrs=['bold']), end='')
        print(colored('i ', 'blue', attrs=['bold']), end='')
        print(colored('n ', 'light_magenta', attrs=['bold']), end='')
        print(colored('!', 'magenta', attrs=['bold']))
        self.win = True
    
    def game_over():
        '''
    ____________________________________________

                   
                    GAME OVER

    ____________________________________________
            '''
        print(f"\t\tThe word was {self.random_word}")