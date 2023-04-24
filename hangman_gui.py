import random
import tkinter as tk
from load_words import Load_Words
from game import Game_String


class HangmanGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Hangman')
        self.grid()
        self.create_widgets()
        

    def create_widgets(self):
        self.title_label = tk.Label(self, text='Welcome to the Hangman Game', fg='red', font=('bold', 20))
        self.title_label.grid(row=0, column=0, columnspan=3, pady=20)

        self.menu_label = tk.Label(self, text='Menu:', font=('bold', 16))
        self.menu_label.grid(row=1, column=0)

        self.play_button = tk.Button(self, text='Play Game', font=('bold', 14), fg='green', command=self.play_game)
        self.play_button.grid(row=2, column=0, pady=20)

        self.inst_button = tk.Button(self, text='Instructions', font=('bold', 14), fg='blue', command=self.instructions)
        self.inst_button.grid(row=2, column=1, pady=20)

        self.quit_button = tk.Button(self, text='Quit', font=('bold', 14), fg='magenta', command=self.master.destroy)
        self.quit_button.grid(row=2, column=2, pady=20)

    def play_game(self):
        hangman_words = Load_Words('words.txt')
        hangman_game = Game_String()
        self.word_display = []
        for i in range(len(hangman_words.random_word)):
            if hangman_words.random_word[i].isalpha():
                self.word_display.append('____ ')
            else:
                self.word_display.append(hangman_words.random_word[i])
        self.guessing_word = list(hangman_words.random_word)
        self.guessed_letters = []

        self.image_label = tk.Label(self, text=hangman_game.image[hangman_game.lives], font=('Courier', 14))
        self.image_label.grid(row=3, column=0, columnspan=3, pady=20)

        self.word_label = tk.Label(self, text=''.join(self.word_display), font=('Courier', 16))
        self.word_label.grid(row=4, column=0, columnspan=3)

        self.guessed_label = tk.Label(self, text='Guessed letters:', font=('bold', 14))
        self.guessed_label.grid(row=5, column=0, columnspan=3, pady=10)

        self.guessed_letters_label = tk.Label(self, text='', font=('Courier', 14))
        self.guessed_letters_label.grid(row=6, column=0, columnspan=3)

        self.letter_label = tk.Label(self, text='Guess a letter:', font=('bold', 14))
        self.letter_label.grid(row=7, column=0, columnspan=3, pady=20)

        self.letter_entry = tk.Entry(self, font=('Courier', 14))
        self.letter_entry.grid(row=8, column=0, columnspan=3)

        self.letter_entry.bind('<Return>', self.guess_letter)
        self.guess_button = tk.Button(self, text='Guess', font=('bold', 14), command=self.guess_letter)
        self.guess_button.grid(row=8, column=2)


    def instructions(self):
        self.title_label.config(text='Instructions', fg='blue')
        self.menu_label.grid_forget()
        self.play_button.grid_forget()
        self.inst_button.grid_forget()
        self.quit_button.grid_forget()

        self.instructions_text = tk.Text(self, height=10, width=50, font=('Courier', 14))
        self.instructions_text.grid(row=2, column=0, columnspan=3, padx=20, pady=20)
        self.instructions_text.insert('end', 'Instructions:\n\n')
        self.instructions_text.insert('end', '1. The game will randomly select a word from the provided list of words.\n\n')
        self.instructions_text.insert('end', '2. You have to guess letters one at a time to complete the word.\n\n')
        self.instructions_text.insert('end', '3. You have 6 lives. Each time you guess a wrong letter, you lose a life.\n\n')
        self.instructions_text.insert('end', '4. If you guess all the letters in the word before losing all your lives, you win!\n\n')
        self.instructions_text.insert('end', '5. If you lose all your lives before guessing all the letters in the word, you lose.\n\n')
        self.back_button = tk.Button(self, text='Back to Menu', font=('bold', 14), fg='purple', command=self.back_to_menu)
        self.back_button.grid(row=3, column=0, columnspan=3, pady=20)

    def back_to_menu(self):
        self.title_label.config(text='Welcome to the Hangman Game', fg='red')
        self.instructions_text.grid_forget()
        self.back_button.grid_forget()
        self.create_widgets()

    def guess_letter(self, event):
        letter = self.letter_entry.get().lower()
        if letter.isalpha() and len(letter) == 1 and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            if letter in self.guessing_word:
                for i in range(len(self.guessing_word)):
                    if self.guessing_word[i] == letter:
                        self.word_display[i] = letter.upper() + ' '
                self.word_label.config(text=''.join(self.word_display))
                if ''.join(self.word_display).replace(' ', '').lower() == ''.join(self.guessing_word).lower():
                    self.win_game()
            else:
                self.image_label.config(text=hangman_game.image[hangman_game.lives], font=('Courier', 14))
                hangman_game.lives += 1
                self.guessed_letters_label.config(text=' '.join(self.guessed_letters))
                hangman_game.lose_life
                if hangman_game.lives == 7:
                    self.lose_game()
        self.letter_entry.delete(0, 'end')

    def win_game(self):
        self.title_label.config(text='You Won!', fg='green')
        self.word_label.config(text=''.join(self.word_display))
        self.letter_entry.grid_forget()
        self.letter_label.config(text='')
        self.guessed_label.grid_forget()
        self.guessed_letters_label.grid_forget()
        self.guess_button.grid_forget()

    def lose_game(self):
        self.title_label.config(text='You Lost!', fg='red')
        self.word_label.config(text=''.join(self.guessing_word).upper())
        self.letter_entry.grid_forget()
        self.letter_label.config(text='')
        self.guessed_label.grid_forget()
        self.guessed_letters_label.grid_forget()
        self.guess_button.grid_forget()


hangman_game = Game_String()
root = tk.Tk()
app = HangmanGUI(master=root)
app.mainloop()