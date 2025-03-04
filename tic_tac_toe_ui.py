import tkinter as tk
from tkinter import messagebox
import random

def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def on_click(row, col):
    global player_turn, game_mode
    if board[row][col] == "" and not game_over:
        board[row][col] = player_turn
        buttons[row][col].config(text=player_turn)
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_board()
        elif all(board[r][c] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_board()
        else:
            player_turn = "O" if player_turn == "X" else "X"
            if game_mode == "computer" and player_turn == "O":
                computer_move()

def computer_move():
    global player_turn
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        on_click(row, col)

def reset_board():
    global board, player_turn, game_over
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="")
    player_turn = "X"
    game_over = False

def set_game_mode(mode):
    global game_mode
    game_mode = mode
    reset_board()

root = tk.Tk()
root.title("Tic Tac Toe")

game_mode = "user"
player_turn = "X"
game_over = False
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=("Arial", 24), height=2, width=5,
                                      command=lambda r=row, c=col: on_click(r, c))
        buttons[row][col].grid(row=row, column=col)

game_mode_frame = tk.Frame(root)
game_mode_frame.grid(row=3, column=0, columnspan=3)

tk.Button(game_mode_frame, text="User vs User", font=("Arial", 14), command=lambda: set_game_mode("user")).pack(side=tk.LEFT)
tk.Button(game_mode_frame, text="User vs Computer", font=("Arial", 14), command=lambda: set_game_mode("computer")).pack(side=tk.LEFT)

reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_board)
reset_button.grid(row=4, column=0, columnspan=3)

root.mainloop()
