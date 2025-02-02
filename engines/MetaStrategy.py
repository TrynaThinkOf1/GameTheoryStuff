class MetaStrategy:
    def __init__(self):
        self.points = 0
        self.strategies = ['tit_for_tat', 'always_cooperate', 'random']
        self.current_strategy = 'tit_for_tat'
        self.switch_threshold = 3
        self.consecutive_losses = 0
        import random
        self.random = random
        
    def move(self, op_last_move):
        if not op_last_move:
            self.consecutive_losses += 1
        else:
            self.consecutive_losses = 0
            
        if self.consecutive_losses >= self.switch_threshold:
            self.current_strategy = self.random.choice(self.strategies)
            self.consecutive_losses = 0
            
        if self.current_strategy == 'tit_for_tat':
            result = op_last_move
        elif self.current_strategy == 'always_cooperate':
            result = True
        else:
            result = self.random.choice([True, False])
            
        print(f"MetaStrategy: {result}")
        return result
        
    def __repr__(self):
        return "MetaStrategy"
