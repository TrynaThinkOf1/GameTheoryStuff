class ProbabilisticMimicry:
    def __init__(self):
        self.points = 0
        self.copy_probability = 0.7
        self.default_move = True
        import random
        self.random = random
        
    def move(self, op_last_move):
        if self.random.random() < self.copy_probability:
            result = op_last_move
        else:
            result = self.default_move
            self.default_move = not self.default_move

        return result
        
    def __repr__(self):
        return "ProbabilisticMimicry"
