# Game controller logic
from game.board import Board
from game.rules import Rules
from game.ai import AIPlayer
from config.settings import BOARD_SIZE, WIN_LENGTH

class GameController:
    def __init__(self, game_mode="pvp", ai_difficulty="medium"):
        self.board = Board(BOARD_SIZE)
        self.rules = Rules(self.board, WIN_LENGTH)
        self.current_player = "X"
        self.game_over = False
        self.move_history = []  # Simpan urutan move
        self.game_mode = game_mode  # "pvp" atau "ai"
        self.ai_difficulty = ai_difficulty
        self.ai_player = AIPlayer(self.board, ai_difficulty) if game_mode == "ai" else None

    def make_move(self, row, col):
        if self.game_over:
            return None

        if not self.board.is_empty(row, col):
            return None

        self.board.place(row, col, self.current_player)
        self.move_history.append((row, col, self.current_player))

        if self.rules.check_win(row, col, self.current_player):
            self.game_over = True
            return f"{self.current_player} MENANG"

        # Cek apakah board penuh (draw)
        if self.is_board_full():
            # Hapus move paling awal
            self.remove_oldest_move()
            # Ganti giliran pemain setelah removal
            self.current_player = "O" if self.current_player == "X" else "X"
            return "DRAW_REMOVE"  # Signal untuk GUI bahwa ada penghapusan

        self.current_player = "O" if self.current_player == "X" else "X"
        return None

    def ai_move(self):
        """Execute AI move"""
        if not self.ai_player or self.current_player != "O" or self.game_over:
            return None
        
        move = self.ai_player.get_best_move()
        if move:
            row, col = move
            return self.make_move(row, col)
        return None

    def is_board_full(self):
        for row in self.board.grid:
            for cell in row:
                if cell == "":
                    return False
        return True

    def remove_oldest_move(self):
        if self.move_history:
            row, col, player = self.move_history.pop(0)
            self.board.grid[row][col] = ""
