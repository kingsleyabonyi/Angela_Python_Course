def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    moove()
    turn_left()

for skip in range(0, 6):
    jump()


# skip = 6

# while skip > 0:
#     jump()
#     skip -=1

