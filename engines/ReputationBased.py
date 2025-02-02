class ReputationBased:
    def __init__(self):
        self.points = 0
        self.reputation_score = 0.5
        self.memory_length = 5
        self.history = []
        
    def move(self, op_last_move):
        self.history.append(op_last_move)
        if len(self.history) > self.memory_length:
            self.history.pop(0)
            
        self.reputation_score = sum(1 for move in self.history if move) / len(self.history)
        result = self.reputation_score >= 0.4
        return result
        
    def __repr__(self):
        return "ReputationBased"
