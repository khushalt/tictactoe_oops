from exceptions import AlreadyExistException, ValidationError
import traceback


class TicTacToeBoard:

    def __init__(self):
        self.board = []
        self.board_size = 3
        self.last_move = None

    def create_board(self):
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                row.append("-")
            self.board.append(row)

    def validate(self):
        pass

    def insert_move(self, identifier: str, row: int, column: int):
        if 0 >= row or row > len(self.board):
            raise ValidationError(f"Invalid move, Please select correct positions at row : {row}")

        elif 0 >= row or row > len(self.board):
            raise ValidationError(f"Invalid move, Please select correct positions at col : {column}")

        elif self.board[row - 1][column - 1] != "-":
            raise AlreadyExistException("Cell is already occupied, please use another move")

        if self.last_move and self.last_move == identifier:
            raise ValidationError(f"Not allowed for {identifier}, wait for your move")

        self.board[row - 1][column - 1] = identifier
        self.get_last_move(identifier)

        is_winner = self.check_for_win_move(identifier, row, column)

        if is_winner:
            print("Congrats..!!, you won it")

        self.display_board()

    def display_board(self):
        print("#" * 50)
        for i in self.board:
            print(" ".join(i))

    def check_for_win_move(self, identifier: str, row: int, column: int) -> bool:
        row_positions, column_positions, diagonal_positions = self.get_win_positions(row, column)
        row_values = [self.board[position[0]][position[1]] for position in row_positions if
                      identifier == self.board[position[0]][position[1]]]
        if len(self.board) == len(row_values):
            return True

        column_values = [self.board[position[0]][position[1]] for position in column_positions if
                         identifier == self.board[position[0]][position[1]]]
        if len(self.board) == len(column_values):
            return True

        diagonal_values = [self.board[position[0]][position[1]] for position in diagonal_positions if
                           identifier == self.board[position[0]][position[1]]]
        if len(self.board) == len(diagonal_values):
            return True

        return False

    def get_win_positions(self, row: int, column: int) -> tuple[list, list, list]:
        row_positions = []
        col_positions = []
        diagonal_positions, diagonal_max_reach = [], len(self.board) - 1
        row, column = TicTacToeBoard.format_input_to_list_index(row, column)
        for i, v in enumerate(self.board):
            row_positions.append([row, i])
            col_positions.append([i, column])
            diagonal_positions.append([i, i])
        return row_positions, col_positions, diagonal_positions

    @staticmethod
    def format_input_to_list_index(row, column):
        return row - 1, column - 1

    def get_last_move(self, last_move):
        self.last_move = last_move
        return self.last_move


try:
    board = TicTacToeBoard()
    board.create_board()
    # board.get_win_positions(2, 2)
    board.insert_move("o", 1, 1)
    board.insert_move("X", 3, 3)
    board.insert_move("o", 2, 2)

except (Exception, MemoryError) as e:
    print(e)
    traceback.print_exc()
    # board.display_board()
    exit()
