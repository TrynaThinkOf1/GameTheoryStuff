class Pavlov:
    def __init__(self):
        self.points = 0
        self.last_move = True
        
    def move(self, op_last_move):
        if self.last_move == op_last_move:
            self.last_move = True
            print("Pavlov: True")
            return True
        self.last_move = False
        print("Pavlov: False")
        return False
        
    def __repr__(self):
        return "Pavlov"
