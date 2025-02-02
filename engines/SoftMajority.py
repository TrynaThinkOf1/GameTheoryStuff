class SoftMajority:
    def __init__(self):
        self.points = 0
        self.opponent_moves = []
        
    def move(self, op_last_move):
        self.opponent_moves.append(op_last_move)
        if len(self.opponent_moves) < 3:
            print("SoftMajority: True")
            return True
            
        true_count = sum(1 for move in self.opponent_moves[-3:] if move)
        result = true_count >= 1
        print(f"SoftMajority: {result}")
        return result
        
    def __repr__(self):
        return "SoftMajority"
