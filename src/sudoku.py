class Sudoku:
    def __init__(self, input_board=None):
        self.board = []
        self.input_board = input_board

        if self.input_board is not None:
            self.decode()
        else:
            self.board = [[0 for _ in range(9)] for _ in range(9)]

    def __str__(self):
        encoded_board = ''
        for y in range(9):
            line = ''
            if y == 3 or y == 6:
                encoded_board += '\n'

            for x in range(9):
                if x == 3 or x == 6:
                    line += ' '

                line += str(self.board[y][x])
            line += '\n'

            encoded_board += line
        return encoded_board

    def decode(self):
        """ Decode the board data from a correctly formatted text file. """

        # Read content from file at specified path
        for line in self.input_board.splitlines():
            if len(line) != 0:  # Ignore empty lines which separates 3x3 squares
                board_line = []
                for char in line:
                    if char != ' ':  # Ignore whitespaces which separates 3x3 squares
                        board_line.append(int(char))
                self.board.append(board_line)

    def solve(self):
        next = self.find_next_empty()
        if not next:
            return True
        else:
            y, x = next

        for n in range(1, 10):
            if self.is_valid(n, (y, x)):
                self.board[y][x] = n

                if self.solve():
                    return True

                self.board[y][x] = 0
        return False

    def is_valid(self, guess, position):
        y, x = position

        # Check column
        for i in range(9):
            if self.board[i][x] == guess and y != i:
                return False
        # Check row
        for j in range(9):
            if self.board[y][j] == guess and x != j:
                return False

        # Check square
        box_x = x // 3
        box_y = y // 3
        for j in range(box_y * 3, box_y * 3 + 3):
            for i in range(box_x * 3, box_x * 3 + 3):
                if self.board[j][i] == guess and (j, i) != position:
                    return False

        print(self.board)
        return True

    def find_next_empty(self):
        for y in range(9):
            for x in range(9):
                if self.board[y][x] == 0:
                    return y, x
        return None

    @staticmethod
    def create_template():
        template = Sudoku()
        return str(template)
