class RandomWithBias:
    def __init__(self):
        self.points = 0
        import random
        self.random = random
        self.cooperation_bias = 0.7
        
    def move(self, op_last_move):
        result = self.random.random() < self.cooperation_bias
        return result
        
    def __repr__(self):
        return "RandomWithBias"
