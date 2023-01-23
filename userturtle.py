import turtle as t
DISPLACEMENTBY = 10

class UserTurtle(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0,-290)
        self.setheading(90)

    def Up(self):
        self.goto(self.xcor(), self.ycor() + DISPLACEMENTBY)

    def resetpos(self):
        self.goto(0,-290)

