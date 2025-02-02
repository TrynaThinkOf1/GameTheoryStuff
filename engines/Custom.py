class Random:
    def __init__(self):
        self.points = 0
        
    def move(self, op_last_move):
      from random import random
      move = random()
      if move > 0.5:
        return True
      return False
        
    def __repr__(self):
        return "Random"

class AlwaysTrue:
    def __init__(self):
        self.points = 0

    def move(self, op_last_move):
        return True

    def __repr__(self):
        return "AlwaysTrue"

class AlwaysFalse:
    def __init__(self):
        self.points = 0

    def move(self, op_last_move):
        return False

    def __repr__(self):
        return "AlwaysFalse"