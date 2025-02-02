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
