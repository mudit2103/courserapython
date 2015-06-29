# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 4
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0,0]
paddle1_pos = [4,0]
paddle1_posend = [4,80]
paddle2_pos = [WIDTH - PAD_WIDTH + 4, 0]
paddle2_posend = [WIDTH - PAD_WIDTH + 4,80]
paddle1_vel = [0,0]
paddle2_vel = [0,0]
redscore = 0
bluescore = 0
paddlespeed = 3

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    vert = random.randrange(60, 180) / 60
    hori = random.randrange(120, 240) / 60
    
    if direction == RIGHT:
        ball_vel = [hori,-vert]
    else:
        ball_vel = [-hori,-vert]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global ball_pos, ball_vel, paddle1_pos, paddle1_posend, paddle2_pos, paddle2_posend
    global paddlespeed
    # these are numbers
    global redscore, bluescore  # these are ints
    
    redscore = 0
    bluescore = 0
    paddle1_vel = [0,0]
    paddle2_vel = [0,0]
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [0,0]
    paddle1_pos = [4,0]
    paddle1_posend = [4,80]
    paddle2_pos = [WIDTH - PAD_WIDTH + 4, 0]
    paddle2_posend = [WIDTH - PAD_WIDTH + 4,80]
    paddlespeed=3
    spawn_ball(LEFT)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_posend, paddle2_posend
    global paddle1_vel, paddle2_vel
    global redscore, bluescore, paddlespeed
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if (ball_pos[1]<=BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    elif (ball_pos[1]>=(HEIGHT-1-BALL_RADIUS)):
          ball_vel[1] = -ball_vel[1]
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 10, 'Yellow', 'Orange')
    
    # determine whether ball collides with gutter
    if (ball_pos[0]<=(PAD_WIDTH + BALL_RADIUS)):
        if(ball_pos[1]>(paddle1_pos[1]) and ball_pos[1]<(paddle1_posend[1])):
            ball_vel[0] =  -(ball_vel[0]+0.1*ball_vel[0])
            ball_vel[1] =  -(ball_vel[1]+0.1*ball_vel[1])
            paddlespeed += 0.1*paddlespeed
        else:
            bluescore +=1
            spawn_ball(RIGHT)
            
            
    elif (ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS - 1)):
        if(ball_pos[1]>(paddle2_pos[1]) and ball_pos[1]<(paddle2_posend[1])):
            ball_vel[0] = -(ball_vel[0] + 0.1*ball_vel[0])
            ball_vel[1] = (ball_vel[1] + 0.1*ball_vel[1])
            paddlespeed += 0.1*paddlespeed
        else:
            redscore +=1
            spawn_ball(LEFT)
    
    
    
    # update paddle's vertical position, keep paddle on the screen
    if(paddle1_pos[1]+paddle1_vel[1]>=0):
        if(paddle1_pos[1] + paddle1_vel[1]<=HEIGHT-PAD_HEIGHT+1):  
            paddle1_pos[1] += paddle1_vel[1]
    
    if(paddle2_pos[1]+paddle2_vel[1]>=0):
        if(paddle2_pos[1] + paddle2_vel[1]<=HEIGHT-PAD_HEIGHT+1):
            paddle2_pos[1] += paddle2_vel[1]
    
    
    # draw paddles
    paddle1_posend[1] = paddle1_pos[1] + PAD_HEIGHT
    paddle2_posend[1] = paddle2_pos[1] + PAD_HEIGHT
    
    canvas.draw_line(paddle1_pos, paddle1_posend, PAD_WIDTH, 'Red')
    canvas.draw_line(paddle2_pos, paddle2_posend, PAD_WIDTH, 'Blue')
    canvas.draw_text(str(redscore), (100, 40), 25, 'Red')
    canvas.draw_text(str(bluescore), (500, 40), 25, 'Blue')
    
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddlespeed
    
    if(key == simplegui.KEY_MAP['w']):
        paddle1_vel = [0,-paddlespeed]
    if(key == simplegui.KEY_MAP['s']):
        paddle1_vel = [0,paddlespeed]
    if(key == simplegui.KEY_MAP['up']):
        paddle2_vel = [0,-paddlespeed]
    if(key == simplegui.KEY_MAP['down']):
        paddle2_vel = [0,paddlespeed]
        
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if(key == simplegui.KEY_MAP['w']):
        paddle1_vel = [0,0]
    if(key == simplegui.KEY_MAP['s']):
        paddle1_vel = [0,0]
    if(key == simplegui.KEY_MAP['up']):
        paddle2_vel = [0,0]
    if(key == simplegui.KEY_MAP['down']):
        paddle2_vel = [0,0]

def button_handler():
    new_game()


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Restart', button_handler)


# start frame
new_game()
frame.start()
