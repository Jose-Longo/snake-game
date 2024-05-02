from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self, seg_num):
        self.seg_num = seg_num
        self.segments = []
        self.initial_x_pos = 0
        for _ in range(3):
            self.add_segment((self.initial_x_pos, 0))
        self.head = self.segments[0]

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.setposition(position)
        self.segments.append(segment)
        self.initial_x_pos -= 20

    def extend(self):
        self.add_segment((self.segments[-1].position() - (20, 0)))

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)


    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.initial_x_pos = 0
        for _ in range(3):
            self.add_segment((self.initial_x_pos, 0))
        self.head = self.segments[0]
