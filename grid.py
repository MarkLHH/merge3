import console_util
import random

level_a = 'abcde'
level_A = {'A':'1', 'B':'2', 'C':'4', 'D':'6', 'E':'8' }

not_check_list = '.@'
# phase = 'Initiate', 'Placement', 'Update'
class grid():
    def __init__(self, size = 4):
        self.size = int(size)

        '''
        # Get the line capacity
        console_width = console_util.get_condole_width()
        max_grid_width = self.size * 4 + 1
        # Error Handling 
        if max_grid_width > console_width:
            raise Exception("Grid size too big, current console cannot handle!")
        elif self.size < 2:
            raise Exception("Grid size too small, there\'s nothing you can do!")
        '''
        
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
        self.x_ind = 0
        self.y_ind = 0
        self.connected = []
        self.visited = set()
        self.empty_field = []
        
        # fill up empty_field
        for x in range(size):
            for y in range(size):
                self.empty_field.append((x,y))
        self.grid_display()
    
    def grid_display(self):
        console_util.clear_screen()
        print(console_util.center_text(f'Round: {self.round}'))
        print(console_util.center_text(f'Phase: Generate > Placement > Update'))
        #print()
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
        #print()
        print(console_util.center_text(f'Phase: {self.phase}'))
        temp = input(console_util.center_text("Press enter to continue...")) if self.phase != "Placement" else None
    
    def grid_update(self):
        self.phase = 'Update'
        merge_flag = self.check_merge()
        if merge_flag == True:
            self.resource_merge()
            self.grid_display()
            self.grid_update()
        else: 
        # update the grid for all resource unavailable to merge to uppercase
            for x in range(self.size):
                for y in range(self.size):
                    self.grid[x][y] = self.grid[x][y].upper()
        
            self.grid_display()
        
    def find_connected(self,r,c):
        if (
            (r,c) in self.visited or 
            r < 0 or 
            r >= self.size or 
            c < 0 or 
            c >= self.size or 
            self.grid[r][c].lower() != self.grid[self.x_ind][self.y_ind] or 
            self.grid[self.x_ind][self.y_ind] in not_check_list):
            return None
        self.visited.add((r,c))
        self.connected.append((r,c))
        # Explore all 4 possible directions: up, down, left, right
        self.find_connected(r - 1, c) # up
        self.find_connected(r + 1, c) # down
        self.find_connected(r, c - 1) # left
        self.find_connected(r, c + 1) # right
    
    def check_merge(self):
        # The point to check from self.grid[self.x_ind][self.y_ind]
        self.find_connected(self.x_ind, self.y_ind)
        if len(self.connected) >= 3:
            print(self.connected)
            return True
        else:
            print(self.connected)
            self.connected = []
            self.visited.clear()
            return False  
    
    def resource_place(self, x, y, resource):
        self.round += 1
        # Raise index error?
        
        self.x_ind = x
        self.y_ind = y
        self.grid[x][y] = resource
        self.empty_field.remove((x,y))
        
        self.grid_display()
        self.grid_update()
        
    def resource_merge(self):
        # Find all connected field(s): self.connected
        # Increase level for the initial point
        level = level_a.index(self.grid[self.x_ind][self.y_ind])
        self.grid[self.x_ind][self.y_ind] = level_a[level+1]
        # and update to empty for the rest
        self.connected.remove((self.x_ind,self.y_ind))
        for field in self.connected:
            self.grid[field[0]][field[1]] = '.'
            self.empty_field.append((field[0],field[1]))
        
        # Reset self.connected
        self.connected = []
        self.visited.clear()
        
    def resource_generate(self):
        self.phase = "Generate"
        res = random.randint(1,10)
        ftp = random.choice(self.empty_field)
        if res == 1: # generate obs
            self.resource_place(ftp[0],ftp[1],'@')
            self.grid_update()
        elif res > 7:
            rtp = 'a'
            self.resource_place(ftp[0],ftp[1],rtp)
            self.grid_update()
        else:
            pass
        
    def resource_get_field(self, x, y):
        return self.grid[x][y]
    
    def game_round(self):
        while(len(self.empty_field)>0):
            # Phase Generate
            self.resource_generate()
            # Phase Placement
            self.phase = 'Placement'
            self.grid_display()
            res = 'a'
            print(console_util.center_text(f"Where you want to place '{res}'"))
            location = input(console_util.center_text("x and y: "))
            x_ind = int(location[0])
            y_ind = int(location[1])
            
            self.resource_place(x_ind, y_ind, res)
        self.game_ends()
            
    def game_ends(self):
        score = 0
        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y] in level_A:
                    score += int(level_A[f'{self.grid[x][y].upper()}'])
        
        print(console_util.center_text(f'Game Ends! Final score: {score}'))
        