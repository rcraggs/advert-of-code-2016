__author__ = 'Richard Craggs'


def day1_part1():

    intructions = "R1, L3, R5, R5, R5, L4, R5, R1, R2, L1, L1, R5, R1, L3, L5, L2, R4, L1, R4, R5, L3, R5, L1, R3, L5, R1, L2, R1, L5, L1, R1, R4, R1, L1, L3, R3, R5, L3, R4, L4, R5, L5, L1, L2, R4, R3, R3, L185, R3, R4, L5, L4, R48, R1, R2, L1, R1, L4, L4, R77, R5, L2, R192, R2, R5, L4, L5, L3, R2, L4, R1, L5, R5, R4, R1, R2, L3, R4, R4, L2, L4, L3, R5, R4, L2, L1, L3, R1, R5, R5, R2, L5, L2, L3, L4, R2, R1, L4, L1, R1, R5, R3, R3, R4, L1, L4, R1, L2, R3, L3, L2, L1, L2, L2, L1, L2, R3, R1, L4, R1, L1, L4, R1, L2, L5, R3, L5, L2, L2, L3, R1, L4, R1, R1, R2, L1, L4, L4, R2, R2, R2, R2, R5, R1, L1, L4, L5, R2, R4, L3, L5, R2, R3, L4, L1, R2, R3, R5, L2, L3, R3, R1, R3";
    instruction_list = intructions.split(", ")

    directions = ['n', 'e', 's', 'w']
    current_direction_index = 0

    direction_counter = {'n': 0, 'e': 0, 'w': 0, 's': 0,}

    for instruction in instruction_list:

        if instruction[0] == 'L':
            current_direction_index -= 1
        else:
            current_direction_index += 1

        current_direction = directions[current_direction_index % 4]
        direction_counter[current_direction] += int(instruction[1:])

    distance = (direction_counter['n'] - direction_counter['s']) + (direction_counter['w'] - direction_counter['e'])
    print("Day 1 distance = %i" % distance)


def day1_part2():

    intructions = "R1, L3, R5, R5, R5, L4, R5, R1, R2, L1, L1, R5, R1, L3, L5, L2, R4, L1, R4, R5, L3, R5, L1, R3, L5, R1, L2, R1, L5, L1, R1, R4, R1, L1, L3, R3, R5, L3, R4, L4, R5, L5, L1, L2, R4, R3, R3, L185, R3, R4, L5, L4, R48, R1, R2, L1, R1, L4, L4, R77, R5, L2, R192, R2, R5, L4, L5, L3, R2, L4, R1, L5, R5, R4, R1, R2, L3, R4, R4, L2, L4, L3, R5, R4, L2, L1, L3, R1, R5, R5, R2, L5, L2, L3, L4, R2, R1, L4, L1, R1, R5, R3, R3, R4, L1, L4, R1, L2, R3, L3, L2, L1, L2, L2, L1, L2, R3, R1, L4, R1, L1, L4, R1, L2, L5, R3, L5, L2, L2, L3, R1, L4, R1, R1, R2, L1, L4, L4, R2, R2, R2, R2, R5, R1, L1, L4, L5, R2, R4, L3, L5, R2, R3, L4, L1, R2, R3, R5, L2, L3, R3, R1, R3";
    instruction_list = intructions.split(", ")

    directions = ['n', 'e', 's', 'w']
    current_direction_index = 0

    current_x = 0
    current_y = 0
    been_locations = []

    direction_counter = {'n': 0, 'e': 0, 'w': 0, 's': 0,}
    up_down = [1,0,-1,0]
    left_right = [0,-1,0,1]

    for instruction in instruction_list:

        if instruction[0] == 'L':
            current_direction_index -= 1
        else:
            current_direction_index += 1

        current_direction_index %= 4
        current_direction = directions[current_direction_index]

        for i in range(0, int(instruction[1:])):
            current_x += left_right[current_direction_index]
            current_y += up_down[current_direction_index]

            if (current_x, current_y) in been_locations:
                print("repeat location %i" % (current_x + current_y))
                return
            else:
                been_locations.append((current_x, current_y))


