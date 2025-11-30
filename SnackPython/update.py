import turtle
import time
import random

# Screen setup
windows = turtle.Screen()
windows.title("Snake Game by Shuvo Sarkar")
windows.bgcolor("black")
windows.setup(width=600, height=600)
windows.tracer(0)

# Score variables
score = 0
high_score = 0
delay = 0.15  # initial speed (Level 1)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("triangle")
head.shapesize(stretch_wid=2, stretch_len=2)
head.color("green")
head.penup()
head.goto(0, 0)
head.setheading(90)
head.direction = "stop"

# Snake eyes
left_eye = turtle.Turtle()
left_eye.speed(0)
left_eye.shape("circle")
left_eye.color("white")
left_eye.shapesize(0.3, 0.3)
left_eye.penup()
left_eye.goto(head.xcor() - 10, head.ycor() + 10)

right_eye = turtle.Turtle()
right_eye.speed(0)
right_eye.shape("circle")
right_eye.color("white")
right_eye.shapesize(0.3, 0.3)
right_eye.penup()
right_eye.goto(head.xcor() + 10, head.ycor() + 10)

# Snake body segments
segments = []

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write(f"Score: {score}  High Score: {high_score}  Level: 1", align="center", font=("Courier", 16, "normal"))

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Keyboard bindings
windows.listen()
windows.onkeypress(go_up, "w")
windows.onkeypress(go_down, "d")
windows.onkeypress(go_left, "j")
windows.onkeypress(go_right, "l")

# Move the snake
def move():
    if head.direction == "up":
        head.setheading(90)
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.setheading(270)
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setheading(180)
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setheading(0)
        head.setx(head.xcor() + 20)
    
    # Eyes move with head
    if head.direction in ["up", "down"]:
        left_eye.goto(head.xcor() - 10, head.ycor() + 10)
        right_eye.goto(head.xcor() + 10, head.ycor() + 10)
    else:
        left_eye.goto(head.xcor(), head.ycor() + 10)
        right_eye.goto(head.xcor(), head.ycor() - 10)

# Game Over function
def game_over():
    head.hideturtle()
    left_eye.hideturtle()
    right_eye.hideturtle()
    food.hideturtle()
    for segment in segments:
        segment.hideturtle()
    
    scoreboard.goto(0, 0)
    scoreboard.write("Well Played!\nTry Again", align="center", font=("Courier", 24, "bold"))
    windows.update()
    time.sleep(3)
    windows.bye()  # closes the window

# Main game loop
while True:
    windows.update()
    
    # Check collision with border
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        # Update high score before game ends
        if score > high_score:
            high_score = score
        game_over()
        break  # exit loop
    
    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        score += 10

        # Update speed / level
        if score < 50:
            delay = 0.15
            level = 1
        elif score < 100:
            delay = 0.1
            level = 2
        elif score < 200:
            delay = 0.07
            level = 3
        else:
            delay = 0.05
            level = 4

        if score > high_score:
            high_score = score

        scoreboard.clear()
        scoreboard.write(f"Score: {score}  High Score: {high_score}  Level: {level}", align="center", font=("Courier", 16, "normal"))

    # Move the end segments in reverse order
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    
    # Move segment 0 to head
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())
    
    move()
    time.sleep(delay)
