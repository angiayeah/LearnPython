# implementation of card game - Memory

import simplegui
import random

list = [0,1,2,3,4,5,6,7]
list = list + list
exposed = [False] * 16
count = 0
#exposed[5] = True
random.shuffle(list)
state = 0
prev = 100
next = 100
# helper function to initialize globals
def new_game():
    global count, list, exposed, prev, next, state
    count = 0
    random.shuffle(list)
    exposed = [False] * 16
    prev = 100
    next = 100
    state = 0

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, prev, next, count
    index =  pos[0]//50
    if exposed[index] == True:
        return	#when click the same card, doesn't do anything
    if state == 0:
        if exposed[index] == False:
            exposed[index] = True
            prev = index
        state += 1
        count += 1
    elif state == 1:        
        if exposed[index] == False:
            exposed[index] = True
            next = index
        state += 1
    else:
        if exposed[index] == False:
            exposed[index] = True
        if list[prev] != list[next]:
            exposed[prev] = False
            exposed[next] = False
            count += 1
        prev = index
        next = 100
        state = 1
    print count   
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global label
    label.set_text(count)
    for i,each in enumerate(list):
        canvas.draw_text(str(each), (i*50, 90), 100, 'white')
    
    for i, show in enumerate(exposed):
        if show == False:
            canvas.draw_polygon([(i*50,0 ), ((i+1)*50, 0), ((i+1)*50, 100),(i*50,100)], 2, 'black', 'Green')
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric