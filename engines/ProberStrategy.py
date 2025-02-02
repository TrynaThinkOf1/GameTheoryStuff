class ProberStrategy:
    def __init__(self):
        self.points = 0
        self.move_count = 0
        self.initial_responses = []
        self.exploit_mode = False
        
    def move(self, op_last_move):
        if self.move_count < 3:
            self.initial_responses.append(op_last_move)
            result = [True, False, True][self.move_count]
            self.move_count += 1
            print(f"ProberStrategy: {result}")
            return result
            
        if self.move_count == 3:
            self.exploit_mode = (self.initial_responses[1] and 
                               not self.initial_responses[2])
            self.move_count += 1
            
        if self.exploit_mode:
            print("ProberStrategy: False")
            return False
            
        print(f"ProberStrategy: {op_last_move}")
        return op_last_move
        
    def __repr__(self):
        return "ProberStrategy"
