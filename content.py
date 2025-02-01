import properties

class content():
    def __init__(self, pos_x, pos_y, level, kind):
        self.kind = kind
        self.level = level
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def res_get_location(self):
        return (self.pos_x, self.pos_y)  
    
class res(content):
    def __init__(self, kind, pos_x, pos_y, level):
        super().__init__(pos_x, pos_y, level, kind)
        self.name = 'R'
        self.score = properties.kind_score_meter(level, kind)
            
    def level_up(self, connected):
        self.level += 1
        base_score = properties.kind_score_meter(self.level, self.kind)
        self.score = (base_score + 1) if connected > 3 else base_score
        
    
    def get_score(self):
    	print(self.score)
        
class obs(content):
    def __init__(self, pos_x, pos_y, level, kind = 'O'):
        super().__init__(pos_x, pos_y, level, kind)
        self.name = 'O'
        self.score = 2 # SR
        self.resolve = True
        self.block_cap = 4
        
        # for resolve usage
        self.adjacent = [( pos_x - 1, pos_y),
                         ( pos_x + 1, pos_y),
                         ( pos_x, pos_y - 1),
                         ( pos_x, pos_y + 1)]
        
    def level_up(self, connected):
        self.level += 1
        if self.level == 3:
            self.resolve = False
            self.score = 3
        else: # level 2
            self.score = properties.obs_2_sr_meter(connected)
            
    def update_block_cap(self):
        pass
        
