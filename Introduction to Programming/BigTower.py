# This program draws a big tower from Karel's starting spot
while facing_south():
    turn_around()
while facing_east():
    turn_left()
while facing_west():
    turn_right()
while front_is_clear():
    put_ball()
    move()
put_ball()