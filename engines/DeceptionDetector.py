class DeceptionDetector:
    def __init__(self):
        self.points = 0
        self.trust_score = 1.0
        self.history = []
        
    def move(self, op_last_move):
        if self.history:
            if self.history[-1] and not op_last_move:
                self.trust_score *= 0.7
            elif not self.history[-1] and op_last_move:
                self.trust_score = min(1.0, self.trust_score * 1.2)
                
        self.history.append(op_last_move)
        result = self.trust_score > 0.5
        return result
        
    def __repr__(self):
        return "DeceptionDetector"
