import tkinter as tk
from tkinter import messagebox

# Globals
current_player = "X"
winner = False
buttons = []

def check_winner():
    global winner
    winning_combos = [...]
    for (a,b,c) in winning_combos:
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            winner = True
            for i in (a,b,c):
                buttons[i].config(bg="green")
            messagebox.showinfo("Tic‑Tac‑Toe", f"Player {buttons[a]['text']} wins!")
            root.destroy()
            return

def button_click(i):
    global current_player
    if buttons[i]["text"] == "" and not winner:
        buttons[i]["text"] = current_player
        check_winner()
        if not winner:
            current_player = "O" if current_player == "X" else "X"
            label.config(text=f"Player {current_player}'s turn")

# UI Setup
root = tk.Tk()
root.title("Tic‑Tac‑Toe")

for i in range(9):
    btn = tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
