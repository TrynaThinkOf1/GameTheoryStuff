class Sample:
  def __init__(self):
    self.op_last_last_move = False
    self.points = 0
    
  def move(self, op_last_move):
    if op_last_move:
      print("Sample: True")
      return True
    elif not op_last_move and not self.op_last_last_move:
      print("Sample: False")
      return False
      
  def __repr__(self):
    return "Sample"
      
class TitForTat:
  def __init__(self):
    self.points = 0
  
  def move(self, op_last_move):
    if op_last_move:
      print("TitForTat: True")
      return True
    else:
      print("TitForTat: False")
      return False
      
  def __repr__(self):
    return "TitForTat"
      
def main(player1: object, player2: object):
  from random import random, randint
  
  player1 = player1()
  player2 = player2()
  
  first = random()
  if first > 0.5:
    first = player1
    second = player2
  else:
    first = player2
    second = player1
    
  move = first.move(True)
  for _ in range(randint(50, 199)):
    move1 = second.move(move)
    move2 = first.move(move1)
    
    if move1 and move2:
      first.points += 3
      second.points += 3
    elif move1 and not move2:
      first.points += 1
    elif not move1 and move2:
      second.points += 1
      
  print(f"{first}: {first.points}, {second}: {second.points}")
    
if __name__ == "__main__":
  print(main(Sample, TitForTat))
