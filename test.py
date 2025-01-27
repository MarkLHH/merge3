import console_util

def test_merge(i_grid):
    if i_grid.grid[1][1].lower() == 'b':
        print(console_util.center_text("Passed!"))
    else:
        print(console_util.center_text("Failed!"))