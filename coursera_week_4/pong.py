# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_vel = [0, 0]
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
paddle2_pos = [WIDTH-HALF_PAD_WIDTH, HEIGHT/2]
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
increase = 1.3
paddle_increase = 3
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction:	#this means right direction
        ball_vel[0] = random.randrange(120, 240)/100
        ball_vel[1] = -random.randrange(60, 180)/100
    
    else:
        ball_vel[0] = -random.randrange(120, 240)/100.0
        ball_vel[1] = -random.randrange(60, 180)/100.0
    print ball_vel
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    if RIGHT:
        spawn_ball(RIGHT)
    if LEFT:
        spawn_ball(LEFT)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, BALL_RADIUS
    global PAD_WIDTH, RIGHT, LEFT
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text("%d    %d" %(score1,score2), (260, 40), 40, 'Green')
    #hit the upper or bottom wall?
    if ball_pos[1] < BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] > HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        
    
    
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, 'White')
    
    #touch gutters?
    paddle1_upper = paddle1_pos[1]-HALF_PAD_HEIGHT
    paddle1_lower = paddle1_pos[1]+HALF_PAD_HEIGHT
    paddle2_upper = paddle2_range = paddle2_pos[1]-HALF_PAD_HEIGHT
    paddle2_lower = paddle2_pos[1]+HALF_PAD_HEIGHT
    
    if ball_pos[0] <= PAD_WIDTH+BALL_RADIUS and ball_pos[1] >paddle1_upper-BALL_RADIUS and ball_pos[1] < paddle1_lower+BALL_RADIUS: 
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= increase
        ball_vel[1] *= increase
    elif ball_pos[0] <= PAD_WIDTH+BALL_RADIUS:
        score2 += 1
        spawn_ball(RIGHT) 
        
    if ball_pos[0] >= WIDTH-PAD_WIDTH-BALL_RADIUS and ball_pos[1] >paddle2_upper-BALL_RADIUS and ball_pos[1] < paddle2_lower+BALL_RADIUS: 
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= increase
        ball_vel[1] *= increase
    elif ball_pos[0] >= WIDTH-PAD_WIDTH-BALL_RADIUS:
        score1 += 1
        spawn_ball(LEFT) 
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel
    if paddle1_pos[1] <= HALF_PAD_HEIGHT:
        paddle1_pos[1] = HALF_PAD_HEIGHT
    elif paddle1_pos[1] >= HEIGHT- HALF_PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT- HALF_PAD_HEIGHT
    
    if paddle2_pos[1] <= HALF_PAD_HEIGHT:
        paddle2_pos[1] = HALF_PAD_HEIGHT
    elif paddle2_pos[1] >= HEIGHT- HALF_PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT- HALF_PAD_HEIGHT
    # draw paddles
    canvas.draw_line((paddle1_pos[0],paddle1_pos[1]-HALF_PAD_HEIGHT),(paddle1_pos[0],paddle1_pos[1]+HALF_PAD_HEIGHT), PAD_WIDTH, "White")
    canvas.draw_line((paddle2_pos[0],paddle2_pos[1]-HALF_PAD_HEIGHT),(paddle2_pos[0],paddle2_pos[1]+HALF_PAD_HEIGHT), PAD_WIDTH, "White")
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -paddle_increase
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle_increase
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -paddle_increase 
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle_increase 
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["2"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"] or key == simplegui.KEY_MAP["2"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

def button_handler():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', button_handler)

# start frame
new_game()
frame.start()
