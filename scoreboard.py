from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.high_score = 0
        self.lives = 6
        self.game_on = True
        self.hideturtle()
        self.penup()
        self.goto(0, 260)

    def refresh_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.lives = self.lives - 1
        if self.lives == 0:
            self.stop_game()
        self.update_scoreboard()

    def stop_game(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"High Score: {self.high_score} Game Over.", align=ALIGNMENT, font=FONT)
        self.game_on = False

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} Lives: {self.lives}", align=ALIGNMENT, font=FONT)

    def gain_score(self):
        self.score += 1
        self.update_scoreboard()
