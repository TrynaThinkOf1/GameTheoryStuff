class FrequencyAnalyzer:
    def __init__(self):
        self.points = 0
        self.window_size = 5
        self.history = []
        import random
        self.random = random
        
    def move(self, op_last_move):
        self.history.append(op_last_move)
        if len(self.history) < self.window_size:
            return True
            
        recent_window = self.history[-self.window_size:]
        true_freq = sum(1 for x in recent_window if x) / self.window_size
        
        if true_freq > 0.7:
            result = True
        elif true_freq < 0.3:
            result = False
        else:
            result = self.random.choice([True, False])

        return result
        
    def __repr__(self):
        return "FrequencyAnalyzer"
