class SuspiciousTitForTat:
    def __init__(self):
        self.points = 0
        self.first_move = True
        
    def move(self, op_last_move):
        if self.first_move:
            self.first_move = False
            return False

        return op_last_move
        
    def __repr__(self):
        return "SuspiciousTitForTat"
