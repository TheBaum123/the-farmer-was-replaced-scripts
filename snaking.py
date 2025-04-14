# replace hats; happens every time you can no longer move
def re_hat():
    change_hat(Hats.Straw_Hat)
    change_hat(Hats.Dinosaur_Hat)


clear()
# set the world size to even number
set_world_size(get_world_size() - get_world_size() % 2)
# infinite loop
while True:
    # initial hat change
    change_hat(Hats.Dinosaur_Hat)
    # logic that even I don't understand anymore
    while move(East):
        # move bottom to top
        while get_pos_y() < get_world_size() - 1:
            # move left to right
            if get_pos_y() % 2 == 0:
                while get_pos_x() < get_world_size() - 1:
                    if not move(East):
                        re_hat()
            # move right to left
            else:
                while get_pos_x() > 1:
                    if not move(West):
                        re_hat()
            # move bottom to top
            if not move(North):
                re_hat()
        # go back to the left
        while get_pos_x() > 0:
            if not move(West):
                re_hat()
        # go back to the bottom
        while get_pos_y() > 0:
            if not move(South):
                re_hat()
