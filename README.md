# 🎮 Infinite Tic Tac Toe

A modern Python implementation of Tic Tac Toe with intelligent AI opponent and beautiful dark theme UI. Play against a friend or challenge yourself against 3 different AI difficulty levels!

## ✨ Features

### Game Modes
- 👥 **Player vs Player** - Classic two-player gameplay
- 🤖 **vs AI (Easy)** - Perfect for beginners, AI plays randomly
- 🤖 **vs AI (Medium)** - Balanced difficulty with strategic moves
- 🤖 **vs AI (Hard)** - Challenging AI using Minimax algorithm

### Infinite Mode ♾️
- When the 3×3 board fills up without a winner, the **oldest move is automatically removed**
- Game continues indefinitely until someone achieves 3 in a row
- No draws! Someone will always win eventually

### Intelligent AI 🧠
- **Easy Level:** Random move selection (suitable for beginners)
- **Medium Level:** 50% smart moves, 50% random for balanced gameplay
- **Hard Level:** Uses Minimax algorithm with:
  - Priority-based move selection (Win > Block > Setup 2-in-a-row > Center > Corner)
  - Board evaluation heuristics
  - Depth-8 lookahead for optimal decision making
  - Alpha-beta pruning optimization

### Beautiful UI/UX 🎨
- Dark theme with vibrant accent colors
- Intuitive mode selection menu
- Real-time game status display
- Responsive button feedback with hover effects
- Automatic window centering
- Color-coded players:
  - 🔴 **Red** for Player X
  - 🔵 **Blue** for Player O (or AI)

## 🚀 Quick Start

### Prerequisites
- Python 3.6+
- Tkinter (usually included with Python)

### Installation & Running

```bash
# Navigate to project directory
cd Infinite\ TicTacToe

# Run the game
python main.py
```

## 🎮 How to Play

1. **Launch the game** by running `python main.py`
2. **Select your desired game mode** from the beautiful menu:
   - Player vs Player
   - vs AI (Easy)
   - vs AI (Medium)
   - vs AI (Hard)
3. **Click empty cells** to place your mark
4. **Get 3 in a row** (horizontal, vertical, or diagonal) to win
5. **When the board is full**, the oldest move automatically disappears
6. **Game continues** until someone wins - no draws possible!

## 📁 Project Structure

```
Infinite TicTacToe/
├── main.py                 # Entry point - starts the game
├── README.md              # This file
├── LICENSE                # MIT License
├── config/
│   ├── __init__.py
│   └── settings.py        # Game configuration, colors, fonts
├── game/
│   ├── __init__.py
│   ├── board.py           # Board data structure and logic
│   ├── controller.py      # Game state and move validation
│   ├── rules.py           # Win condition checking
│   └── ai.py              # AI player with 3 difficulty levels
└── ui/
    ├── __init__.py
    └── gui.py             # Tkinter GUI implementation
```

## 🎨 Color Scheme

| Element | Color | Hex Code |
|---------|-------|----------|
| Player X | Red | #FF4444 |
| Player O / AI | Blue | #4488FF |
| Accent | Orange | #FFB84D |
| Background | Dark Gray | #1a1a1a |
| Panel | Medium Gray | #252525 |
| Button | Dark Gray | #2d2d2d |

## 🤖 AI Algorithm Details

### Easy Difficulty
- **Strategy:** Complete random selection from available moves
- **Use Case:** Learning the game mechanics
- **Chance to win:** Very low against experienced players

### Medium Difficulty
- **Strategy:** 
  - 50% chance to make a smart move
  - 50% chance to make a random move
- **Smart move priorities:**
  1. Winning move (complete 3 in a row)
  2. Block opponent's winning move
  3. Create 2-in-a-row setup
  4. Block opponent's 2-in-a-row
  5. Take center position
  6. Take corner position
- **Use Case:** Fun and challenging gameplay
- **Chance to win:** Moderate

### Hard Difficulty
- **Strategy:** Minimax algorithm with depth-first search
- **Features:**
  - Lookahead depth: 8 moves
  - Alpha-beta pruning optimization
  - Board position evaluation with heuristics
  - Priority-based move ordering
  - Recognizes winning/losing positions
- **Use Case:** Ultimate challenge
- **Chance to win:** Very low (AI is nearly unbeatable)

## 🎯 Game Rules

1. Players alternate placing marks on a 3×3 grid
2. First player to get 3 marks in a row (any direction) wins
3. When the board fills without a winner, the oldest move is removed
4. Game continues until someone wins
5. X always plays first

## 📊 Win Conditions

A player wins by getting 3 of their marks in a line:
- **Horizontal:** 3 in a row across
- **Vertical:** 3 in a column down
- **Diagonal:** 3 in a diagonal line

## 🛠️ Technologies Used

- **Language:** Python 3.6+
- **GUI Framework:** Tkinter (built-in with Python)
- **Algorithms:** Minimax with alpha-beta pruning
- **Design Pattern:** MVC (Model-View-Controller)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

MIT License © 2026

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 💡 Possible Future Enhancements

- [ ] Larger board sizes (4×4, 5×5)
- [ ] Adjustable win length (4 in a row, 5 in a row, etc.)
- [ ] Game statistics and score tracking
- [ ] Different themes (light mode, custom themes)
- [ ] Undo/Redo functionality
- [ ] Game replay system
- [ ] Network multiplayer support
- [ ] Mobile app version

## 🎓 Educational Value

This project demonstrates:
- Object-oriented programming (OOP) principles
- Game development fundamentals
- AI implementation (Minimax algorithm)
- GUI development with Tkinter
- Algorithm optimization (alpha-beta pruning)
- State management in games
- Event-driven programming

## 📞 Support

If you encounter any issues or have suggestions, feel free to create an issue or pull request!

---

**Made with ❤️ by SISWA**
