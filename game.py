import numpy as npy
import random
import time

nb = [[0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0]]


class Game:
    board = None

    def __init__(self, board_size, delay):
        self.num_rows = board_size
        self.num_cols = board_size
        self.delay = delay

    # initial the game board
    def init_board(self, num_live_cells):
        # initial the cells of the board to 0 - dead state
        self.board = npy.zeros(shape=(self.num_rows + 2, self.num_cols + 2), dtype=int)
        random_cols = [random.randint(1, self.num_cols) for i in
                       range(int((self.num_cols * self.num_rows) * num_live_cells))]
        random_rows = [random.randint(1, self.num_rows) for i in
                       range(int((self.num_cols * self.num_rows) * num_live_cells))]
        # change the random cells to 1 - live state
        for i in range(len(random_cols)):
            self.board[random_rows[i]][random_cols[i]] = 1
        print(self.board)

    # count how many living neighboring cells the cell has
    def count_live_cells_for_cell(self, row, col):
        count = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if i == row and j == col:
                    continue
                if self.board[i][j] == 1:
                    count += 1
        return count

    # create new generation
    def create_new_generation(self):
        new_board = self.board
        for i in range(1, self.num_cols + 1):
            for j in range(1, self.num_rows + 1):
                live_cells = self.count_live_cells_for_cell(i, j)
                if self.board[i][j] == 1:
                    if live_cells != 2 and live_cells != 3:
                        new_board[i][j] = 0
                elif self.board[i][j] == 0:
                    if live_cells == 3:
                        new_board[i][j] = 1
                else:
                    pass
        # print(new_board)
        self.board = new_board




# checking the code
# g = Game(5, 0.5)
# g.init_board(0.5)
# print(g.count_live_cells_for_cell(2, 2))
# g.create_new_generation()
# g.game_life()
