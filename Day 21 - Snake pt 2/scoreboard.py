from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        with open("hiscore.txt") as file:
            self.hiscore = int(file.read())
        self.set_score()

    def update_score(self):
        self.score += 1
        self.set_score()

    def set_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.hiscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.hiscore:
            self.hiscore = self.score
            with open("hiscore.txt", mode="w") as file:
                file.write(f"{self.hiscore}")
        self.score = 0
        self.set_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)