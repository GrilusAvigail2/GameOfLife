import time

from GameOfLife.game import Game
import pygame

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


def display_game(board_size, delay, num_live_cells):
    g = Game(board_size, delay)
    g.init_board(num_live_cells)

    # set up the drawing window
    screen = pygame.display.set_mode([800, 800])
    pygame.display.set_caption('Game Of Life')
    pygame.init()
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Game Of Life', True, WHITE, BLUE)
    textRect = text.get_rect()
    textRect.center = (100,40)
    screen.blit(text, textRect)

    running = True
    while running:
        # close the window when the user click the window close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # going over each cell in the board and draw rectangle if the cell lives = 1
        for i in range(1, g.num_cols + 1):
            for j in range(1, g.num_rows + 1):
                if g.board[i][j] == 1:
                    pygame.draw.rect(screen, WHITE, [60 + 10 * j, 60 + 10 * i, 10, 10])
                    pygame.display.flip()
        # create a new generation
        g.create_new_generation()
        time.sleep(delay)


display_game(40, 0.5, 0.3)
