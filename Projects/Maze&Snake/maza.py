import turtle
import math
import random

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Game")
wn.setup(700,700)
wn.tracer(0)

#register shapes
images=["magician.gif","magician_left.gif","wall.gif","box.gif","enemy_left.gif","enemy_right.gif"]
for image in images:
    turtle.register_shape(image)
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
        self.shape("magician.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold=0

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
        self.shape("magician_left.gif")

    def go_right(self):
        move_to_x=player.xcor()+24
        move_to_y = player.ycor()
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        self.shape("magician.gif")

    def is_collision(self,other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance =math.sqrt((a ** 2)+(b ** 2))
        if distance < 5 :
            return True
        else :
            return False

class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("box.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold=100
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("enemy_left.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold=25
        self.goto(x,y)
        self.direction = random.choice(["up","down","left","right"])

    def move(self):
        if self.direction == "up":
            dx=0
            dy=24
        elif self.direction == "down":
            dx=0
            dy=-24
        elif self.direction == "left":
            dx=-24
            dy=0
            self.shape("enemy_left.gif")
        elif self.direction == "right":
            dx=24
            dy=0
            self.shape("enemy_right.gif")
        else:
            dx=0
            dy=0

        #check if player is is_close if yes head in that direction
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction ="left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        #calculate the spot to move on
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor()+dy
        #chech if wall
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        else:
            #choose another direction
            self.direction = random.choice(["up","down","left","right"])

        #set timer to move next time
        turtle.ontimer(self.move, t=random.randint(100,300))

    def is_close(self,other):
        a =self.xcor()-other.xcor()
        b =self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2)+(b ** 2))
        if distance<50:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

#treasure list
treasures=[]
#Create levels list
levels = [""]

#define first levels
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX       EXX",
    "XXXXXX  XX  XXXT       XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X  XXX        XXXX  XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXX",
    "X                XXXXXXXX",
    "XXXXXXXXXXXXX    XXXXX  X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXXE                    X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX              X",
    "XX   XXXXX              X",
    "XX   XXXXXXXXXXXXX  XXXXX",
    "XX    YXXXXXXXXXXX  XXXXX",
    "XX          XXXX        X",
    "XXXXT                   X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"]

#ADD maze to maxe list
levels.append(level_1)

walls = []
enemies = []
#create function to set up Maze
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character=level[y][x]
            screen_x=-288+(x*24)
            screen_y=288-(y*24)

            if character=="X":
                pen.goto(screen_x,screen_y)
                pen.shape("wall.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))

            if character == "P":
                player.goto(screen_x,screen_y)

            if character == "T":
                treasures.append(Treasure(screen_x,screen_y))

            if character == "E":
                enemies.append(Enemy(screen_x,screen_y))

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

#start movieng enemies
for enemy in enemies:
    turtle.ontimer(enemy.move,t=250)
#Main Game loop
while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold:{}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)

    for enemy in enemies:
        if player.is_collision(enemy):
            print("Player dies!")
            turtle.color("red")
            turtle.penup()
            turtle.goto(-100,0)
            turtle.pendown()
            turtle.write("Player died",align="left",font=("Arial", 48, "normal"))
            turtle.hideturtle()
            turtle.delay(10000)
            turtle.bye()
    wn.update()
