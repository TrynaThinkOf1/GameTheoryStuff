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
