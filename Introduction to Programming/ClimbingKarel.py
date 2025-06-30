""" 
Karel needs to find the open slot and
climb up 7 rows. We cannot depend on the 
number of columns. 
"""

"""
Karel will start at the left side of a
row, keep moving across the row until
there is an open spot, then go through
the slot, and return to the start of
the row. 
"""
# Precondition: Karel facing any direction
# Postcondition: Karel moved to next wall in the original direction

def move_to_wall():
    while front_is_clear():
        move()

# Precondition: Karel facing east at the left most avenue.
# Postcondition: Karelf one street higher.
def move_up():
    while left_is_blocked():
        move()
    turn_left()
    move()
    turn_left()
    move_to_wall()
    turn_around()

# We know we will have 8 rows, so we can call
# our move up function 7 times.
for i in range(7):
    move_up()