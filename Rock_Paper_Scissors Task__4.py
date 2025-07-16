import random
import tkinter as tk
from tkinter import messagebox

# Choices available
choices = ["Rock", "Paper", "Scissors"]

# Game logic to determine winner
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

# Function triggered when a choice button is clicked
def make_choice(user_choice):
    computer_choice = random.choice(choices)
    
    result = get_winner(user_choice, computer_choice)

    result_text.set(f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")

# Setup GUI window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x350")
root.config(bg="#E6E6FA")

# Game title
tk.Label(root, text="Rock, Paper, Scissors!", font=("Arial", 20, "bold"), bg="#E6E6FA").pack(pady=10)

# Result text
result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Arial", 14), bg="#E6E6FA", justify="center").pack(pady=20)

# Buttons for choices
button_frame = tk.Frame(root, bg="#E6E6FA")
button_frame.pack()

for choice in choices:
    tk.Button(button_frame, text=choice, width=10, height=2, font=("Arial", 12),
              command=lambda c=choice: make_choice(c)).pack(side="left", padx=10)

# Exit button
tk.Button(root, text="Exit", font=("Arial", 12), bg="red", fg="white", command=root.quit).pack(pady=20)

# Start the GUI loop
root.mainloop()
