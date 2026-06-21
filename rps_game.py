import random
import customtkinter as ctk

# =================================================================
# STONE PAPER SCISSORS - COLOR SCHEME
# =================================================================
BG_BLACK    = "#0a0a0a"
DARK_GREY   = "#1a1a1a"
MAROON      = "#800000"
CRIMSON     = "#DC143C"
SOFT_RED    = "#CD5C5C"
DARK_RED    = "#4a0000"
WHITE       = "#FFFFFF"
LIGHT_GREY  = "#CCCCCC"
GREEN       = "#00ff00"

# =================================================================
# GAME SETTINGS
# =================================================================
WINS_NEEDED = 3

# =================================================================
# GAME LOGIC
# =================================================================
def check_win(player, computer):
    if player == computer:
        return "tie", f"Both chose {player}. It's a tie!"

    elif player == "rock":
        if computer == "scissors":
            return "win", "Rock smashes scissors! You win!"
        else:
            return "lose", "Paper covers rock! You lose."

    elif player == "paper":
        if computer == "rock":
            return "win", "Paper covers rock! You win!"
        else:
            return "lose", "Scissors cuts paper! You lose."

    elif player == "scissors":
        if computer == "paper":
            return "win", "Scissors cuts paper! You win!"
        else:
            return "lose", "Rock smashes scissors! You lose."

# =================================================================
# GAME APP
# =================================================================
class RPSGame(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Stone Paper Scissors")
        self.geometry("500x700")
        self.minsize(400, 650)
        self.configure(fg_color=BG_BLACK)
        self.resizable(False, False)

        self.player_score   = 0
        self.computer_score = 0
        self.tie_score      = 0
        self.round_num      = 0
        self.game_over      = False

        self.build_ui()

    def build_ui(self):
        # ── Title ──────────────────────────────────────
        ctk.CTkLabel(
            self,
            text="STONE PAPER\nSCISSORS",
            font=("Arial", 40, "bold"),
            text_color=CRIMSON
        ).pack(pady=(30, 10))

        self.subtitle = ctk.CTkLabel(
            self,
            text="First to 3 wins!",
            font=("Arial", 14),
            text_color=SOFT_RED
        )
        self.subtitle.pack(pady=(0, 20))

        # ── Buttons Frame ─────────────────────────────
        self.btn_frame = ctk.CTkFrame(self, fg_color=BG_BLACK)
        self.btn_frame.pack(pady=10)

        buttons = [
            ("STONE",    "rock"),
            ("PAPER",    "paper"),
            ("SCISSORS", "scissors"),
        ]

        self.game_buttons = []
        for label, choice in buttons:
            btn = ctk.CTkButton(
                self.btn_frame,
                text=label,
                font=("Arial", 16, "bold"),
                fg_color=DARK_RED,
                hover_color=MAROON,
                width=130,
                height=80,
                corner_radius=15,
                command=lambda c=choice: self.play_round(c)
            )
            btn.pack(side="left", padx=10)
            self.game_buttons.append(btn)

        # ── VS Display ────────────────────────────────
        self.vs_frame = ctk.CTkFrame(
            self, fg_color=DARK_GREY, corner_radius=15
        )
        self.vs_frame.pack(pady=20, padx=30, fill="x")

        # Player side
        player_side = ctk.CTkFrame(self.vs_frame, fg_color=DARK_GREY)
        player_side.pack(side="left", expand=True, pady=15)

        ctk.CTkLabel(
            player_side,
            text="YOU",
            font=("Arial", 12),
            text_color=SOFT_RED
        ).pack()

        self.player_label = ctk.CTkLabel(
            player_side,
            text="?",
            font=("Arial", 28, "bold"),
            text_color=WHITE
        )
        self.player_label.pack(pady=5)

        # VS text
        ctk.CTkLabel(
            self.vs_frame,
            text="VS",
            font=("Arial", 24, "bold"),
            text_color=CRIMSON
        ).pack(side="left", expand=True, pady=15)

        # Computer side
        comp_side = ctk.CTkFrame(self.vs_frame, fg_color=DARK_GREY)
        comp_side.pack(side="left", expand=True, pady=15)

        ctk.CTkLabel(
            comp_side,
            text="CPU",
            font=("Arial", 12),
            text_color=SOFT_RED
        ).pack()

        self.computer_label = ctk.CTkLabel(
            comp_side,
            text="?",
            font=("Arial", 28, "bold"),
            text_color=WHITE
        )
        self.computer_label.pack(pady=5)

        # ── Result Label ──────────────────────────────
        self.result_label = ctk.CTkLabel(
            self,
            text="Make your move!",
            font=("Arial", 18, "bold"),
            text_color=LIGHT_GREY
        )
        self.result_label.pack(pady=10)

        # ── Score Board ───────────────────────────────
        score_frame = ctk.CTkFrame(
            self, fg_color=DARK_GREY, corner_radius=15
        )
        score_frame.pack(pady=10, padx=30, fill="x")

        score_inner = ctk.CTkFrame(score_frame, fg_color=DARK_GREY)
        score_inner.pack(pady=15)

        # Player score
        player_col = ctk.CTkFrame(score_inner, fg_color=DARK_GREY)
        player_col.pack(side="left", padx=25)

        self.p_score_label = ctk.CTkLabel(
            player_col,
            text="0",
            font=("Arial", 36, "bold"),
            text_color=CRIMSON
        )
        self.p_score_label.pack()

        ctk.CTkLabel(
            player_col,
            text="YOU",
            font=("Arial", 12),
            text_color=SOFT_RED
        ).pack()

        # Tie score
        tie_col = ctk.CTkFrame(score_inner, fg_color=DARK_GREY)
        tie_col.pack(side="left", padx=25)

        self.t_score_label = ctk.CTkLabel(
            tie_col,
            text="0",
            font=("Arial", 36, "bold"),
            text_color=LIGHT_GREY
        )
        self.t_score_label.pack()

        ctk.CTkLabel(
            tie_col,
            text="TIE",
            font=("Arial", 12),
            text_color="#666666"
        ).pack()

        # Computer score
        comp_col = ctk.CTkFrame(score_inner, fg_color=DARK_GREY)
        comp_col.pack(side="left", padx=25)

        self.c_score_label = ctk.CTkLabel(
            comp_col,
            text="0",
            font=("Arial", 36, "bold"),
            text_color=MAROON
        )
        self.c_score_label.pack()

        ctk.CTkLabel(
            comp_col,
            text="CPU",
            font=("Arial", 12),
            text_color=SOFT_RED
        ).pack()

        # ── Round Counter ─────────────────────────────
        self.round_label = ctk.CTkLabel(
            self,
            text="Round: 0",
            font=("Arial", 13),
            text_color="#666666"
        )
        self.round_label.pack(pady=5)

        # ── Game Over Frame (Hidden initially) ────────
        self.gameover_frame = ctk.CTkFrame(
            self, fg_color=BG_BLACK
        )

        self.gameover_label = ctk.CTkLabel(
            self.gameover_frame,
            text="",
            font=("Arial", 28, "bold"),
            text_color=GREEN
        )
        self.gameover_label.pack(pady=(10, 5))

        self.gameover_subtitle = ctk.CTkLabel(
            self.gameover_frame,
            text="",
            font=("Arial", 14),
            text_color=LIGHT_GREY
        )
        self.gameover_subtitle.pack(pady=(0, 15))

        ctk.CTkButton(
            self.gameover_frame,
            text="PLAY AGAIN",
            fg_color=DARK_RED,
            hover_color=MAROON,
            width=200,
            height=50,
            corner_radius=25,
            font=("Arial", 16, "bold"),
            command=self.reset_game
        ).pack(pady=10)

    # =============================================================
    # GAME PLAY
    # =============================================================
    def play_round(self, player_choice):
        if self.game_over:
            return

        computer_choice = random.choice(
            ["rock", "paper", "scissors"]
        )
        self.round_num += 1

        # Text mapping instead of emojis
        display_map = {
            "rock":     "STONE",
            "paper":    "PAPER",
            "scissors": "SCISSORS"
        }

        # Update display
        self.player_label.configure(
            text=display_map[player_choice]
        )
        self.computer_label.configure(
            text=display_map[computer_choice]
        )

        # Check winner
        result, message = check_win(
            player_choice, computer_choice
        )

        # Update scores
        if result == "win":
            self.player_score += 1
            self.result_label.configure(
                text=message,
                text_color=GREEN
            )
        elif result == "lose":
            self.computer_score += 1
            self.result_label.configure(
                text=message,
                text_color=CRIMSON
            )
        else:
            self.tie_score += 1
            self.result_label.configure(
                text=message,
                text_color=LIGHT_GREY
            )

        # Update score display
        self.p_score_label.configure(
            text=str(self.player_score)
        )
        self.c_score_label.configure(
            text=str(self.computer_score)
        )
        self.t_score_label.configure(
            text=str(self.tie_score)
        )
        self.round_label.configure(
            text=f"Round: {self.round_num}"
        )

        # Check for game over
        if self.player_score >= WINS_NEEDED:
            self.show_game_over(
                "YOU WIN!",
                f"Victory in {self.round_num} rounds!",
                GREEN
            )
        elif self.computer_score >= WINS_NEEDED:
            self.show_game_over(
                "CPU WINS!",
                f"Defeated in {self.round_num} rounds.",
                CRIMSON
            )

    # =============================================================
    # GAME OVER
    # =============================================================
    def show_game_over(self, title, subtitle, color):
        self.game_over = True

        # Disable buttons
        for btn in self.game_buttons:
            btn.configure(state="disabled")

        # Show game over message
        self.gameover_label.configure(
            text=title,
            text_color=color
        )
        self.gameover_subtitle.configure(
            text=subtitle
        )
        self.gameover_frame.pack(pady=10)

        # Update subtitle
        self.subtitle.configure(
            text="Game Over!",
            text_color=color
        )

    # =============================================================
    # RESET GAME
    # =============================================================
    def reset_game(self):
        self.player_score   = 0
        self.computer_score = 0
        self.tie_score      = 0
        self.round_num      = 0
        self.game_over      = False

        # Reset displays
        self.player_label.configure(text="?")
        self.computer_label.configure(text="?")
        self.result_label.configure(
            text="Make your move!",
            text_color=LIGHT_GREY
        )
        self.p_score_label.configure(text="0")
        self.c_score_label.configure(text="0")
        self.t_score_label.configure(text="0")
        self.round_label.configure(text="Round: 0")
        self.subtitle.configure(
            text="First to 3 wins!",
            text_color=SOFT_RED
        )

        # Enable buttons
        for btn in self.game_buttons:
            btn.configure(state="normal")

        # Hide game over frame
        self.gameover_frame.pack_forget()

# =================================================================
# RUN GAME
# =================================================================
if __name__ == "__main__":
    app = RPSGame()
    app.mainloop()