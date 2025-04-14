# import section
import planting_helper


# watering to balance between 5k and 0 water buckets
def smart_water():
    if get_water() < num_items(Items.Water) / 5000:
        use_item(Items.Water)


# little helper to harvest
def smart_harvest():
    if can_harvest():
        harvest()


# main func to delegate tasks
def main():
    clear()
    # loop
    while True:
        # get the world size and loop through its cols and rows
        world_size = get_world_size()
        for i in range(world_size):
            for j in range(world_size):
                # harvest each field
                smart_harvest()
                # water each field
                smart_water()
                # replant each field
                planting_helper.smart_plant()
                # movement
                move(North)
            move(East)


# call main
main()
