class GradualTitForTat:
    def __init__(self):
        self.points = 0
        self.defection_count = 0
        self.punishment_mode = False
        self.punishment_counter = 0
        
    def move(self, op_last_move):
        if not op_last_move:
            self.defection_count += 1
            self.punishment_mode = True
            self.punishment_counter = self.defection_count
        
        if self.punishment_mode:
            if self.punishment_counter > 0:
                self.punishment_counter -= 1
                return False
            else:
                self.punishment_mode = False

        return True
        
    def __repr__(self):
        return "GradualTitForTat"
