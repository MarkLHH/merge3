import properties

class content():
    def __init__(self, kind, pos_x, pos_y, level = 1):
        self.kind = kind
        self.level = level
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def res_get_location(self):
        return (self.pos_x, self.pos_y)  
    
class res(content):
    def __init__(self, kind, pos_x, pos_y, level = 1):
        super().__init__(kind, pos_x, pos_y, level)
        if kind == '1':
            self.score = properties.kind_1_score_meter(level)
        elif kind == '2':
            self.score = properties.kind_2_score_meter(level)
    
    def res_get_score(self):
    	print(self.score)
        
class obs(content):
    def __init__(self, kind, pos_x, pos_y, level = 1):
        super().__init__(kind, pos_x, pos_y, level)
        self.score = 2
        self.resolve = True
        self.block_cap = 4
        
        self.adjacent = [( pos_x - 1, pos_y),
                         ( pos_x + 1, pos_y),
                         ( pos_x, pos_y - 1),
                         ( pos_x, pos_y + 1)]
        
    def update_block_cap(self):
        pass
        
