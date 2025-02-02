class AdversityLearner:
    def __init__(self):
        self.points = 0
        self.stress_level = 0
        self.recovery_rate = 0.2
        self.max_stress = 3
        
    def move(self, op_last_move):
        if not op_last_move:
            self.stress_level = min(self.max_stress, self.stress_level + 1)
        else:
            self.stress_level = max(0, self.stress_level - self.recovery_rate)
            
        if self.stress_level >= self.max_stress:
            result = False
        elif self.stress_level <= 1:
            result = True
        else:
            result = op_last_move
            
        print(f"AdversityLearner: {result}")
        return result
        
    def __repr__(self):
        return "AdversityLearner"
