class XOState:
    def __init__(self):
        self.field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.current_player = 1

    def set_cell(self, row, col, value):
        self.field[row][col] = value

    def get_row(self, n):
        return self.field[n]

    def get_col(self, n):
        return [self.field[i][n] for i in range(3)]

    def get_diag(self, n):
        if n == 0:
            return [self.field[i][i] for i in range(3)]
        if n == 1:
            return [self.field[i][2 - i] for i in range(3)]

    def switch_player(self):
        if self.current_player == 1:
            self.current_player = 2
        elif self.current_player == 2:
            self.current_player = 1