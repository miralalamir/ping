
import turtle

wn=turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("green")
wn.setup(width=800,height=600)
wn.tracer(0)
##########################
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=6,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
##########################
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=6,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
##########################
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=2
##########################
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
    
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
###########################
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
    
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)
###########################

###########################
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
        ###########
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
############################
while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)