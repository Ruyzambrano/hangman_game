class Game_String:

    def __init__(self):
        self.lives = 0
        self.lose = False
        self.win = False
        self.image = ['''
        ___________
        |        |
        |        
        |        
        |        
        |        
     ___|___
     
     Lives Left: 6

     ''', 
     '''
        ___________
        |        |
        |        O
        |        
        |        
        |        
     ___|___
     
     Lives Left: 5
     
     ''',
    '''
        ___________
        |        |
        |        O
        |        |
        |        |
        |        
     ___|___
     
     Lives Left: 4

     ''',
    '''
        ___________
        |        |
        |        O
        |       /|
        |        |
        |        
     ___|___
     
     Lives Left: 3

     ''',
    '''
        ___________
        |        |
        |        O
        |       /|\\
        |        |
        |        
     ___|___
    
    Lives Left: 2

     ''',
     '''
        ___________
        |        |
        |        O
        |       /|\\
        |        |
        |       / 
     ___|___      

     Lives Left: 1

     ''',]

    def __str__(self):
        return self.image
        
    def game_over(self):
        self.image = '''
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
    
    '''
        self.lose = True
    
    def lose_life(self):
        self.lives += 1
        if self.lives == 6:
            self.game_over()
            print(self.image)

    def game_win(self):
        self.win = True
