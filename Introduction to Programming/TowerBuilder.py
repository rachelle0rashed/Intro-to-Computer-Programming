def tower():
    turn_left()
    put_ball()
    move()
    put_ball()
    move()
    put_ball()
    turn_around()
    move()
    move()
    turn_around()
    turn_right()

def next_column():
    if front_is_clear():
        move()
        if front_is_clear():
            move()
            tower()

tower()

while front_is_clear():
    next_column()