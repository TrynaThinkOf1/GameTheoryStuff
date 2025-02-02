class RiskAdjuster:
    def __init__(self):
        self.points = 0
        self.risk_threshold = 0.5
        self.betrayal_cost = 0.1
        
    def move(self, op_last_move):
        if not op_last_move:
            self.risk_threshold += self.betrayal_cost
        else:
            self.risk_threshold = max(0.5, self.risk_threshold - self.betrayal_cost)
            
        result = self.risk_threshold < 0.7
        return result
        
    def __repr__(self):
        return "RiskAdjuster"
