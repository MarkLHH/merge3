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
        # Raise index error
        self.grid[x][y] = resource
        self.grid_display()
        
    def check_merge_ava(self):
        merge = False
        if merge == True:
            self.resource_merge()
            self.grid_display()
        else:
            pass
    
    def resource_merge():
        pass