from turtle import Turtle

POSITION = (0, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.penup()
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("white")
        self.goto(POSITION)
        self.update_score(increase=0)

    def update_score(self, increase):
        self.clear()
        self.current_score += increase
        self.write(arg=f"Score: {self.current_score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 35, "bold"))

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.current_score = 0
        self.update_score(increase=0)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", move=False, align="center", font=("Arial", 35, "bold"))
