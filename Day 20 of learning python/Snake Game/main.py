from turtle import Screen, Turtle
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



screen.exitonclick()

# Segment_1 = Turtle("square")
# Segment_1 . color("white")
#
# Segment_2 = Turtle("square")
# Segment_2 . color("white")
# Segment_2 . goto(-20, 0)
#
# Segment_3 = Turtle("square")
# Segment_3 . color("white")
# Segment_3 . goto(-40, 0)
#



