from turtle import Turtle
FONT = ("Courier", 24, "normal")


# Set up the scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # Increase the level
    def increase_level(self):
        self.clear()
        self.level += 1

        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):

        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)