class AdaptiveStrategy:
    def __init__(self):
        self.points = 0
        self.opponent_cooperation_rate = 0.5
        self.total_moves = 0
        
    def move(self, op_last_move):
        self.total_moves += 1
        if op_last_move:
            self.opponent_cooperation_rate = ((self.opponent_cooperation_rate * 
                (self.total_moves - 1)) + 1) / self.total_moves
        else:
            self.opponent_cooperation_rate = (self.opponent_cooperation_rate * 
                (self.total_moves - 1)) / self.total_moves
        
        result = self.opponent_cooperation_rate >= 0.5
        print(f"AdaptiveStrategy: {result}")
        return result
        
    def __repr__(self):
        return "AdaptiveStrategy"
