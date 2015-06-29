# template for "Stopwatch: The Game"
import simplegui


# define global variables
time = 0
times_stopped = 0
times_won = 0
isStopped = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t/600
    t %= 600
    B = t/100
    t %= 100
    C = t/10
    t%=10
    D = t
    return str(A)+":"+str(B)+str(C)+"."+str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_handler():
    timer.start()
    global isStopped
    if isStopped == True:
        isStopped = False
        print "Timer started"

def stop_button_handler():
    timer.stop()
    
    global times_stopped, times_won, isStopped
    if isStopped == False:
        isStopped = True
        times_stopped += 1
        print "Timer stopped"
        
        if (time%10)==0:
            times_won+=1
            
    
def reset_button_handler():
    global time, times_stopped, times_won, isStopped
    print "Timer reset and stopped"
    time = 0
    timer.stop()
    isStopped = True
    times_won = 0
    times_stopped = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1
    print time

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), (250,250), 25, 'White')
    canvas.draw_text(str(times_won)+"/"+str(times_stopped), (450,30), 25, 'White')
    
# create frame
frame = simplegui.create_frame('Stopwatch: The Game!', 500, 500)
start_button = frame.add_button('Start', start_button_handler, 200)
stop_button = frame.add_button('Stop', stop_button_handler, 200)
reset_button = frame.add_button('Reset', reset_button_handler, 200)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric
