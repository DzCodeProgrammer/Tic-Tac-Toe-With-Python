# Tkinter GUI code with enhanced UI/UX and AI Mode
import tkinter as tk
from tkinter import messagebox
from game.controller import GameController
from config.settings import (
    BOARD_SIZE, WINDOW_TITLE, FONT, TITLE_FONT, STATUS_FONT, INFO_FONT,
    COLOR_X, COLOR_O, COLOR_ACCENT, BG_COLOR, PANEL_BG, BUTTON_BG, 
    BUTTON_HOVER, BUTTON_FG, BORDER_COLOR, TEXT_INFO
)

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(WINDOW_TITLE)
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)
        
        self.controller = None
        self.buttons = []
        self.game_mode = None
        self.ai_difficulty = None
        self.current_frame = None
        
        # Configure window
        self._configure_window()
        self._show_mode_selection()
        
    def _configure_window(self):
        """Setup window styling and position"""
        self.root.update_idletasks()
        width = 550
        height = 700
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def _clear_frame(self):
        """Clear current frame"""
        if self.current_frame:
            self.current_frame.destroy()
        self.buttons = []

    def _show_mode_selection(self):
        """Show mode selection menu"""
        self._clear_frame()
        
        self.current_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title = tk.Label(
            self.current_frame,
            text="TIC TAC TOE",
            font=("Arial", 40, "bold"),
            bg=BG_COLOR,
            fg=COLOR_ACCENT
        )
        title.pack(pady=40)
        
        subtitle = tk.Label(
            self.current_frame,
            text="Pilih Mode Permainan",
            font=("Arial", 20, "bold"),
            bg=BG_COLOR,
            fg=TEXT_INFO
        )
        subtitle.pack(pady=20)
        
        # Buttons container
        btn_container = tk.Frame(self.current_frame, bg=BG_COLOR)
        btn_container.pack(pady=30)
        
        # PvP Button
        pvp_btn = tk.Button(
            btn_container,
            text="👥 Player vs Player",
            font=("Arial", 14, "bold"),
            width=20,
            height=3,
            bg="#FF6B6B",
            fg="#ffffff",
            border=0,
            cursor="hand2",
            command=lambda: self._start_game("pvp"),
            activebackground="#FF8080"
        )
        pvp_btn.pack(pady=10)
        
        # AI Easy
        ai_easy_btn = tk.Button(
            btn_container,
            text="🤖 vs AI (Easy)",
            font=("Arial", 14, "bold"),
            width=20,
            height=3,
            bg="#4ECDC4",
            fg="#ffffff",
            border=0,
            cursor="hand2",
            command=lambda: self._start_game("ai", "easy"),
            activebackground="#6FE0DC"
        )
        ai_easy_btn.pack(pady=10)
        
        # AI Medium
        ai_medium_btn = tk.Button(
            btn_container,
            text="🤖 vs AI (Medium)",
            font=("Arial", 14, "bold"),
            width=20,
            height=3,
            bg="#45B7D1",
            fg="#ffffff",
            border=0,
            cursor="hand2",
            command=lambda: self._start_game("ai", "medium"),
            activebackground="#5CD0E8"
        )
        ai_medium_btn.pack(pady=10)
        
        # AI Hard
        ai_hard_btn = tk.Button(
            btn_container,
            text="🤖 vs AI (Hard)",
            font=("Arial", 14, "bold"),
            width=20,
            height=3,
            bg="#96185B",
            fg="#ffffff",
            border=0,
            cursor="hand2",
            command=lambda: self._start_game("ai", "hard"),
            activebackground="#B8297A"
        )
        ai_hard_btn.pack(pady=10)

    def _start_game(self, mode, difficulty=None):
        """Start game with selected mode"""
        self.game_mode = mode
        self.ai_difficulty = difficulty
        self.controller = GameController(game_mode=mode, ai_difficulty=difficulty or "medium")
        self._create_game_ui()
    def _create_game_ui(self):
        """Create main game UI layout"""
        self._clear_frame()
        
        self.current_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title Panel
        title_frame = tk.Frame(self.current_frame, bg=PANEL_BG, height=70)
        title_frame.pack(fill=tk.X, padx=0, pady=0)
        
        title_label = tk.Label(
            title_frame, 
            text="TIC TAC TOE",
            font=("Arial", 28, "bold"),
            bg=PANEL_BG,
            fg=COLOR_ACCENT
        )
        title_label.pack(pady=12)
        
        mode_text = "PvP" if self.game_mode == "pvp" else f"vs AI ({self.ai_difficulty.upper()})"
        subtitle_label = tk.Label(
            title_frame,
            text=f"Mode: {mode_text}",
            font=("Arial", 12),
            bg=PANEL_BG,
            fg=TEXT_INFO
        )
        subtitle_label.pack(pady=5)
        
        # Status Panel
        status_frame = tk.Frame(self.current_frame, bg=PANEL_BG, height=60)
        status_frame.pack(fill=tk.X, padx=20, pady=(10, 15))
        
        self.status_label = tk.Label(
            status_frame,
            text="",
            font=("Arial", 16, "bold"),
            bg=PANEL_BG,
            fg=COLOR_ACCENT
        )
        self.status_label.pack(pady=12)
        
        self._update_status()
        
        # Board Panel with border
        board_container = tk.Frame(self.current_frame, bg=BG_COLOR)
        board_container.pack(pady=15)
        
        board_frame = tk.Frame(board_container, bg=BORDER_COLOR, padx=3, pady=3)
        board_frame.pack()
        
        inner_frame = tk.Frame(board_frame, bg=BG_COLOR)
        inner_frame.pack(padx=3, pady=3)
        
        self._create_board(inner_frame)
        
        # Info Panel
        info_frame = tk.Frame(self.current_frame, bg=PANEL_BG)
        info_frame.pack(fill=tk.X, padx=20, pady=(10, 15))
        
        info_text = tk.Label(
            info_frame,
            text="🔴 Merah = X  |  🔵 Biru = O  |  Raih 3 Sejajar untuk Menang!",
            font=("Arial", 11),
            bg=PANEL_BG,
            fg=TEXT_INFO
        )
        info_text.pack(pady=8)
        
        # Buttons Panel
        button_frame = tk.Frame(self.current_frame, bg=BG_COLOR)
        button_frame.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        reset_btn = tk.Button(
            button_frame,
            text="🔄 New Game",
            font=("Arial", 11, "bold"),
            bg=COLOR_ACCENT,
            fg="#000000",
            padx=15,
            pady=8,
            border=0,
            cursor="hand2",
            command=self._show_mode_selection,
            activebackground="#FFC868"
        )
        reset_btn.pack(side=tk.LEFT, padx=5)
        
        quit_btn = tk.Button(
            button_frame,
            text="❌ Quit",
            font=("Arial", 11, "bold"),
            bg="#4d4d4d",
            fg=BUTTON_FG,
            padx=15,
            pady=8,
            border=0,
            cursor="hand2",
            command=self.root.quit,
            activebackground="#5d5d5d"
        )
        quit_btn.pack(side=tk.RIGHT, padx=5)

    def _create_board(self, parent):
        """Create game board with enhanced styling"""
        for r in range(BOARD_SIZE):
            row_buttons = []
            for c in range(BOARD_SIZE):
                btn = tk.Button(
                    parent,
                    text="",
                    width=7,
                    height=4,
                    font=("Arial", 18, "bold"),
                    bg=BUTTON_BG,
                    fg=BUTTON_FG,
                    border=1,
                    relief=tk.RAISED,
                    activebackground=BUTTON_HOVER,
                    cursor="hand2",
                    command=lambda r=r, c=c: self.on_click(r, c)
                )
                btn.grid(row=r, column=c, padx=2, pady=2)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def _update_status(self):
        """Update status label"""
        if self.controller.game_over:
            self.status_label.config(text="✅ GAME OVER - PEMENANG DITEMUKAN!", fg=COLOR_ACCENT)
        else:
            if self.game_mode == "ai" and self.controller.current_player == "O":
                self.status_label.config(text="🤖 AI Sedang Berpikir...", fg=COLOR_O)
            else:
                player = self.controller.current_player
                color = COLOR_X if player == "X" else COLOR_O
                self.status_label.config(text=f"Giliran: {player}", fg=color)

    def on_click(self, row, col):
        """Handle button click"""
        # Cegah click jika bukan giliran pemain atau game over
        if self.controller.game_over:
            return
        
        if self.game_mode == "ai" and self.controller.current_player == "O":
            return
        
        result = self.controller.make_move(row, col)

        if result == "DRAW_REMOVE":
            self.refresh_board()
            # Setelah refresh, jika giliran ke AI, jalankan AI move
            if self.game_mode == "ai" and self.controller.current_player == "O":
                self.root.after(800, self._execute_ai_move)
        elif result is None:
            player = self.controller.board.get(row, col)
            color = COLOR_X if player == "X" else COLOR_O
            self.buttons[row][col].config(
                text=player,
                fg=color,
                state=tk.DISABLED
            )
            self._update_status()
            
            # Jika AI mode, jalankan AI move
            if self.game_mode == "ai" and self.controller.current_player == "O":
                self.root.after(800, self._execute_ai_move)
        else:
            player = self.controller.board.get(row, col)
            color = COLOR_X if player == "X" else COLOR_O
            self.buttons[row][col].config(
                text=player,
                fg=color,
                state=tk.DISABLED
            )
            self._update_status()
            self._disable_all_buttons()
            messagebox.showinfo("🎉 PEMENANG!", result)
            self._show_mode_selection()

    def refresh_board(self):
        """Refresh tampilan seluruh board"""
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                cell_value = self.controller.board.get(r, c)
                if cell_value == "":
                    self.buttons[r][c].config(text="", fg=BUTTON_FG, state=tk.NORMAL)
                else:
                    color = COLOR_X if cell_value == "X" else COLOR_O
                    self.buttons[r][c].config(text=cell_value, fg=color, state=tk.DISABLED)

    def _execute_ai_move(self):
        """Execute AI move"""
        result = self.controller.ai_move()
        
        if result == "DRAW_REMOVE":
            self.refresh_board()
            # Setelah refresh, jika masih giliran AI, lanjut bermain
            if self.game_mode == "ai" and self.controller.current_player == "O":
                self.root.after(800, self._execute_ai_move)
        elif result is None:
            row, col = self.controller.move_history[-1][0], self.controller.move_history[-1][1]
            player = self.controller.board.get(row, col)
            color = COLOR_X if player == "X" else COLOR_O
            self.buttons[row][col].config(
                text=player,
                fg=color,
                state=tk.DISABLED
            )
            self._update_status()
        else:
            row, col = self.controller.move_history[-1][0], self.controller.move_history[-1][1]
            player = self.controller.board.get(row, col)
            color = COLOR_X if player == "X" else COLOR_O
            self.buttons[row][col].config(
                text=player,
                fg=color,
                state=tk.DISABLED
            )
            self._update_status()
            self._disable_all_buttons()
            messagebox.showinfo("🎉 PEMENANG!", result)
            self._show_mode_selection()

    def _disable_all_buttons(self):
        """Disable all buttons when game ends"""
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                self.buttons[r][c].config(state=tk.DISABLED)

    def reset_game(self):
        """Reset game to initial state"""
        self.controller = GameController()
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                self.buttons[r][c].config(text="", fg=BUTTON_FG, state=tk.NORMAL)
        self._update_status()
