"""
 This program has Karel paint a checkerboard
"""
def paint_board():
    paint(color['black'])
    while front_is_clear():
        if color_is(color['red']):
            move()
            paint(color['black'])
                
        if color_is(color['black']):
            move()
            paint(color['red'])
    
        
            
def next_row():
    if front_is_blocked():
        if right_is_clear():
            turn_right()
            move()
            turn_right()
            paint_board()
        if left_is_clear():
            turn_left()
            move()
            turn_left()
            paint_board()
def starting_position():
    turn_left()
    while front_is_clear():
        move()
    turn_left()
        
def checker_board():
    paint_board()
    for i in range(4):
        next_row()
    starting_position()
    
checker_board()