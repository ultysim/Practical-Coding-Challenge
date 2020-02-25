

class ConnectFour():
    # TODO make sure col is full before putting a piece
    def __init__(self):
        self.board = [[0] * 6 for _ in range(6)]
        self.player = 1

    def show_board(self):
        for i in self.board:
            temp = []
            for j in i:
                if j == 0:
                    temp.append(' ')
                elif j == 1:
                    temp.append('r')
                else:
                    temp.append('b')
            print(temp)

    def move(self, col):
        row = self.drop_piece(col)
        if self.check_win(row, col):
            return True
        self.player *= -1
        return False

    def drop_piece(self, n):
        # N is column
        # Can check later to yell at user for bad placement
        index = -1
        for i in range(5, -1, -1):
            if self.board[i][n] == 0:
                self.board[i][n] = int(self.player)
                index = i
                break
        return index  # returns row

    def check_win(self, row, col):
        # check row
        row_check = self.find_four(self.board[row])
        # check column
        colm = [i[col] for i in self.board]
        col_check = self.find_four(colm)
        # check tl to br diag
        start_col = int(col)
        start_row = int(row)
        while start_col > 0 and start_row > 0:
            start_col -= 1
            start_row -= 1
        tl = []
        while start_row < 6 and start_col < 6:
            tl.append(self.board[start_row][start_col])
            start_row += 1
            start_col += 1
        tl_check = self.find_four(tl)
        # check tr to bl diag
        start_col = int(col)
        start_row = int(row)
        while start_col < 5 and start_row > 0:
            start_col += 1
            start_row -= 1
        tr = []
        while start_row < 6 and start_col >= 0:
            tr.append(self.board[start_row][start_col])
            start_row += 1
            start_col -= 1
        tr_check = self.find_four(tr)

        return row_check or col_check or tl_check or tr_check

    def find_four(self, data):
        sums = 0
        last = 0
        for i in data:
            if last == i:
                sums += i
            else:
                last = i
                sums = 1
            if abs(sums) == 4:
                return True
        return False

    def full_board(self):
        for i in self.board:
            for j in i:
                if j == 0:
                    return False
        else:
            return True


def play():
    while True:
        game = ConnectFour()
        out = 1
        while True:
            player = game.player
            game.show_board()
            if player == 1:
                col = int(input('Player 1 please input a move, number 0 through 5'))
            else:
                col = int(input('Player 2 please input a move, number 0 through 5'))
            if game.move(col):
                print('*'*30)
                print('*' * 30)
                game.show_board()
                if player == 1:
                    out = int(input('Player 1 wins the game, enter 0 to play again'))
                else:
                    out = int(input('Player 2 wins the game, enter 0 to play again'))
                break
            if game.full_board():
                print('Full Board, start over')
                break

        if out != 0:
            break
if __name__ == '__main__':
    play()