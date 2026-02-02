# Board data structure
class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [["" for _ in range(size)] for _ in range(size)]

    def is_empty(self, row, col):
        return self.grid[row][col] == ""

    def place(self, row, col, player):
        self.grid[row][col] = player

    def get(self, row, col):
        return self.grid[row][col]
