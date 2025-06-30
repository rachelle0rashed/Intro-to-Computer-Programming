def clean():
    while front_is_clear():
        if balls_present():
            take_ball()
                
        if no_balls_present():
            move()
            if balls_present():
                take_ball()
    
        
            
def next_row():
    if balls_present():
            take_ball()
    if front_is_blocked():
        if right_is_clear():
            turn_right()
            move()
            turn_right()
            clean()
        if left_is_clear():
            turn_left()
            move()
            turn_left()
            clean()
def starting_position():
    while not_facing_west():
        turn_left()
    while front_is_clear():
        move()
    turn_left()
    while front_is_clear():
        move()
        
def clean_board():
    clean()
    for i in range(20):
        next_row()
    starting_position()
    
clean_board()