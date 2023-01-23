import turtle as t

class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.color('Black')
        self.goto(-100,250)
        self.CreateScore()
        

    def CreateScore(self):
        self.clear()
        self.write(f"Score : {self.score}" , align= "right" , font = ("Courier" , 20, "normal"))


    def UpdateScore(self):
        self.score += 1
        self.CreateScore()

    def GameOver(self):
        self.home()
        self.write("GAME OVER" , align= "center" , font = ("Courier" , 20, "bold"))

        