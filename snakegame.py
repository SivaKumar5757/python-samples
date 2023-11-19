from turtle import Turtle,Screen
import time
import random
#initialize
screen=Screen()
screen.setup(1000,800)
screen.bgcolor("black")
screen.title("Dark's Snake Game")
screen.tracer(0)
initial_position=[(0,0),(-20,0),(-40,0)]
blocks=[]
score=0
#score board
dark=Turtle()
dark.penup
dark.hideturtle()
dark.goto(0,360)
dark.color("white")
dark.write(f"Score:{score}",align="center",font=("Courier", 24, "normal"))
#game over 
def gameover():
   dark.home()
   dark.write(f"Game Over",align="center",font=("courier",24,"normal"))
def increasescore():
   dark.write(f"Score:{score}",align="center",font=("Courier", 24, "normal"))

def snake ():
  for position in initial_position:
    block=Turtle("square")
    block.color("white")
    block.penup()
    block.goto(position)
    blocks.append(block)
snake()
def addsnake(z):
   body=Turtle("square")
   body.color("white")
   body.penup()
   body.goto(z)
   blocks.append(body)

#motion
head=blocks[0]
head.setheading(0)
def up ():
   if head.heading()!=270:
      head.setheading(90)
def down ():
   if head.heading()!=90:
      head.setheading(270)
def right ():
   if head.heading()!=180:
      head.setheading(0)
def left ():
   if head.heading()!=0:
      head.setheading(180)
screen.listen()
screen.onkey(up,"Up")
screen.onkey(down,"Down")
screen.onkey(right,"Right")
screen.onkey(left,"Left")
#food
food=Turtle("circle")
food.color("red")
food.shapesize(0.5,0.5)
food.penup()
x=[]
y=[]
for x1 in range (-460,461,20):
   x.append(x1)
for y1 in range (-360,361,20):
   y.append(y1)
#collision with food setup
def refresh():
     randomx=random.choice(x)
     randomy=random.choice(y)
     food.goto(randomx,randomy)
refresh()
life=True
while life:
 screen.update()
 time.sleep(0.1)
#collision with food 
 if head.distance(food)<15:
    score+=1
    dark.clear()
    refresh()
    addsnake(blocks[-1].position())
    addsnake(blocks[-1].position())
    increasescore() 
#colision with wal
 if head.xcor()>480 or head.ycor()>380 or head.xcor()<-480 or head.ycor()<-380:
   gameover()
   life=False

#collision with tail
 for k in blocks:
    if head==k:
       pass
    elif k.position()==head.position():
       gameover()
       life = False
 for n in range (len(blocks)-1,0,-1):
    x2=blocks[n-1].xcor()
    y2=blocks[n-1].ycor()
    blocks[n].goto(x2,y2)
 head.forward(20)


screen.exitonclick()