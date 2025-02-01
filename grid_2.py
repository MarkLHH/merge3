import console_util
import content
import properties
import random

class grid():
    def __init__(self, size = 7):
        self.size = int(size)

        # console block
        console_width = console_util.get_condole_width()
        max_grid_width = self.size * 9 + 1
        # Error: grid too big for the console
        if max_grid_width > console_width:
            raise Exception("Grid too big!")
        
        # Create the grid
        self.grid = self.grid = [[None for _ in range(size)] for _ in range(size)]
        
        # Grid information
        self.empty_field = [(x,y) for x in range(size) for y in range(size)] # empty field list for random generate res or obs
                
        # Round information
        self.round = 0
        self.phase = 'Initiate'
        self.display()
        self.x_ind = 0
        self.y_ind = 0
        self.connected = []
        self.visited = set()

    def display(self, not_skip = True):
        console_util.clear_screen()
        print(console_util.center_text(f'Round: {self.round} | Phase: {self.phase}'))
        print(console_util.center_text(f'Phase: Generate > Placement'))
        # Top line
        sep_line = ''
        for i in range(self.size * 10 + 1):
            sep_line += '-'
        # Print each field
        print(console_util.center_text(sep_line))
        for x in range(self.size):
            field_line_1, field_line_2, field_line_3, field_line_4 = '|', '|', '|', '|'
            for y in range(self.size):
                if self.grid[x][y] != None:
                    f_content = self.grid[x][y]
                    field_line_1 += f' . . . . |'
                    field_line_2 += f' {f_content.name} {f_content.kind} L {f_content.level} |'
                    field_line_3 += f' . S {f_content.score} . |'
                    field_line_4 += f' . . . . |'
                else:
                    field_line_1 += f' . . . . |'
                    field_line_2 += f' . . . . |'
                    field_line_3 += f' . . . . |'
                    field_line_4 += f' . . . . |'
            print(console_util.center_text(field_line_1))
            print(console_util.center_text(field_line_2))
            print(console_util.center_text(field_line_3))
            print(console_util.center_text(field_line_4))
            print(console_util.center_text(sep_line))
            
        if  not_skip: 
            input()        
    
    def place(self, x, y, kind = '1', level = 1, not_skip = True):
        self.phase = "Placement"
        # check if x y in bound and check if x y is not occupied
        if (0 <= x < self.size and 0 <= y < self.size):
            if (x,y) in self.empty_field:
                if kind == 'O':
                    self.grid[x][y] = content.obs(x, y, level)
                elif properties.res_kind(kind):
                    self.grid[x][y] = content.res(kind, x, y, level)
                
                self.empty_field.remove((x,y))
                # record the last updated location
                self.x_ind = x
                self.y_ind = y
            else:
                print(console_util.center_text("Field not empty!"))
                input()
        else:
            raise IndexError("Coordinate out of bounds!")
        
        self.display(not_skip)
        
    def update(self):
        self.phase = 'Update'
        # merge res or obs
        updated = self.merge()
        # resolve obs
        updated = self.resolve()        
        # Display the grid
        self.display(updated)
    
    def connect(self, r, c):
        if self.grid[r][c] != None:
            # find connected contents no matter it is obs or res
            v_kind, kind = self.grid[r][c].kind, self.grid[self.x_ind][self.y_ind].kind
            v_level, level = self.grid[r][c].level, self.grid[self.x_ind][self.y_ind].level
            if(
                (r,c) in self.visited or
                v_kind != kind or # not same kind 
                v_level != level # not same level
            ):
                return None
            self.visited.add((r,c))
            self.connected.append((r,c))
            # Explore all direction
            if (r - 1) >= 0: 
                self.connect(r - 1, c) # left
            if (r + 1) < self.size:
                self.connect(r + 1, c) # right
            if (c + 1) < self.size:
                self.connect(r, c + 1) # up
            if (c - 1) >= 0:
                self.connect(r, c - 1) # down
    
    def merge(self):
        updated = False
        # find connected
        if self.grid[self.x_ind][self.y_ind].name == "O" and self.grid[self.x_ind][self.y_ind].level == 3:
            return updated
        
        if self.grid[self.x_ind][self.y_ind] != None:
            self.connect(self.x_ind, self.y_ind)
        if len(self.connected) >= 3:
            self.grid[self.x_ind][self.y_ind].level_up(len(self.connected))
            updated = True
            # update empty_field and the grid when merged
            self.connected.remove((self.x_ind,self.y_ind))
            for field in self.connected:
                self.grid[field[0]][field[1]] = None
                self.empty_field.append((field[0],field[1]))
            self.connected = []
            self.visited.clear()    
            # if merged into O3 then dun need to run merge() again
            self.merge() # there may be chain merge
        # Reset grid information
        self.connected = []
        self.visited.clear()
        return updated
    
    def o_connect(self):
        connected_o = []
        if (self.x_ind - 1) >= 0 and self.grid[self.x_ind-1][self.y_ind] != None:
            if self.grid[self.x_ind-1][self.y_ind].name == "O":
                connected_o.append((self.x_ind-1,self.y_ind))
        if (self.x_ind + 1) < self.size and self.grid[self.x_ind+1][self.y_ind] != None:
            if self.grid[self.x_ind+1][self.y_ind].name == "O":
                connected_o.append((self.x_ind+1,self.y_ind))
        if (self.y_ind - 1) >= 0 and self.grid[self.x_ind][self.y_ind-1] != None:
            if self.grid[self.x_ind][self.y_ind-1].name == "O":
                connected_o.append((self.x_ind,self.y_ind-1))
        if (self.y_ind + 1) < self.size and self.grid[self.x_ind][self.y_ind+1] != None:
            if self.grid[self.x_ind][self.y_ind+1].name == "O":
                connected_o.append((self.x_ind,self.y_ind+1))
        
        return connected_o
    
    def blocked(self):
        for loc in self.connected:
            if loc[0]-1 >= 0:
                if self.grid[loc[0]-1][loc[1]] == None: # nothing blocked in left direction
                    return False
            if loc[0]+1 < self.size:
                if self.grid[loc[0]+1][loc[1]] == None: # nothing blocked in right direction
                    return False
            if loc[1]-1 >= 0:
                if self.grid[loc[0]][loc[1]-1] == None: # nothing blocked in up direction
                    return False
            if loc[1]+1 < self.size:
                if self.grid[loc[0]][loc[1]+1] == None: # nothing blocked in down direction
                    return False 
        return True
    
    def resolve(self):
        updated = False
        if self.grid[self.x_ind][self.y_ind] != None:
            placed_one = self.grid[self.x_ind][self.y_ind].name
            if placed_one == "R": # the placed one is R
                connected_o = self.o_connect() # check all direction yaumo O
                if len(connected_o) > 0: # yau O -> check connected O -> 
                    for o in connected_o: # o is obs loc (x,y) not yet is the potential whole group
                        self.x_ind, self.y_ind = o[0], o[1]
                        self.connect(o[0], o[1]) # try to resolve one group by one group here
                        block = self.blocked() # check blocked
                        if block: # resolve the connected list and reset
                            for field in self.connected:
                                self.grid[field[0]][field[1]] = None
                                self.empty_field.append((field[0],field[1]))
                                updated = True
                        # Reset self.connected and self.visited after finish one O
                        self.connected = []
                        self.visited.clear()
                                
            if placed_one == "O": # the placed one is O
                self.connect(self.x_ind, self.y_ind)
                block = self.blocked()
                if block:
                    for field in self.connected:
                        self.grid[field[0]][field[1]] = None
                        self.empty_field.append((field[0],field[1]))
                        updated = True
                # Reset self.connected and self.visited after finish one O
                self.connected = []
                self.visited.clear() 
                    
        return updated
    
    def generate(self):
        self.round += 1
        self.phase = "Generate"
        gen_1 = random.randint(1,10)
        ftp = random.choice(self.empty_field)
        if gen_1 == 1:
            self.place(ftp[0],ftp[1], 'O')
        elif gen_1 > 7:
            self.place(ftp[0],ftp[1], '1')
        
        self.display(True)
        
    def end(self):
        # points calculate
        total_score = 0
        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y] != None:
                    if self.grid[x][y].name == 'O' and self.grid[x][y].level == 3:
                        total_score -= self.grid[x][y].score
                    elif self.grid[x][y].name == 'R':
                        total_score += self.grid[x][y].score
        print(console_util.center_text(f"Final Score: {total_score}"))
        
        # print game ends
        print()
        print(console_util.center_text("Game Ends!"))
        print()
    
    # Game round should be separated but ..
    def game_round(self):
        while len(self.empty_field) > 0:
            # Generate obs or res
            self.generate()
            self.update()
            ### Place res
            self.phase = "Placement"
            self.display(True)
            # Random the next res kind and level to place
            kind = '1'
            level = 1
            # prompt player to place
            while True:
                ans = input(console_util.center_text('Where you want to place ?: '))
                if len(ans) == 2:
                    if ans[0] in '1234567890' and ans[1] in '1234567890':
                        x_input, y_input = int(ans[0]), int(ans[1])
                        break
                    if ans == '!!':
                        print(console_util.center_text("Game ended by player!"))
                        return None
            # place
            self.place(x_input, y_input, kind, level)
            self.update()
            
            
def test():
    A = grid()
    
    A.place(0,0,'O')
    A.place(0,1,'O')
    A.place(0,2,'O')
    A.update()
    A.place(0,0,'O')
    A.place(1,1,'O')
    A.place(0,1,'O')
    A.update()
    A.place(2,0,'O')
    A.place(1,0,'O')
    A.place(0,0,'O')
    A.update()
    A.place(0,1,'O',3)
    A.place(0,2,'O',3)
    A.update()
    
test()