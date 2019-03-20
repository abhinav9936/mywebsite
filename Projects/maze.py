import turtle

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Game")
wn.setup(700,700)

#create pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

    def go_up(self):
        move_to_x=player.xcor()
        move_to_y = player.ycor()+24
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_down(self):
        move_to_x=player.xcor()
        move_to_y = player.ycor()-24
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_left(self):
        move_to_x=player.xcor()-24
        move_to_y = player.ycor()
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_right(self):
        move_to_x=player.xcor()+24
        move_to_y = player.ycor()
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)


#Create levels list
levels = [""]

#define first levels
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX        XX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X  XXX        XXXX  XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXX",
    "X                XXXXXXXX",
    "XXXXXXXXXXXXX    XXXXX  X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXX                     X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX              X",
    "XX   XXXXX              X",
    "XX   XXXXXXXXXXXXX  XXXXX",
    "XX    YXXXXXXXXXXX  XXXXX",
    "XX          XXXX        X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"]

#ADD maze to maxe list
levels.append(level_1)

walls = []
#create function to set up Maze
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character=level[y][x]
            screen_x=-288+(x*24)
            screen_y=288-(y*24)

            if character=="X":
                pen.goto(screen_x,screen_y)
                pen.stamp()
                walls.append((screen_x,screen_y))

            if character == "P":
                player.goto(screen_x,screen_y)

#create class instances
pen=Pen()
player=Player()

#set up the level
setup_maze(levels[1])

#keyboard Binding
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

wn.tracer(0)
#Main Game loop
while True:
    wn.update()
