"""
This program has Karel invert colors
"""
for i in range(10):
    
    if color_is(color['red']):
        paint(color['blue'])
    else:
        paint(color['red'])
    if front_is_clear():
        move()