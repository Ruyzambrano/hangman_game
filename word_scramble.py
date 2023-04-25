from termcolor import colored


class Word_Scramble:

    def __init__(self):
        self.lives = 5
        self.lose = False
        self.win = False
        self.image = ['\u2665', '\u2665', '\u2665', '\u2665', '\u2665',
                       '\u2665']


    def start_game(self, word):
        self.word = word


    def lose_life(self):
        self.image[self.lives] = '\u2661'

    def check_guess(self, word, guess):
        if self.word == guess:
            print(colored('\n\n\t\tY ', 'red', attrs=['bold']), end='')
            print(colored('o ', 'light_red', attrs=['bold']), end='')
            print(colored('u   ', 'yellow', attrs=['bold']), end='')
            print(colored('w ', 'green', attrs=['bold']), end='')
            print(colored('i ', 'blue', attrs=['bold']), end='')
            print(colored('n ', 'light_magenta', attrs=['bold']), end='')
            print(colored('!', 'magenta', attrs=['bold']))
            self.win = True
    