from turtle import Turtle
starting_position=[(0,0),(-20,0),(-40,0)]
a=Turtle()
move_dist=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    a = Turtle()
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for i in starting_position:
            self.add_seg(i)

    def add_seg(self,i):
        ns = Turtle("square")
        ns.color("white")
        ns.penup()
        ns.goto(i)
        self.segment.append(ns)
    def extend(self):
        self.add_seg(self.segment[-1].position())



    def move(self):
        for seg_no in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_no - 1].xcor()
            new_y = self.segment[seg_no - 1].ycor()
            self.segment[seg_no].goto(new_x, new_y)
        self.segment[0].forward(move_dist)

    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)








