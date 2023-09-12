from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, postion):
        super().__init__()
        self.score = 0
        self.ascore(postion)

    def ascore(self, position):
        self.ht()
        self.color("white")
        self.penup()
        self.setpos(position)
        self.write(self.score, True, "left", ("Courier", 100, "normal"))

    def point(self, position):
        self.clear()
        self.score += 1
        self.ascore(position)