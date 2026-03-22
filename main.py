import pygame
import sys
from ui.window import GameWindow

def main():
    pygame.init()
    game_window = GameWindow()
    game_window.run()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()