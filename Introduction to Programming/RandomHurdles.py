def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for i in range(13):
    if front_is_clear():
        move()
    else:
        jump_hurdle()