class TwoTitsForTat:
    def __init__(self):
        self.points = 0
        self.last_two_moves = [True, True]
        
    def move(self, op_last_move):
        self.last_two_moves.append(op_last_move)
        self.last_two_moves.pop(0)
        
        if not all(self.last_two_moves):
            return False
        return True
        
    def __repr__(self):
        return "TwoTitsForTat"
