from turtle import Turtle

class Padle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.goto(position)
        self.shapesize(stretch_len= 4)


    def move_up(self):
        self.forward(20)
    
    def move_down(self):
        self.backward(20)