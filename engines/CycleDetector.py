class CycleDetector:
    def __init__(self):
        self.points = 0
        self.history = []
        self.min_cycle_length = 2
        self.max_cycle_length = 4
        
    def find_cycle(self):
        for length in range(self.min_cycle_length, min(self.max_cycle_length + 1, len(self.history))):
            recent = self.history[-length:]
            previous = self.history[-2*length:-length]
            if recent == previous:
                return length, recent
        return None, None
        
    def move(self, op_last_move):
        self.history.append(op_last_move)
        cycle_length, pattern = self.find_cycle()
        
        if cycle_length:
            next_predicted = pattern[0]
            result = not next_predicted
        else:
            result = True

        return result
        
    def __repr__(self):
        return "CycleDetector"
