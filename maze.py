clear()
# infinite loop
while True:
    # directions array and initial index
    directions = [North, East, South, West]
    current_direction = 0

    # create maze
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, get_world_size() * num_unlocked(Unlocks.Mazes))

    # move till treasure is found
    while not get_entity_type() == Entities.Treasure:
        # right turn
        current_direction = (current_direction + 1) % len(directions)
        if not move(directions[current_direction]):
            # go one to the left if shit doesn't work
            current_direction -= 2
            current_direction %= len(directions)
    # harvest treasure
    harvest()
