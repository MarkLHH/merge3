import console_util
import grid
import grid_2
import test

def main():
    try:
        new_game = grid_2.grid()
        new_game.game_round()
        new_game.end()
    except KeyboardInterrupt:
        print(console_util.center_text(f"Game terminated!"))
    
main()