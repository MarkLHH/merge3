import console_util
import invasion_grid

def main():
    console_util.clear_screen()
    console_util.print_spacer()
    try:
        new_grid = invasion_grid.grid()
        new_grid.grid_display()
    except Exception as e:
        print(e)
    console_util.print_spacer()
main()