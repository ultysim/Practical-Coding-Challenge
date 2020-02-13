import numpy as np
import random

def run_game(length, mines):
    game = MineSweeper(length, mines)

    while not game.game_over:
        print(game.print_board())
        a = input('Please give input x and y separated by a space, eg: 0 1')
        x, y = a.split()
        x = int(x)
        y = int(y)
        game.input_move(x, y)
        game.check_win()

    if game.check_win():
        print('Yay, you win')
    else:
        print('BOOOOOOOOOOOM You lose')

class MineSweeper():

    def __init__(self, board_length, num_mines):
        assert num_mines <= board_length ** 2, 'More mines than spots on the board'

        # If a user goes to a place, replace 0 with a space, ' '
        # Store the numbers in the board state

        self.length = board_length
        self.board = np.zeros(shape=(self.length, self.length))
        self.board = np.array(self.board, dtype=object)
        self.mines = num_mines
        # locations we've already been to
        self.checked = {}
        self.revealed_squares = 0

        self.game_over = False

        for _ in range(self.mines):
            while True:
                x = random.randint(0, self.length - 1)
                y = random.randint(0, self.length - 1)
                if self.board[x, y] == 0:
                    self.board[x, y] = -1
                    break

    def print_board(self):
        temp = np.array(self.board, dtype=str)
        temp[temp == '0.0'] = '?'
        temp[temp == '-1'] = '?'
        return temp

    def input_move(self, x, y):
        if self.board[x, y] == -1:
            self.game_over = True
        else:
            self.check_for_bombs(x, y)

    def check(self, x, y):
        if self.board[x, y] == -1:
            return False
        if x in self.checked:
            if y in self.checked[x]:
                return True
            self.checked[x].append(y)
            self.revealed_squares += 1
            return False
        else:
            self.checked[x] = [y]
            self.revealed_squares += 1
            return False

    def check_for_bombs(self, x, y):
        # Check locally for bombs, recursively
        count = 0
        if not self.check(x, y):
            if x - 1 >= 0 and y - 1 >= 0:
                if self.board[x - 1, y - 1] == -1:
                    count += 1
            if x - 1 >= 0:
                if self.board[x - 1, y] == -1:
                    count += 1
            if x - 1 >= 0 and y + 1 < self.length:
                if self.board[x - 1, y + 1] == -1:
                    count += 1
            if y + 1 < self.length:
                if self.board[x, y + 1] == -1:
                    count += 1
            if x + 1 < self.length and y + 1 < self.length:
                if self.board[x + 1, y + 1] == -1:
                    count += 1
            if x + 1 < self.length:
                if self.board[x + 1, y] == -1:
                    count += 1
            if x + 1 < self.length and y - 1 >= 0:
                if self.board[x + 1, y - 1] == -1:
                    count += 1
            if y - 1 >= 0:
                if self.board[x, y - 1] == -1:
                    count += 1
            if count == 0:
                self.board[x, y] = ''
                # No bombs here, look around for more
                self.propogate_search(x, y)
            else:
                self.board[x, y] = count

    def propogate_search(self, x, y):
        # This triggers when we clicked an square with no bomb near by
        # Want to search next spots
        # Don't search diag:
        # if x - 1 >= 0 and y - 1 >= 0:
        #     self.check_for_bombs(x - 1, y - 1)
        if x - 1 >= 0:
            self.check_for_bombs(x - 1, y)
        # if x - 1 >= 0 and y + 1 < self.length:
        #     self.check_for_bombs(x - 1, y + 1)
        if y + 1 < self.length:
            self.check_for_bombs(x, y + 1)
        # if x + 1 < self.length and y + 1 < self.length:
        #     self.check_for_bombs(x + 1, y + 1)
        if x + 1 < self.length:
            self.check_for_bombs(x + 1, y)
        # if x + 1 < self.length and y - 1 >= 0:
        #     self.check_for_bombs(x + 1, y - 1)
        if y - 1 >= 0:
            self.check_for_bombs(x, y - 1)

    def check_win(self):
        out = self.length**2 - self.revealed_squares == self.mines
        if out:
            self.game_over = True
        return True

if __name__ == "__main__":
    a = input("Please input board size and number mines with space, eg 12 3")
    length, mines = a.split()
    length = int(length)
    mines = int(mines)

    while True:
        run_game(length, mines)
        a = input('Type yes to play again')
        if a != 'yes':
            break
