from load_words import Load_Words
from game import Game_String

def main():
    print('''
    ____________________________________________
            
            Welcome to the Hangman Game
    
    ____________________________________________
    ''')
    while True:
        print('''
    Menu:
        
        Play Game        - 'g'
        Quit             - 'q'
        ''')
        choice = input(': ').lower()

        if choice == 'g':
            hangman_words = Load_Words('Hangman game\hangman_game\words.txt')
            hangman_game = Game_String()
            print(hangman_game)
            print('____   ' * len(hangman_words.random_word))
            
        elif choice == 'q':
            quit()

        else:
            print('Invalid option. Please Try again.')

if __name__ == '__main__':
      main()