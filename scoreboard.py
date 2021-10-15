from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=-100, y=200)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.l_score} : {self.r_score}", "False", font=("Courier", 80, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", "False", font=("Arial", 20, "normal"))

    def increase_score(self, player):
        if player == "right":
            self.r_score += 1
        elif player == "left":
            self.l_score += 1

        self.clear()
        self.update_scoreboard()
