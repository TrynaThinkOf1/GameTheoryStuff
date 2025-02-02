class PatternHunter:
    def __init__(self):
        self.points = 0
        self.opponent_history = []
        self.pattern_length = 3
        
    def move(self, op_last_move):
        self.opponent_history.append(op_last_move)
        if len(self.opponent_history) < self.pattern_length:
            print("PatternHunter: True")
            return True
            
        recent = self.opponent_history[-self.pattern_length:]
        for i in range(len(self.opponent_history) - self.pattern_length):
            if self.opponent_history[i:i+self.pattern_length] == recent:
                next_move = self.opponent_history[i+self.pattern_length]
                print(f"PatternHunter: {not next_move}")
                return not next_move
        
        print("PatternHunter: True")
        return True
        
    def __repr__(self):
        return "PatternHunter"
