class GradualLearner:
    def __init__(self):
        self.points = 0
        self.learning_rate = 0.1
        self.cooperation_probability = 0.5
        
    def move(self, op_last_move):
        if op_last_move:
            self.cooperation_probability += (1 - self.cooperation_probability) * self.learning_rate
        else:
            self.cooperation_probability -= self.cooperation_probability * self.learning_rate
            
        import random
        result = random.random() < self.cooperation_probability
        return result
        
    def __repr__(self):
        return "GradualLearner"
