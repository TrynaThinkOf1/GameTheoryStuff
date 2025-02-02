class Random:
    def __init__(self):
        self.points = 0
        
    def move(self, op_last_move):
      from random import random
      move = random()
      if move > 0.5:
        print("Random: True")
        return True
      print("Random: False")
      return False
        
    def __repr__(self):
        return "Random"
