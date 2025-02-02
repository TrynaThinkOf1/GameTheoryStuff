class MajorityRule:
    def __init__(self):
        self.points = 0
        self.opponent_moves = []
        
    def move(self, op_last_move):
        self.opponent_moves.append(op_last_move)
        if len(self.opponent_moves) < 3:
            return True
        
        true_count = sum(1 for move in self.opponent_moves if move)
        result = true_count > len(self.opponent_moves) / 2
        return result
        
    def __repr__(self):
        return "MajorityRule"
