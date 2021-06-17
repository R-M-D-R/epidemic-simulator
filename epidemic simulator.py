#
# This is an epidemic simulator. It is done to model the spread of an illness through a population.
#
# To change the parameters of the simulation, alter the four variables written below.
#

incubation_period = 250 # how long the virus incubates
                        # (this is for how long the person does not exhibit any symptoms but they are still able to spread the disease)
sick_time = 250         # for how long the person is sick
mortality_rate = 0.10   # this is a number between 0% and 100%
number_of_balls = 100   # this is the number of people in the simulation


#######################################################################
# import packages
#######################################################################

import pygame, random, math, time
from pygame.locals import *

#######################################################################
# initialize variables and stuff
#######################################################################

# set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (215, 215, 215)
PINK = (255, 125, 125)
PURPLE = (200, 100, 255)
SKY_BLUE = (100, 200, 255)
YELLOW = (255, 255, 100)

# set up population and model features
HEALTHY = "Healthy"
INFECTED = "Infected"
SICK = "Sick"
RECOVERED = "Recovered"
DEAD = "Dead"
healthy_color = YELLOW
infected_color = PINK
sick_color = RED
recovered_color = SKY_BLUE
dead_color = BLACK

healthy_speed = 0.8
infected_speed = 0.8
sick_speed = 0
dead_speed = 0
recovered_speed = healthy_speed

# these variables set up the window for the bouncing balls
box_x = 50
box_y = 150
box_width = 900
box_height = 500

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up display window
background_color = WHITE
(WINDOW_WIDTH, WINDOW_HEIGHT) = (1100, 700)

# define surface
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Bouncing balls')

#######################################################################
# classes
#######################################################################

class Ball:
    def __init__(self, x, y, dx, dy, radius):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

        self.radius = radius
        self.thickness = 0
        self.status = HEALTHY
        self.color = healthy_color
        self.incubation_timer = 0
        self.sick_timer = 0

    def move(self):
        if self.status != SICK and self.status != DEAD:
            if (self.x - self.radius) + self.dx <= box_x:
                self.dx = abs(self.dx)
            elif (self.x + self.radius) + self.dx >= (box_x + box_width):
                self.dx = -abs(self.dx)
            if (self.y - self.radius) + self.dy <= box_y:
                self.dy = abs(self.dy)
            elif (self.y + self.radius) + self.dy >= (box_y + box_height):
                self.dy = -abs(self.dy)
            self.x += self.dx
            self.y += self.dy

    def check_status(self):
        if self.status == INFECTED:
            if self.incubation_timer < incubation_period:
                self.incubation_timer += 1
            else:
                self.status = SICK
                self.color = sick_color
                status[INFECTED] -= 1
                status[SICK] += 1
        elif self.status == SICK:
            if self.sick_timer < sick_time:
                self.sick_timer += 1
            else:
                status[SICK] -= 1
                survived_or_died = random.random()
                if survived_or_died < mortality_rate:
                    self.status = DEAD
                    self.color = dead_color
                    status[DEAD] += 1
                else:
                    self.status = RECOVERED
                    self.color = recovered_color
                    status[RECOVERED] += 1

    def display(self):
        if self.status == DEAD:
            pygame.draw.circle(screen, self.color, (round(self.x), round(self.y)), self.radius, self.thickness)
        elif self.status == RECOVERED:
            pygame.draw.circle(screen, self.color, (round(self.x), round(self.y)), self.radius, self.thickness)
        elif self.status == SICK:
            pygame.draw.circle(screen, self.color, (round(self.x), round(self.y)), self.radius, self.thickness)
            pygame.draw.circle(screen, BLACK, (round(self.x), round(self.y)), self.radius, 1)
        elif self.status == HEALTHY:
            pygame.draw.circle(screen, self.color, (round(self.x), round(self.y)), self.radius, self.thickness)
            pygame.draw.circle(screen, BLACK, (round(self.x), round(self.y)), self.radius, 1)
        else:
            pygame.draw.circle(screen, self.color, (round(self.x), round(self.y)), self.radius, self.thickness)

class Box():
    def draw_box(ball_list):
        # draw the display box
        pygame.draw.rect(screen, BLACK, (box_x, box_y, box_width, box_height), 1)

class Data():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.thickness = 1
        self.color = BLACK

    def update(self):
        if time % check_point == 0:
            healthy = status[HEALTHY]
            sick = status[INFECTED] + status[SICK]
            recovered = status[RECOVERED]
            dead = status[DEAD]
            data_list.append([recovered, healthy, sick, dead])

    def display(self):
        for i in range(0, len(data_list)):
            recovered_height = round(data_list[i][0] / number_of_balls * self.height)
            healthy_height = round(data_list[i][1] / number_of_balls * self.height)
            sick_height = round(data_list[i][2] / number_of_balls * self.height)
            dead_height = round(data_list[i][3] / number_of_balls * self.height)
            if recovered_height > 0:
                pygame.draw.line(screen, recovered_color, (self.x + i, self.y), (self.x + i, (self.y + recovered_height)), self.thickness)
            if healthy_height > 0:
                pygame.draw.line(screen, healthy_color, (self.x + i, self.y + recovered_height), (self.x + i, self.y + recovered_height + healthy_height - self.thickness), self.thickness)
            if sick_height > 0:
                pygame.draw.line(screen, sick_color, (self.x + i, self.y + recovered_height + healthy_height), (self.x + i, self.y + recovered_height + healthy_height + sick_height - self.thickness), self.thickness)
            if dead_height > 0:
                pygame.draw.line(screen, dead_color, (self.x + i, self.y + recovered_height + healthy_height + sick_height), (self.x + i, self.y + recovered_height + healthy_height + sick_height + dead_height - self.thickness), self.thickness)
        # this draws the box around the data graph
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width + 1, self.height), self.thickness)
        # I hate this line because it fudges things and adds code that should be unneccesary.
        # This line adds an extra box around the border so that the data lines never go outside the
        # data box itself. Under certain circumstances (e.g. the right number of balls), data bars will
        # creep outside the data box by a pixel or two, so this next line just draws an extra box
        # around the first box (using the background color)
        # THIS LINE IS ME NOT BEING A CLEVER PROGRAMMER!
        pygame.draw.rect(screen, background_color, (self.x - 2, self.y - 2, self.width + 5, self.height + 4), 3)

#######################################################################
# functions
#######################################################################

def collision(ball1, ball2):
        x_diff = (ball1.x + ball1.dx) - (ball2.x + ball2.dx)
        y_diff = (ball1.y + ball1.dy) - (ball2.y + ball2.dy)
        distance_between = math.hypot(x_diff, y_diff)
        if distance_between <= (ball1.radius + ball2.radius):
            (ball1.dx, ball2.dx) = (ball2.dx, ball1.dx)
            (ball1.dy, ball2.dy) = (ball2.dy, ball1.dy)
            if ball1.status == SICK or ball1.status == INFECTED:
                if ball2.status == HEALTHY:
                    ball2.status = INFECTED
                    ball2.color = infected_color
                    status[INFECTED] += 1
                    status[HEALTHY] -= 1

            elif ball2.status == SICK or ball2.status == INFECTED:
                if ball1.status == HEALTHY:
                    ball1.status = INFECTED
                    ball1.color = infected_color
                    status[INFECTED] += 1
                    status[HEALTHY] -= 1

def draw_text():
        text_x1 = 25
        text_x2 = text_x1 + 140
        text_x3 = text_x2 + 140
        text_y = 25
        font_size = 24
        font = pygame.font.SysFont(None, font_size)

        line1 = ["Population: " + str(number_of_balls), "Time: " + str(time)]
        line2 = ["Healthy: " + str(status[HEALTHY]), "Infected: " + str(status[INFECTED])]
        line3 = ["Sick: " + str(status[SICK]), "Recovered: " + str(status[RECOVERED]), "Dead: " + str(status[DEAD])]

        for i in range(0, len(line1)):
            line = font.render(line1[i], True, BLUE)
            screen.blit(line, (text_x1, text_y + i*font_size))

        for i in range(0, len(line2)):
            line = font.render(line2[i], True, BLUE)
            screen.blit(line, (text_x2, text_y + i*font_size))

        for i in range(0, len(line3)):
            line = font.render(line3[i], True, BLUE)
            screen.blit(line, (text_x3, text_y + i*font_size))

#######################################################################
# main program
#######################################################################

balls = []
radius = 6
speed = healthy_speed

# make the first ball
angle = random.randint(0, 359) * math.pi / 180
dx = speed * math.cos(angle)
dy = speed * (-math.sin(angle))
x = random.randint( box_x + math.ceil(radius + speed + 1),  (box_x + box_width) - math.ceil(radius + speed + 1) )
y = random.randint( box_y + math.ceil(radius + speed + 1),  (box_y + box_height) - math.ceil(radius + speed + 1) )
balls.append( Ball(x, y, dx, dy, radius) )

# make the rest of the balls
# the following checks to make sure the balls are not overlapping upon creation
# if so, then we remake that ball
done_making_balls = False

while len(balls) < number_of_balls:
    # make another ball
    new_x = random.randint(box_x + math.ceil(radius + speed + 1),  box_x + box_width - math.ceil(radius + speed + 1))
    new_y = random.randint(box_y + math.ceil(radius + speed + 1),  box_y + box_height - math.ceil(radius + speed + 1))
    add_ball = True
    for i in range(0, len(balls)):
        x_diff = new_x - balls[i].x
        y_diff = new_y - balls[i].y
        distance_between = math.hypot(x_diff, y_diff)
        if distance_between <= radius + balls[i].radius:
            add_ball = False
            break
    if add_ball == True:
        angle = random.randint(0, 359) * math.pi / 180
        dx = speed * math.cos(angle)
        dy = speed * (-math.sin(angle))
        balls.append(Ball(new_x, new_y, dx, dy, radius))

balls[0].status = INFECTED
balls[0].color = infected_color
status = {HEALTHY : number_of_balls - 1, INFECTED : 1, SICK : 0, RECOVERED : 0, DEAD : 0}
time = 0

PAUSE = False
data_list = [[0, 0, 0, 0]]                  # This is the list of data points that creates the graph.
                                                         # Each element of the list has itself 4 elements:
                                                         # 0: recovered, 1: healthy, 2: infected+sick, 3: dead
databox = Data(450, 10, 500, 100)   # Make the box that displays the graph. The first two values are (x,y)
                                                                # and are the top left corner of the box. The second two values are
                                                                # the width of the box and the height of the box
check_point = 2000 / 500

# the main program
while True:
    mainClock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            PAUSE = True
        elif event.type == pygame.MOUSEBUTTONUP:
            PAUSE = False
        
    if PAUSE == False:
        #erase screen
        screen.fill(background_color)

        # move and display the balls
        for i in balls:
            i.move()
            i.check_status()

        # remove dead balls from the list
        for i in balls:
            if i.status == DEAD:
                balls.remove(i)

        for i in range(0, len(balls)):
            for j in range(i+1, len(balls)):
                if balls[i].status != DEAD and balls[j].status != DEAD:
                    collision(balls[i], balls[j])
            balls[i].move()
            balls[i].display()

        Box.draw_box(balls)   # draw the box of balls
        draw_text()                 # type the text onto the screen
        if time < 2000:
            databox.update()      # update the info for the graph
            time += 1                   # increment the timer
        databox.display()          # draw the graph

        # the following group of code creates the information text when the mouse
        # cursor is placed over the data graph
        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseX > databox.x and mouseX < databox.x + databox.width:
            if mouseY > databox.y and mouseY < databox.y + databox.height:
                # this draws the vertical line
                pygame.draw.line(screen, BLUE, (mouseX, databox.y + databox.thickness), (mouseX, databox.y + databox.height - databox.thickness), 3)
                # this draws the tiny box upon which the text will be written
                pygame.draw.rect(screen, GREY, (mouseX + 5, databox.y + databox.height + 5, 110, 100), 0)
                # the following code writes the actual text
                textX = 10      # this is the top left corner x-value placement of the text
                textY = 10      # this is the top left corner y-value placement of the text
                text_color = BLACK
                font_size = 24
                font = pygame.font.SysFont(None, font_size)
                position = mouseX - databox.x   # this is the x-position of the mouse with respect to the start of the graph
                # there is a try statement because this will only work if the cursor isn't too far to the right,
                # otherwise there isn't enough info to fill in the text
                # (the info is coming from a list, so if the cursor is too far to the right, then it will be out of
                # index for the list)
                try:
                    text = ["Time: " + str(4 * position), "Healthy: " + str(data_list[position][0] + data_list[position][1]), "Sick: " + str(data_list[position][2]), "Dead: " + str(data_list[position][3])]
                except:
                    text = ["Time: " + str(4 * position), "Healthy: -", "Sick: -", "Dead: -"]
                for i in range(0, 4):
                    # print the text to the little box
                    line = font.render(text[i], True, text_color)
                    screen.blit(line, (mouseX + textX, databox.y + databox.height + textY + i*font_size))

        pygame.display.flip()   # display the new screen
