from exceptions import AlreadyExistException, ValidationError
import traceback


class TicTacToeBoard:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
            self.board.append(row)

    def insert_move(self, identifier: str, row: int, column: int):
        if 0 >= row or row > len(self.board):
            raise ValidationError(f"Invalid move, Please select correct positions at row : {row}")

        elif 0 >= row or row > len(self.board):
            raise ValidationError(f"Invalid move, Please select correct positions at col : {column}")

        elif self.board[row - 1][column - 1] != "-":
            raise AlreadyExistException("Cell is already occupied, please use another move")

        self.board[row - 1][column - 1] = identifier

        is_winner = self.check_for_win_move(identifier, row, column)

        if is_winner:
            print("Hurrey..!!, you won it")

        self.display_board()

    def display_board(self):
        print("#" * 50)
        for i in self.board:
            print(" ".join(i))

    def check_for_win_move(self, identifier: str, row: int, column: int) -> bool:
        row_positions, column_positions = self.get_win_positions(row, column)
        row_values = [self.board[position[0]][position[1]] for position in row_positions if
                      identifier == self.board[position[0]][position[1]]]
        if len(self.board) == len(row_values):
            return True

        column_values = [self.board[position[0]][position[1]] for position in column_positions if
                         identifier == self.board[position[0]][position[1]]]
        if len(self.board) == len(column_values):
            return True

        diagonal_values = []

        return False

    def get_win_positions(self, row: int, column: int) -> tuple[list, list]:
        row_positions = []
        col_positions = []
        row, column = TicTacToeBoard.format_input_to_list_index(row, column)
        for i, v in enumerate(self.board):
            row_positions.append([row, i])
            col_positions.append([i, column])
        return row_positions, col_positions

    @staticmethod
    def format_input_to_list_index(row, column):
        return row - 1, column - 1


try:
    board = TicTacToeBoard()
    board.create_board()
    board.insert_move("X", 1, 1)
    board.insert_move("X", 2, 1)
    board.insert_move("X", 3, 1)

    board.insert_move("O", 1, 2)
    # board.display_board()
except (Exception, MemoryError) as e:
    print(e)
    traceback.print_exc()
    # board.display_board()
    exit()
