class XOField:
    def __init__(self):
        self.FIELD = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


    def set_cell(self, row, col, value):
        self.FIELD[row][col] = value
    def get_row(self, n):
        return self.FIELD(n)


    def get_col(self, n):
        return [self.FIELD[i][n] for i in range (3)]

    def get_diag(self, n):
        if n == 0:
            return [self.FIELD[i][i] for i in range (3)]
        if n == 1:
            return [self.FIELD[i][2 - i] for i in range (3)]