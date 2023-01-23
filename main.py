import turtle as t 
from cars import Cars
import time
from userturtle import UserTurtle
from scoreboards import ScoreBoard


game_on = True



screen= t.Screen()
screen.setup(600,600)
screen.bgcolor("white")
screen.title("Why did the Turtle cross the road?")
screen.tracer(0)
t.colormode(255)


usert = UserTurtle()
scoreboard = ScoreBoard()
car = Cars()


screen.listen()
screen.onkeypress(usert.Up, "Up")



while game_on:
    time.sleep(0.1)
    screen.update()
    car.CreateCar()
    car.MoveCar()


    for _ in car.carlist:
        if _.distance(usert) < 20 and usert.ycor() < _.ycor() +15 and usert.ycor() > _.ycor() -15 :
            game_on = False
            scoreboard.GameOver()

    if usert.ycor() > 280:
        scoreboard.UpdateScore()
        usert.resetpos()
        car.level_up()























screen.exitonclick()
