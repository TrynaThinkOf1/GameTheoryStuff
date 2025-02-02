class TrendFollower:
    def __init__(self):
        self.points = 0
        self.history = []
        self.window_size = 4
        
    def move(self, op_last_move):
        self.history.append(op_last_move)
        if len(self.history) < self.window_size:
            print("TrendFollower: True")
            return True
            
        trend = sum(1 if self.history[i] else -1 
                   for i in range(-self.window_size, 0))
        result = trend >= 0
        print(f"TrendFollower: {result}")
        return result
        
    def __repr__(self):
        return "TrendFollower"
