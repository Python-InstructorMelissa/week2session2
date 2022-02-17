class Trick:
    def __init__(self, trickName, difficulty):
        self.trickName = trickName
        self.difficulty = difficulty

    def leveledUpTrick(self, level):
        original = self.difficulty
        self.difficulty += level
        print(f'Trick leveled up from {original} to {self.difficulty}')
        return self

    