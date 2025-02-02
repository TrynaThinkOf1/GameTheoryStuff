class MomentumBased:
    def __init__(self):
        self.points = 0
        self.streak_count = 0
        self.current_streak = True
        
    def move(self, op_last_move):
        if op_last_move == self.current_streak:
            self.streak_count += 1
        else:
            self.streak_count = 1
            self.current_streak = op_last_move
            
        if self.streak_count >= 3:
            result = self.current_streak
        else:
            result = not self.current_streak

        return result
        
    def __repr__(self):
        return "MomentumBased"
