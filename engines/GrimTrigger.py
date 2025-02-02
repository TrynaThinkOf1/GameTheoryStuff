class GrimTrigger:
    def __init__(self):
        self.points = 0
        self.betrayed = False
        
    def move(self, op_last_move):
        if not op_last_move:
            self.betrayed = True
        if self.betrayed:
            return False
        return True
        
    def __repr__(self):
        return "GrimTrigger"
