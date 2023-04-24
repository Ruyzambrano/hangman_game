class Game_String:

    def __init__(self):
        self.image = '''
        ___________
        |        |
        |        
        |        
        |        
        |        
     ___|___
     
     Lives Left: 6

     '''

    def __str__(self):
        return self.image
    
    def wrong_guess1(self):
        self.image = '''
        ___________
        |        |
        |        O
        |        
        |        
        |        
     ___|___
     
     Lives Left: 5
     
     '''

    def wrong_guess2(self):
        self.image = '''
        ___________
        |        |
        |        O
        |        |
        |        |
        |        
     ___|___
     
     Lives Left: 4

     '''
        
    def wrong_guess3(self):
        self.image = '''
        ___________
        |        |
        |        O
        |       /|
        |        |
        |        
     ___|___
     
     Lives Left: 3

     '''
        
    def wrong_guess4(self):
        self.image = '''
        ___________
        |        |
        |        O
        |       /|\\
        |        |
        |        
     ___|___
    
    Lives Left: 2

     '''
        
    def wrong_guess5(self):
        self.image = '''
        ___________
        |        |
        |        O
        |       /|\\
        |        |
        |       / 
     ___|___      

     Lives Left: 1

     '''
        
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
    
