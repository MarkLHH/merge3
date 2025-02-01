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

    def display(self):
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
        input()
    
    def place(self, x, y, kind, level = 1):
        self.phase = "Placement"
        # check if x y in bound and check if x y is not occupied
        if (0 <= x < self.size and 0 <= y < self.size):
            if (x,y) in self.empty_field:
                if kind == '.':
                    self.grid[x][y] = content.obs(x, y, level)
                elif properties.res_kind(kind):
                    self.grid[x][y] = content.res(kind, x, y, level)
                
                self.empty_field.remove((x,y))
            else:
                print(console_util.center_text("Field not empty!"))
                input()
        else:
            raise IndexError("Coordinate out of bounds!")
        
        self.display()
        
    def update(self):
        # merge res or obs
        
        pass
    
    def connected(self, r, c):
        # find connected contents no matter it is obs or res
        pass
    
    def merge(self):
        
        pass
    
    def generate(self):
        self.round += 1
        self.phase = "Generate"
        
        #self.display()
        
    def end(self):
        # points calculate
        
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
            # place
            self.place(x_input, y_input, kind, level)
            self.update()
        self.end()