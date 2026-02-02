# AI Player with different difficulty levels
import random
from game.board import Board

class AIPlayer:
    def __init__(self, board, difficulty="medium"):
        self.board = board
        self.difficulty = difficulty  # easy, medium, hard
        self.ai_symbol = "O"
        self.human_symbol = "X"

    def get_best_move(self):
        """Get the best move based on difficulty"""
        if self.difficulty == "easy":
            return self._get_easy_move()
        elif self.difficulty == "medium":
            return self._get_medium_move()
        else:
            return self._get_hard_move()

    def _get_easy_move(self):
        """Easy: Random move"""
        available_moves = self._get_available_moves()
        return random.choice(available_moves) if available_moves else None

    def _get_medium_move(self):
        """Medium: Mix of smart and random moves"""
        available_moves = self._get_available_moves()
        
        # 50% chance untuk smart move, 50% random
        if random.random() < 0.5:
            smart_move = self._find_smart_move()
            if smart_move:
                return smart_move
        
        return random.choice(available_moves) if available_moves else None

    def _get_hard_move(self):
        """Hard: Minimax algorithm"""
        available_moves = self._get_available_moves()
        if not available_moves:
            return None
        
        best_score = float('-inf')
        best_move = available_moves[0]
        
        for row, col in available_moves:
            self.board.grid[row][col] = self.ai_symbol
            score = self._minimax(0, False)
            self.board.grid[row][col] = ""
            
            if score > best_score:
                best_score = score
                best_move = (row, col)
        
        return best_move

    def _minimax(self, depth, is_maximizing, max_depth=9):
        """Minimax with depth-first search and better heuristics"""
        # Check win conditions
        ai_wins = self._check_win_for(self.ai_symbol)
        human_wins = self._check_win_for(self.human_symbol)
        
        if ai_wins:
            return 100 - depth  # Prioritize faster wins
        if human_wins:
            return depth - 100  # Prioritize blocking earlier
        
        available_moves = self._get_available_moves()
        if not available_moves:
            return 0  # Draw
        
        if depth >= max_depth:
            # Heuristic evaluation at max depth
            return self._evaluate_board()
        
        if is_maximizing:
            best_score = float('-inf')
            for row, col in available_moves:
                self.board.grid[row][col] = self.ai_symbol
                score = self._minimax(depth + 1, False, max_depth)
                self.board.grid[row][col] = ""
                best_score = max(score, best_score)
                # Alpha-beta pruning optimization
                if best_score > 50:
                    break
            return best_score
        else:
            best_score = float('inf')
            for row, col in available_moves:
                self.board.grid[row][col] = self.human_symbol
                score = self._minimax(depth + 1, True, max_depth)
                self.board.grid[row][col] = ""
                best_score = min(score, best_score)
                # Alpha-beta pruning optimization
                if best_score < -50:
                    break
            return best_score

    def _find_smart_move(self):
        """Find smart move with priority: win > block > 2-in-a-row > center > corner"""
        available_moves = self._get_available_moves()
        
        # Priority 1: Find winning move (immediately winning)
        for row, col in available_moves:
            self.board.grid[row][col] = self.ai_symbol
            if self._check_win_for(self.ai_symbol):
                self.board.grid[row][col] = ""
                return (row, col)
            self.board.grid[row][col] = ""
        
        # Priority 2: Block opponent's winning move
        for row, col in available_moves:
            self.board.grid[row][col] = self.human_symbol
            if self._check_win_for(self.human_symbol):
                self.board.grid[row][col] = ""
                return (row, col)
            self.board.grid[row][col] = ""
        
        # Priority 3: Make two in a row (set up winning move)
        two_in_row_moves = []
        for row, col in available_moves:
            self.board.grid[row][col] = self.ai_symbol
            # Count how many 2-in-a-row lines this creates
            two_count = self._count_two_in_row()
            if two_count > 0:
                two_in_row_moves.append((row, col, two_count))
            self.board.grid[row][col] = ""
        
        if two_in_row_moves:
            # Return move that creates most 2-in-a-row
            best_move = max(two_in_row_moves, key=lambda x: x[2])
            return (best_move[0], best_move[1])
        
        # Priority 4: Block opponent's 2-in-a-row
        for row, col in available_moves:
            self.board.grid[row][col] = self.human_symbol
            two_count = self._count_two_in_row()
            if two_count > 0:
                self.board.grid[row][col] = ""
                return (row, col)
            self.board.grid[row][col] = ""
        
        # Priority 5: Take center
        center = 1
        if self.board.is_empty(center, center):
            return (center, center)
        
        # Priority 6: Take corner
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        empty_corners = [c for c in corners if self.board.is_empty(c[0], c[1])]
        if empty_corners:
            return random.choice(empty_corners)
        
        return None

    def _count_two_in_row(self):
        """Count how many 2-in-a-row lines exist for current board state"""
        count = 0
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        
        for row in range(3):
            for col in range(3):
                if self.board.get(row, col) == self.ai_symbol:
                    for dr, dc in directions:
                        # Look ahead
                        r, c = row + dr, col + dc
                        if 0 <= r < 3 and 0 <= c < 3 and self.board.get(r, c) == self.ai_symbol:
                            count += 1
        return count

    def _check_win_for(self, symbol):
        """Check if symbol has a winning position"""
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        
        for row in range(3):
            for col in range(3):
                if self.board.get(row, col) == symbol:
                    for dr, dc in directions:
                        count = 1
                        # Check forward
                        r, c = row + dr, col + dc
                        while 0 <= r < 3 and 0 <= c < 3 and self.board.get(r, c) == symbol:
                            count += 1
                            r += dr
                            c += dc
                        # Check backward
                        r, c = row - dr, col - dc
                        while 0 <= r < 3 and 0 <= c < 3 and self.board.get(r, c) == symbol:
                            count += 1
                            r -= dr
                            c -= dc
                        if count >= 3:
                            return True
        return False

    def _get_available_moves(self):
        """Get all available moves"""
        available = []
        for row in range(3):
            for col in range(3):
                if self.board.is_empty(row, col):
                    available.append((row, col))
        return available

    def _evaluate_board(self):
        """Evaluate board position with heuristics"""
        score = 0
        
        # Check all possible 3-in-a-row lines
        lines = [
            # Rows
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # Columns
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            # Diagonals
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]
        
        for line in lines:
            ai_count = sum(1 for r, c in line if self.board.get(r, c) == self.ai_symbol)
            human_count = sum(1 for r, c in line if self.board.get(r, c) == self.human_symbol)
            empty_count = sum(1 for r, c in line if self.board.get(r, c) == "")
            
            # AI scoring
            if human_count == 0 and ai_count > 0:
                if ai_count == 2:
                    score += 20  # Two in a row
                elif ai_count == 1:
                    score += 5   # One in a row
            
            # Human blocking (negative)
            if ai_count == 0 and human_count > 0:
                if human_count == 2:
                    score -= 20  # Opponent has two in a row
                elif human_count == 1:
                    score -= 5   # Opponent has one in a row
        
        # Prefer center
        if self.board.get(1, 1) == self.ai_symbol:
            score += 10
        elif self.board.get(1, 1) == self.human_symbol:
            score -= 10
        
        return score
