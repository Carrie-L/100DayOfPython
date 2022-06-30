def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def down():
    turn_right()
    move()
    turn_right()
    move()
    while not wall_in_front():
        print("down - not wall_in_front - move")
        move()
    print("down - wall_in_front - turn_left")
    turn_left()     

def jump():
    turn_left()
    print("jump - turn_left")
    move()
    print("jump - move")
    while not right_is_clear():
        move()
    down()
    
while not at_goal():
    if wall_in_front():
        print("not at_goal - wall_in_front - jump")
        jump()
    else:
        print("not at_goal - not wall_in_front - move")
        move()
print("at goal!")           
        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
