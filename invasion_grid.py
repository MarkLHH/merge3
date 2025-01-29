import console_util

level_a = 'abcde'
level_1 = '12345'
# phase = 'Initiate', 'Placement', 'Update'
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
        self.round = 0
        self.phase = 'Initiate'
        self.x_ind = None
        self.y_ind = None
        self.connected = []
        self.visited = set()
    
    def grid_display(self):
        console_util.clear_screen()
        print(console_util.center_text(f'Round: {self.round}'))
        print()
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
        print(console_util.center_text(f'Phase: {self.phase}'))
        print(console_util.center_text(f'Phase: Generate > Placement > Update'))
        temp = input(console_util.center_text("Press enter to continue..."))
    
    def place_resource(self, x, y, resource):
        self.round += 1
        # Raise index error?
        self.phase = 'Placement'
        self.x_ind = x
        self.y_ind = y
        self.grid[x][y] = resource
        
        self.grid_display()
        
    def dfs(self,r,c):
        if (r,c) in self.visited or r < 0 or r >= self.size or c < 0 or c >= self.size or self.grid[r][c].lower() != self.grid[self.x_ind][self.y_ind]:
            return None
        self.visited.add((r,c))
        self.connected.append((r,c))
        # Explore all 4 possible directions: up, down, left, right
        self.dfs(r - 1, c) # up
        self.dfs(r + 1, c) # down
        self.dfs(r, c - 1) # left
        self.dfs(r, c + 1) # right
    
    def update_grid(self):
        self.phase = 'Update'
        merge_flag = self.check_merge()
        if merge_flag == True:
            self.resource_merge()
            self.grid_display()
        else: 
        # update the grid for all resource unavailable to merge to uppercase
            for x in range(self.size):
                for y in range(self.size):
                    self.grid[x][y] = self.grid[x][y].upper()
        
        self.grid_display()
    
    def check_merge(self):
        # The point to check from self.grid[self.x_ind][self.y_ind]
        self.dfs(self.x_ind, self.y_ind)
        if len(self.connected) >= 3:
            print(self.connected)
            return True
        else:
            print(self.connected)
            self.connected = []
            self.visited.clear()
            return False  
    
    def resource_merge(self):
        # Find all connected field(s): self.connected
        # Increase level for the initial point
        level = level_a.index(self.grid[self.x_ind][self.y_ind])
        self.grid[self.x_ind][self.y_ind] = level_a[level+1]
        # and update to empty for the rest
        self.connected.remove((self.x_ind,self.y_ind))
        for field in self.connected:
            self.grid[field[0]][field[1]] = '.'
        
        # Reset self.connected
        self.connected = []
        self.visited.clear()
        
    def get_field_resources(self, x, y):
        return self.grid[x][y]
        
    def game_ends(self):
        # calculate score
        # ...
        
        print('Game Ends!')
        