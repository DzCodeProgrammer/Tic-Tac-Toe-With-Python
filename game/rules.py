# Win rules and logic
class Rules:
    def __init__(self, board, win_length):
        self.board = board
        self.win_length = win_length

    def check_win(self, row, col, player):
        directions = [
            (1, 0),    # vertical
            (0, 1),    # horizontal
            (1, 1),    # diagonal \
            (1, -1)    # diagonal /
        ]

        for dr, dc in directions:
            count = 1
            count += self._count_direction(row, col, dr, dc, player)
            count += self._count_direction(row, col, -dr, -dc, player)

            if count >= self.win_length:
                return True

        return False

    def _count_direction(self, row, col, dr, dc, player):
        r, c = row + dr, col + dc
        count = 0

        while 0 <= r < self.board.size and 0 <= c < self.board.size:
            if self.board.get(r, c) == player:
                count += 1
                r += dr
                c += dc
            else:
                break

        return count
