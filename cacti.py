# imports
import planting_helper


# sorting algorithm
def sort_dir(direction, plane_pos_func, secondary_direction):
    # loop ghrough full secondary direction
    for i in range(get_world_size()):
        # start sort loop
        err = True
        while err == True:
            # remove error
            err = False
            # loop through single sorting iteration on sorting plane
            for j in range(get_world_size()):
                if (
                    measure() > measure(direction)
                    and not plane_pos_func() + 1 == get_world_size()
                ):
                    swap(direction)
                    err = True
                move(direction)
        # move to next sorting plane
        move(secondary_direction)


clear()
# main loop
while True:
    # loop through world
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            move(North)
            # plant cacti
            planting_helper.smart_till("cactus")
            plant(Entities.Cactus)
        move(East)
    # call sorting algo
    sort_dir(North, get_pos_y, East)
    sort_dir(East, get_pos_x, North)
    # harvest
    if can_harvest():
        harvest()
