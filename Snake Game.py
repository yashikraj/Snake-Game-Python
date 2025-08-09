from turtle import Turtle,Screen
from my_snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
s=Screen()
s.setup(width=600,height=600)
s.bgcolor("black")
s.title("Snake Game")
starting_position=[(0,0),(-20,0),(-40,0)]
segment=[]
s.tracer(0)
turtle=Turtle()
snake=Snake()
food=Food()
scoreboard=Scoreboard()
s.listen()
s.onkey(fun=snake.up,key="Up")
s.onkey(fun=snake.down,key="Down")
s.onkey(fun=snake.left,key="Left")
s.onkey(fun=snake.right,key="Right")


game=True
while game:
    s.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <- 280:
        game=False
        scoreboard.game_over()

    for segment in snake.segment:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()












s.exitonclick()
