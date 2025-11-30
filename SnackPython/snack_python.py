import turtle
import time

slow = 0.1

# Making the screen.
windows = turtle.Screen()
windows.title("Snack game made by Shuvo Sarkar")
windows.bgcolor("Black")
windows.setup(width = 550, height = 550)
windows.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")  
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"



# Functions

def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

# Keyboard binding

windows.listen()

windows.onkeypress(go_up, "w")
windows.onkeypress(go_down, "d")
windows.onkeypress(go_left, "l")
windows.onkeypress(go_right, "j")



def run():
    if head.direction == "up":
        corner_of_y = head.ycor()
        head.sety(corner_of_y + 20)

    if head.direction == "down":
        corner_of_y = head.ycor()
        head.sety(corner_of_y - 20)

    if head.direction == "left":
        corner_of_x = head.xcor()
        head.setx(corner_of_x - 20)

    if head.direction == "right":
        corner_of_x = head.xcor()
        head.setx(corner_of_x + 20)


# Main loop
while True:
    windows.update()
    run()
    time.sleep(slow)
windows.mainloop()