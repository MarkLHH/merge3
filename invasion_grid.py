import console_util

class grid():
    def __init__(self, size = 4):
        self.size = int(size)

        # Get the line capacity
        console_width = console_util.get_condole_width()
        max_grid_width = self.size * 4 + 1
        if max_grid_width > console_width:
            raise Exception("Grid size too big, current console cannot handle!")
        elif self.size < 2:
            raise Exception("Grid size too small, there\'s nothing you can do!")
        
        # create the invasion grid
        self.grid = []
        for i in range(size):
            k = []
            for j in range(size):
                k.append('.')
            self.grid.append(k)
        
        # step placeholder
        self.x_ind = None
        self.y_ind = None
    
    def grid_display(self):
        console_util.clear_screen()
        for x in range(self.size):
            x_line = '|'
            sep_line = ''
            for y in range(self.size):
                x_line += f' {self.grid[x][y]} |'
            for i in range(len(x_line)):
                sep_line += '-'
            print(console_util.center_text(sep_line))
            print(console_util.center_text(x_line))
        print(console_util.center_text(sep_line))
        print()
        temp = input(console_util.center_text("Press enter to continue..."))
    
    def place_resource(self, x, y, resource):
        # Raise index error?
        self.x_ind = x
        self.y_ind = y
        self.grid[x][y] = resource
        self.grid_display()
        
        
    def update_grid(self):
        merge_flag = self.check_merge()
        if merge_flag == True:
            self.resource_merge()
            self.grid_display()
        else: 
        # update the grid for all resource unavailable to merge to uppercase
            for x in range(self.size):
                for y in range(self.size):
                    self.grid[x][y] = self.grid[x][y].upper()
    
    def check_merge(self):
        connected_resources = 0
        # The point to check from self.grid[self.x_ind][self.y_ind]
        #...
        if connected_resources >= 3:
            return True
        return False
        
    
    def resource_merge(self):
        gt_merge = [f'{self.x_ind},{self.y_ind}']
        # Find all connected field(s)
        return None