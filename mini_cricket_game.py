import tkinter as tk
import random
from tkinter import messagebox, font

class MiniCricketGame:
    def __init__(self, root):
        """Initialize the Mini Cricket Game with GUI elements"""
        self.root = root
        self.root.title("Mini Cricket Game")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#e6f7ff")  # Light blue background

        # Game variables
        self.total_score = 0
        self.game_active = True

        # Create and configure fonts
        self.title_font = font.Font(family="Arial", size=18, weight="bold")
        self.label_font = font.Font(family="Arial", size=12)
        self.button_font = font.Font(family="Arial", size=12, weight="bold")
        self.score_font = font.Font(family="Arial", size=14, weight="bold")

        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface components"""
        # Title
        self.title_label = tk.Label(
            self.root,
            text="Mini Cricket Game",
            font=self.title_font,
            bg="#e6f7ff",
            fg="#003366"
        )
        self.title_label.pack(pady=10)

        # Instructions
        instructions = "Click a number (1-6) to bat. If your number matches\nthe computer's bowl, you're out!"
        self.instructions_label = tk.Label(
            self.root,
            text=instructions,
            font=self.label_font,
            bg="#e6f7ff"
        )
        self.instructions_label.pack(pady=5)

        # Frame for batting buttons
        self.button_frame = tk.Frame(self.root, bg="#e6f7ff")
        self.button_frame.pack(pady=10)

        # Create batting buttons (1-6)
        self.batting_buttons = []
        for i in range(1, 7):
            btn = tk.Button(
                self.button_frame,
                text=str(i),
                width=4,
                height=2,
                font=self.button_font,
                bg="#4CAF50",  # Green
                fg="white",
                command=lambda num=i: self.play_shot(num)
            )
            btn.grid(row=0, column=i-1, padx=5)
            self.batting_buttons.append(btn)

        # Frame for game information
        self.info_frame = tk.Frame(self.root, bg="#e6f7ff")
        self.info_frame.pack(pady=15)

        # Player's run
        self.player_run_label = tk.Label(
            self.info_frame,
            text="Your Shot: -",
            font=self.label_font,
            bg="#e6f7ff",
            width=15,
            anchor="w"
        )
        self.player_run_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # AI's bowl
        self.ai_bowl_label = tk.Label(
            self.info_frame,
            text="Computer Bowl: -",
            font=self.label_font,
            bg="#e6f7ff",
            width=15,
            anchor="w"
        )
        self.ai_bowl_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Total score
        self.score_label = tk.Label(
            self.info_frame,
            text="Total Score: 0",
            font=self.score_font,
            bg="#e6f7ff",
            fg="#003366",
            width=15,
            anchor="w"
        )
        self.score_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Game status
        self.status_label = tk.Label(
            self.info_frame,
            text="Game Status: Ready to play!",
            font=self.label_font,
            bg="#e6f7ff",
            width=25,
            anchor="w"
        )
        self.status_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Restart button (initially hidden)
        self.restart_button = tk.Button(
            self.root,
            text="Play Again",
            font=self.button_font,
            bg="#FF5722",  # Orange
            fg="white",
            command=self.restart_game,
            state=tk.DISABLED
        )
        self.restart_button.pack(pady=10)

    def play_shot(self, player_number):
        """Handle player's batting shot"""
        if not self.game_active:
            return

        # Generate AI's bowl (1-6)
        ai_number = random.randint(1, 6)

        # Update labels
        self.player_run_label.config(text=f"Your Shot: {player_number}")
        self.ai_bowl_label.config(text=f"Computer Bowl: {ai_number}")

        # Check if player is out
        if player_number == ai_number:
            self.game_active = False
            self.status_label.config(text="Game Status: You're OUT!", fg="red")
            self.show_game_over()
        else:
            # Add runs to total score
            self.total_score += player_number
            self.score_label.config(text=f"Total Score: {self.total_score}")
            self.status_label.config(text=f"Game Status: Good shot! +{player_number} runs", fg="green")

    def show_game_over(self):
        """Display game over message and enable restart button"""
        # Disable batting buttons
        for btn in self.batting_buttons:
            btn.config(state=tk.DISABLED)

        # Enable restart button
        self.restart_button.config(state=tk.NORMAL)

        # Show game over message
        messagebox.showinfo("Game Over", f"You're OUT!\nYour final score: {self.total_score}")

    def restart_game(self):
        """Reset the game to initial state"""
        # Reset game variables
        self.total_score = 0
        self.game_active = True

        # Reset labels
        self.player_run_label.config(text="Your Shot: -")
        self.ai_bowl_label.config(text="Computer Bowl: -")
        self.score_label.config(text="Total Score: 0")
        self.status_label.config(text="Game Status: Ready to play!", fg="black")

        # Enable batting buttons
        for btn in self.batting_buttons:
            btn.config(state=tk.NORMAL)

        # Disable restart button
        self.restart_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = MiniCricketGame(root)
    root.mainloop()