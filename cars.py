import turtle as t 
import random
XCOR = 300
MOVE_CAR_BY = 5

class Cars:
    def __init__(self):
        self.carspeed = MOVE_CAR_BY
        self.carlist = []
        t.colormode(255)
        self.CreateCar()


    def CreateCar(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = t.Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len = 2, stretch_wid= 1)
            new_car.color(self.CustomColor())
            car_ycor = random.randint(-250,250)
            new_car.goto(XCOR, car_ycor)
            self.carlist.append(new_car)


    def CustomColor(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        _ = (r, g, b)
        return _


    def MoveCar(self):
        for car in self.carlist:
            car.backward(self.carspeed)


    def level_up(self):
        self.carspeed +=10