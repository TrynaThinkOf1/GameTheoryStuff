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
