import tkinter as tk
import random
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("The Perfect Guess")
root.geometry("400x300")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
guess_count = 0

# Function to check the user's guess
def check_guess():
    global guess_count
    try:
        guess = int(entry.get())
        guess_count += 1
        if guess > secret_number:
            feedback.set("Lower number please.")
        elif guess < secret_number:
            feedback.set("Higher number please.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed it in {guess_count} tries!")
            reset_game()
    except ValueError:
        feedback.set("Please enter a valid number.")

# Reset the game
def reset_game():
    global secret_number, guess_count
    secret_number = random.randint(1, 100)
    guess_count = 0
    entry.delete(0, tk.END)
    feedback.set("New game started! Enter your guess.")

# GUI Widgets
title = tk.Label(root, text="The Perfect Guess", font=("Helvetica", 18, "bold"))
title.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=10)

submit_btn = tk.Button(root, text="Submit Guess", command=check_guess)
submit_btn.pack(pady=5)

feedback = tk.StringVar()
feedback_label = tk.Label(root, textvariable=feedback, font=("Helvetica", 12))
feedback_label.pack(pady=10)

reset_btn = tk.Button(root, text="Reset Game", command=reset_game)
reset_btn.pack()

feedback.set("Enter your guess between 1 and 100")

# Run the application
root.mainloop()
