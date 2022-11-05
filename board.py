from exceptions import AlreadyExistException, ValidationError


class TicTacToeBoard:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
            self.board.append(row)
        self.display_board()

    def insert_move(self, identifier, row, column):
        for i, v in enumerate(self.board):
            if len(self.board) < row or len(self.board) < column:
                raise ValidationError("Invalid move")

            if self.board[row-1][column-1] != "-":
                raise AlreadyExistException("Cell is already occupied, please use another move")

            if i == (row - 1) and self.board[row - 1][column - 1] == "-":
                self.board[row - 1][column - 1] = identifier
        self.display_board()

    def display_board(self):
        for i in self.board:
            print(" ".join(i))

    def check_for_win_move(self):
        pass


try:
    board = TicTacToeBoard()
    board.create_board()
    board.insert_move("X", 1, 2)
    board.insert_move("X", 1, 2)
    board.display_board()
except (Exception, MemoryError) as e:
    print(e)
    board.display_board()
    exit()
