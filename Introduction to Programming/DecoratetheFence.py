def go_to_wall():
    while front_is_clear():
        move()

def lights():
    while front_is_clear():
        if right_is_blocked():
            put_ball()
            move()
        if right_is_clear():
            move()
    put_ball()




go_to_wall()
turn_left()
lights()