class TitForTwoTats:
    def __init__(self):
        self.points = 0
        self.opponent_defections = 0
        
    def move(self, op_last_move):
        if not op_last_move:
            self.opponent_defections += 1
        else:
            self.opponent_defections = 0
            
        if self.opponent_defections >= 2:
            print("TitForTwoTats: False")
            return False
            
        print("TitForTwoTats: True")
        return True
        
    def __repr__(self):
        return "TitForTwoTats"
