import console_util
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

    def grid_display_2(self):
        console_util.clear_screen()
        #print(console_util.center_text(f'Round: {self.round} | Phase: {self.phase}'))
        #print(console_util.center_text(f'Phase: Generate > Placement'))
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
                    field_line_1 += f' . . . . |'
                    field_line_2 += f' R 1 L 1 |'
                    field_line_3 += f' . S 1 . |'
                    field_line_4 += f' . . . . |'
                else:
                    field_line_1 += ' . . . . |'
                    field_line_2 += ' . . . . |'
                    field_line_3 += ' . . . . |'
                    field_line_4 += ' . . . . |'
            print(console_util.center_text(field_line_1))
            print(console_util.center_text(field_line_2))
            print(console_util.center_text(field_line_3))
            print(console_util.center_text(field_line_4))
            print(console_util.center_text(sep_line))

console_util.clear_screen()
A = grid()
A.grid_display_2()
