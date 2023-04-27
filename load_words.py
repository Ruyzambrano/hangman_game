import random

class Load_Words:

    def __init__(self, file):
        self.file = file
        with open(self.file, 'r') as file:
            self.words = file.read().split('\n')
        self.random_word = random.choice(self.words)
    
    def get_random_word(self):
        return self.random_word

    
    

