from TestRunner import run_tests
from inputs.input24 import puzzle_input, test_cases_a


def solve(input):
    flipped_tiles = []

    for route in input.splitlines():
        steps = parse_route(route)
        end_tile = follow_route(steps)

        if end_tile not in flipped_tiles:
            flipped_tiles.append(end_tile)
        else:
            flipped_tiles.remove(end_tile)

    return len(flipped_tiles)


def parse_route(route):
    steps = []
    curr_step = ''
    for c in route:
        curr_step += c
        if c not in 'ns':
            steps.append(curr_step)
            curr_step = ''

    return steps


def follow_route(steps):
    location = [0, 0]

    move_coords = {'e': [2, 0], 'se': [1, -1], 'sw': [-1, -1], 'w': [-2, 0], 'nw': [-1, 1], 'ne': [1, 1]}

    for step in steps:
        location = add_vectors(location, move_coords[step])

    return location


def add_vectors(a, b):
    return [ai + bi for ai, bi in zip(a, b)]


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
