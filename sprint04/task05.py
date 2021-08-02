class Gallows():
    
    def __init__(self):
        self.words = []
        self.game_over = False
    
    def play(self, word):
        if self.game_over:
            return 'game over'
        if not self.words:
            self.words.append(word)
            return self.words
        if (
            word.startswith(self.words[-1][-1])
            and word not in self.words    
        ):
            self.words.append(word)
            return self.words
        self.game_over = True
        return 'game over'
    
    def restart(self):
        self.words = []
        self.game_over = False
        return 'game restarted'
