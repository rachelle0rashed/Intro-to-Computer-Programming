"function for Karel to make the tower"
def tower():
    put_ball()
    move()
    put_ball()
    move()
    put_ball()
    
"function for Farel to turn right"  
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

move()
turn_left()
tower()
#Make first tower
move()
turn_right()
move()
move()
turn_right()
move()
tower()
#Make the second tower
turn_left()
turn_left()
move()
move()
move()
turn_right()
##Karel faces the right on top of the tower