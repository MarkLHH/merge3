import console_util
import grid
import test

def main():
    try:
        new_game = grid.grid(7)
        new_game.game_round()
    except KeyboardInterrupt:
        print(console_util.center_text(f"Game terminated!"))
    
main()