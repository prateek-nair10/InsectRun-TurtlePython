import turtle
import random
import time
import math

delay = 0.1



initial=turtle.Screen()
turtle.bgcolor("orange")
if True:
    turtle.hideturtle()
    turtle.penup()

    turtle.write("INSECT RUN",align="center",font=("Freestyle Script",72))
    
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(90)
    turtle.write("Loading...",True,align="right",font=(10))

    def clear():
        turtle.clearscreen()
        
    turtle.ontimer(clear,2000)


shift=turtle.Screen()
shift.delay(5000)    


if True:
    turtle.bgcolor("orange")
    turtle.hideturtle()
    turtle.penup()

    turtle.write("WELCOMEagain",align="center",font=("Magneto",35))
    turtle.hideturtle()
    turtle.penup()
    turtle.bgcolor("lightblue")

    turtle.write("CONTROLS",align="center",font=("Magneto",35))
    

    
    
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(90)
    turtle.write("press A to go left",True,align="left",font=(10))
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.write("press W to go up",True,align="left",font=(10))
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.write("press D to go right",True,align="left",font=(10))
    turtle.backward(100)
    turtle.right(90)
    turtle.backward(200)
    turtle.write("press S to go down",True,align="left",font=(10))
    turtle.backward(100)
    turtle.right(90)
    turtle.fd(20)
    turtle.write("or use ARROW KEYS",font=(6))
    

    def clear():
        turtle.clearscreen()
    turtle.ontimer(clear,2000)

start=turtle.Screen()
start.delay(7000)



if True:
    turtle.hideturtle()
    turtle.penup()

    turtle.write("GET READY",align="center",font=("Copperplate Gothic Bold",35))
    turtle.hideturtle()
    turtle.penup()

    
    turtle.hideturtle()
    turtle.penup()
    turtle.bgcolor("orange")

    turtle.write("GET READY",align="center",font=("Copperplate Gothic Bold",35))
    
    

    def clear():
        turtle.clearscreen()
    turtle.ontimer(clear,300)    



    
screen=turtle.Screen()
screen.delay(1000)




#----------

wn = turtle.Screen()
wn.setup(600,600)

turtle.shape("circle")
turtle.color("red")
turtle.penup()
turtle.speed(40)
turtle.direction = "notmoving"

def up():
    turtle.direction = "up"
def down():
    turtle.direction = "down"
def left():
    turtle.direction = "left"
def right():
    turtle.direction = "right"

def move():
    if turtle.direction == "up":
        y = turtle.ycor()
        turtle.sety(y+28)
    if turtle.direction == "down":
        y = turtle.ycor()
        turtle.sety(y-28)
    if turtle.direction == "left":
        x = turtle.xcor()
        turtle.setx(x-28)
    if turtle.direction == "right":
        x = turtle.xcor()
        turtle.setx(x+28)
        
turtle.listen()    
turtle.onkey(up,"w")
turtle.onkey(down,"s")
turtle.onkey(left,"a")
turtle.onkey(right,"d")
turtle.goto(130,0)

cthr=turtle.Turtle()
cthr.shape("square")
cthr.color("blue")
cthr.penup()
cthr.speed(60)
cthr.goto(-110,0)
cthr.direction = "not moving"

def up2():
    cthr.direction = "up"
def down2():
    cthr.direction = "down"
def left2():
    cthr.direction = "left"
def right2():
    cthr.direction = "right"

def move2():
    if cthr.direction == "up":
        y = cthr.ycor()
        cthr.sety(y+30)
    if cthr.direction == "down":
        y = cthr.ycor()
        cthr.sety(y-30)
    if cthr.direction == "left":
        x = cthr.xcor()
        cthr.setx(x-30)
    if cthr.direction == "right":
        x = cthr.xcor()
        cthr.setx(x+30)
turtle.listen()
turtle.onkeypress(up2,"Up")
turtle.onkeypress(down2,"Down")
turtle.onkeypress(left2,"Left")
turtle.onkeypress(right2,"Right")



#spider image
screen = turtle.Screen()
image = "images~1.gif"

screen.addshape(image)
cthr.shape(image)


#hosefly image
image1 = "download~1.gif"

screen.addshape(image1)
turtle.shape(image1)



def clear():
        turtle.clearscreen()





while True:
    turtle.update()
    move()#move function of turtle
    move2()#move function of cthr
    
    #turlte collide with cthr
    turtle.update()
    x=list(turtle.pos())
    y=list(cthr.pos())
    if math.fabs(x[0]-y[0])<33 and math.fabs(x[1]-y[1])<33:
        turtle.clearscreen()
        turtle.hideturtle()
        turtle.penup()
        turtle.bgcolor("grey")
        turtle.write("GAME OVER",align="Center",font=("MS Comic Sans",35))
        turtle.backward(1)
        turtle.right(90)
        turtle.forward(40)
        turtle.write("click anywhere to exit",True,align="right",font=(10))
        turtle.exitonclick()
    
        

    #turtle stops when it touches the border
    if turtle.xcor()>290:
        turtle.setx(290)
    if turtle.xcor()<-290:
        turtle.setx(-290)
    if turtle.ycor()>290:
        turtle.sety(290)
    if turtle.ycor()<-290:
        turtle.sety(-290)

    #cthr stops when it touches the border
    if cthr.xcor()>280:
        cthr.setx(280)
    if cthr.xcor()<-290:
        cthr.setx(-290)
    if cthr.ycor()>290:
        cthr.sety(290)
    if cthr.ycor()<-280:
        cthr.sety(-280)

    #delays the screen
    time.sleep(delay)

wn.mainloop()
