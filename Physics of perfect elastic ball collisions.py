# imports
import pygame
from math import sqrt
from random import randint, uniform


# some variables
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
FPS = 60
BACKGROUND_COLOR = (255, 255, 255)
BALLS_COLOR = (31, 132, 155)
BALLS_SIZE = 30
NUMBER_OF_BALLS = 10
BALLS_SPEED = 5
RED_LAUNCH_TIME = 100
STOP_TIME = 3600 + RED_LAUNCH_TIME
RED = (155, 31, 31)
RED_SPEED = BALLS_SPEED / 10


# ball class
class Ball:

    def __init__(self, x, y, x_speed, y_speed, radius, color):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.radius = radius
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


def collision_check(ball1, ball2):
    # finds distance between two centres of the balls and sum of their radiates
    center_distance = sqrt((ball1.x - ball2.x) ** 2 + (ball1.y - ball2.y) ** 2)
    two_radiates_sum = ball1.radius + ball2.radius
    # returns True when collision and False otherwise
    if center_distance <= two_radiates_sum:
        return True
    else:
        return False


def collision(ball1, ball2):
    # collision calculation
    # 1
    # unit normal vector
    n = [ball1.x - ball2.x, ball1.y - ball2.y]
    un = [n[0] / (n[0] ** 2 + n[1] ** 2) ** (1 / 2), n[1] / (n[0] ** 2 + n[1] ** 2) ** (1 / 2)]
    # unit tangent vector
    ut = [-un[1], un[0]]
    # 2
    # velocity vector for ball1
    v1 = [ball1.x_speed, ball1.y_speed]
    # velocity vector for ball2
    v2 = [ball2.x_speed, ball2.y_speed]
    # 3
    # vectors to plain numbers
    v1n = v1[0] * un[0] + v1[1] * un[1]
    v1t = v1[0] * ut[0] + v1[1] * ut[1]
    v2n = v2[0] * un[0] + v2[1] * un[1]
    v2t = v2[0] * ut[0] + v2[1] * ut[1]
    # 4
    # new tangent velocities
    # there is no friction so this step is not necessary
    # 5
    # new normal velocities
    # there are masses in original formulas, so they are left ones as placeholders
    # but because masses are the same it means v1n, v2n = v2n, v1n
    v1n, v2n = (v1n * (1 - 1) + 2 * 1 * v2n) / (1 + 1), (v2n * (1 - 1) + 2 * 1 * v1n) / (1 + 1)
    # 6
    # scalar values to vectors for ball1
    v1n = [v1n * un[0], v1n * un[1]]
    v1t = [v1t * ut[0], v1t * ut[1]]
    # scalar values to vectors for ball2
    v2n = [v2n * un[0], v2n * un[1]]
    v2t = [v2t * ut[0], v2t * ut[1]]
    # 7
    # new velocity vectors
    v1[0] = v1n[0] + v1t[0]
    v1[1] = v1n[1] + v1t[1]
    v2[0] = v2n[0] + v2t[0]
    v2[1] = v2n[1] + v2t[1]
    # assigment to balls
    ball1.x_speed = v1[0]
    ball1.y_speed = v1[1]
    ball2.x_speed = v2[0]
    ball2.y_speed = v2[1]
    # end of collision calculation

    # moving ball1 and ball2 "out of each other"
    # point of collision
    cx = (ball1.x + ball2.x) / 2
    cy = (ball1.y + ball2.y) / 2
    # distance from collision point to ball1 centre (a bit smaller than radius)
    d = sqrt((ball1.x - cx) ** 2 + (ball1.y - cy) ** 2)
    # if balls are exactly into each other, there are wrong setting
    if d == 0:
        print("Too many, too small or too fast balls.")
        exit(0)
    # distance between point of the collision and ball1 center point in both axes
    dx = ball1.x - cx
    dy = ball1.y - cy
    # proportions in dx, dy, d triangle
    x_ratio = dx / d
    y_ratio = dy / d
    # x and y in new triangle, where radius is instead of d
    new_x = x_ratio * ball1.radius
    new_y = y_ratio * ball1.radius
    # difference between dx, dy and new_x, new_y
    diff_x = new_x - dx
    diff_y = new_y - dy
    # new positions in relation to center (could be in relation to old position)
    # difference times two, so it is like they already bounce back and not get "sticky" first
    ball1.x = cx + dx + 2 * diff_x
    ball1.y = cy + dy + 2 * diff_y
    # same with ball2 in the opposite direction
    ball2.x = cx - dx - 2 * diff_x
    ball2.y = cy - dy - 2 * diff_y
    return ball1, ball2


def move(ball):
    # moving ball
    ball.x = ball.x + ball.x_speed
    ball.y = ball.y + ball.y_speed
    # checking for wall collision
    if ball.x >= SCREEN_WIDTH - BALLS_SIZE:
        ball.x_speed = -ball.x_speed
        ball.x = 2 * SCREEN_WIDTH - ball.x - 2 * BALLS_SIZE
    if ball.x <= BALLS_SIZE:
        ball.x_speed = -ball.x_speed
        ball.x = 2 * BALLS_SIZE - ball.x
    if ball.y >= SCREEN_HEIGHT - BALLS_SIZE:
        ball.y_speed = -ball.y_speed
        ball.y = 2 * SCREEN_HEIGHT - ball.y - 2 * BALLS_SIZE
    if ball.y <= BALLS_SIZE:
        ball.y_speed = -ball.y_speed
        ball.y = 2 * BALLS_SIZE - ball.y
    return ball


# writes prompt and creates screen and clock
print('\nHello! This program allows to play with perfect elastic ball collisions.')
print('\nAll collision formulas based on article by Chad Berchek '
      '"2-Dimensional Elastic Collisions without Trigonometry".')
print('http://www.vobarian.com/collisions/\n')
# On one time unit every ball travels thought as many pixels as their speed says
# It is possible to add masses to this simulation, there is placeholder for it in formulas
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# creating balls
balls = []
for i in range(NUMBER_OF_BALLS):
    balls.append(Ball(randint(BALLS_SIZE, SCREEN_WIDTH - BALLS_SIZE),
                      randint(BALLS_SIZE, SCREEN_HEIGHT - BALLS_SIZE),
                      uniform(-BALLS_SPEED, BALLS_SPEED), uniform(-BALLS_SPEED, BALLS_SPEED),
                      BALLS_SIZE, BALLS_COLOR))

# main loop
time = 0
time_since_last_RED_collision = 0
RED_collision_times = []
RED_collision_distances = []
distance_since_last_collision = 0
while True:
    time += 1
    time_since_last_RED_collision += 1
    if time == STOP_TIME:
        print('Time since RED ball appeared is', time - RED_LAUNCH_TIME, 'frames, which is',
              (time - RED_LAUNCH_TIME) / 60, 'seconds.')
        print('Number of collisions with RED ball is {}.'.format(len(RED_collision_times)))
        if len(RED_collision_times) == 0:
            print('There were no collisions with RED ball.')
        else:
            print('Average time between collision with RED ball is',
                  sum(RED_collision_times) / len(RED_collision_times), 'frames, which is',
                  sum(RED_collision_times) / len(RED_collision_times) / 60, 'seconds.')
            print('Average distance between collision with RED ball is',
                  sum(RED_collision_distances) / len(RED_collision_distances), 'pixels.')
        exit(0)
    if time == RED_LAUNCH_TIME:
        balls.append(Ball(SCREEN_WIDTH - BALLS_SIZE, SCREEN_HEIGHT - BALLS_SIZE, uniform(-RED_SPEED, 0),
                          uniform(-RED_SPEED, 0), BALLS_SIZE, RED))
        time_since_last_RED_collision = 0
    # checks if user wants to close the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Time since RED ball appeared is', time - RED_LAUNCH_TIME, 'frames, which is',
                  (time - RED_LAUNCH_TIME) / 60, 'seconds.')
            print('Number of collisions with RED ball is {}.'.format(len(RED_collision_times)))
            if len(RED_collision_times) == 0:
                print('There were no collisions with RED ball.')
            else:
                print('Average time between collision with RED ball is',
                      sum(RED_collision_times) / len(RED_collision_times), 'frames, which is',
                      sum(RED_collision_times) / len(RED_collision_times) / 60, 'seconds.')
                print('Average distance between collision with RED ball is',
                      sum(RED_collision_distances) / len(RED_collision_distances), 'pixels.')
            exit(0)
    # moves balls and checks if any hits the wall
    for element in balls:
        move(element)
        if element.color == RED:
            distance_since_last_collision = distance_since_last_collision + sqrt(element.x_speed ** 2
                                                                                 + element.y_speed ** 2)
    # checks for collisions between balls
    for ball1_index in range(0, len(balls)):
        for ball2_index in range(ball1_index + 1, len(balls)):
            if collision_check(balls[ball1_index], balls[ball2_index]):
                if balls[ball1_index].color == RED or balls[ball2_index].color == RED:
                    RED_collision_times.append(time_since_last_RED_collision)
                    time_since_last_RED_collision = 0
                    RED_collision_distances.append(distance_since_last_collision)
                    distance_since_last_collision = 0
                balls[ball1_index], balls[ball2_index] = collision(balls[ball1_index], balls[ball2_index])
                # breaks the second for loop, so the balls wont stuck into each other
                break
    # drawing stuff
    screen.fill(BACKGROUND_COLOR)
    for element in balls:
        element.draw()
    pygame.display.flip()
    clock.tick(FPS)
