class ForgivingTitForTat:
    def __init__(self):
        self.points = 0
        self.forgiveness_counter = 0
        
    def move(self, op_last_move):
        if not op_last_move:
            self.forgiveness_counter += 1
            if self.forgiveness_counter < 3:
                return True
        else:
            self.forgiveness_counter = 0
        result = op_last_move
        return result
        
    def __repr__(self):
        return "ForgivingTitForTat"
