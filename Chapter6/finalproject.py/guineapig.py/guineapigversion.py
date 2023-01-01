import turtle


#I'm trying to create some basic screen parameters here.
screen = turtle.Screen()
screen.title("One Pong to Rule Them All")
screen.bgpic('mordor3.png')
screen.setup(width=1068, height=600)

#I'll now create a left paddle.
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")
paddle1.shapesize(stretch_wid=6, stretch_len=2)
paddle1.penup()
paddle1.goto(-500, 0)

#paddle1 = turtle.Screen()
#paddle1.speed(0)
#paddle1.shape("square")
#paddle1.bgpic("gondor2.png")
#paddle1.color("blue")
#paddle1.shapesize(stretch_wid=6, stretch_len=2)
#paddle1.penup()
#paddle1.goto(-500, 0)

#And now for the right paddle.
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("red")
paddle2.shapesize(stretch_wid=6, stretch_len=2)
paddle2.penup()
paddle2.goto(500, 0)

#I'm attempting to create a ball here.
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx = 3
ball.dy = -3

#littleball = turtle.Turtle()
#littleball.speed(0)
#littleball.shape("circle")
#littleball.color("black")
#littleball.shapesize(stretch_wid=2,stretch_len=2)
#littleball.penup()
#littleball.goto(0,0)
#littleball.dx = 3
#littleball.dy = -3

def movePad1Up():
    y = paddle1.ycor() #Getting the current y-coordinated of the left paddle
    y += 15
    paddle1.sety(y) #Updating the y-coordinated of the paddle

def movePad1Down():
    y = paddle1.ycor()#Getting the current y-coordinated of the paddle
    y -= 15
    paddle1.sety(y)#Updating the y-coordinated of the paddle

def movePad2Up():
    y = paddle2.ycor()
    y += 15
    paddle2.sety(y)

def movePad2Down():
   y = paddle2.ycor()
   y -= 15
   paddle2.sety(y)

#Trying to create some rudimentary computer control. I found some resources on YouTube that were helpful for this.
if paddle1.ycor() < ball.ycor() and abs(paddle1.ycor() - ball.ycor()) > 10:
    movePad1Up()

elif paddle1.ycor() > ball.ycor() and abs(paddle1.ycor() - ball.ycor()) > 10:
    movePad1Down()

if paddle2.ycor() < ball.ycor() and abs(paddle2.ycor() - ball.ycor()) > 10:
    movePad2Up()

elif paddle2.ycor() > ball.ycor() and abs(paddle2.ycor() - ball.ycor()) > 10:
    movePad2Down()

#Setting up the game.
while True:
    screen.update()

    #Updating ball coordinates.
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #littleball.setx(ball.xcor()+ball.dx)
    #littleball.sety(ball.ycor()+ball.dy)   

    if paddle1.ycor() < ball.ycor() and abs(paddle1.ycor() - ball.ycor()) > 10:
        movePad1Up()

    elif paddle1.ycor() > ball.ycor() and abs(paddle1.ycor() - ball.ycor()) > 10:
        movePad1Down()

    if paddle2.ycor() < ball.ycor() and abs(paddle2.ycor() - ball.ycor()) > 10:
        movePad2Up()

    elif paddle2.ycor() > ball.ycor() and abs(paddle2.ycor() - ball.ycor()) > 10:
        movePad2Down()

#I had to find a good tutorial for this next bit, where I get the ball to bounce.
    if ball.ycor() > 280:
     ball.sety(280)
     ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if (ball.xcor() < -460 and ball.xcor() > -470) and (paddle1.ycor() + 50 > ball.ycor() > paddle1.ycor() - 50):
         ball.dx *=-1

    if (ball.xcor() > 460 and ball.xcor() < 470) and (paddle2.ycor() + 50 > ball.ycor() > paddle2.ycor() - 50):
        ball.dx *=-1


    #if littleball.ycor() > 280:
    # littleball.sety(280)
    # littleball.dy *= -1

    #if littleball.ycor() < -280:
    #    littleball.sety(-280)
    #    littleball.dy *= -1

    #if (littleball.xcor() < -460 and ball.xcor() > -470) and (paddle1.ycor() + 50 > ball.ycor() > paddle1.ycor() - 50):
    #     littleball.dx *=-1

    #if (littleball.xcor() > 460 and ball.xcor() < 470) and (paddle2.ycor() + 50 > ball.ycor() > paddle2.ycor() - 50):
    #    littleball.dx *=-1   