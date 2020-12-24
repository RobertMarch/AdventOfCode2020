from TestRunner import run_tests
from inputs.input24 import puzzle_input, test_cases_b

DIRECTIONS = {'e': [2, 0], 'se': [1, -1], 'sw': [-1, -1], 'w': [-2, 0], 'nw': [-1, 1], 'ne': [1, 1]}


def solve(input):
    flipped_tiles = []

    for route in input.splitlines():
        steps = parse_route(route)
        end_tile = follow_route(steps)

        if end_tile not in flipped_tiles:
            flipped_tiles.append(end_tile)
        else:
            flipped_tiles.remove(end_tile)

    for _ in range(100):
        flipped_tiles = simulate_day(flipped_tiles)

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
    for step in steps:
        location = add_vectors(location, DIRECTIONS[step])

    return location


def simulate_day(initial_black_tiles):
    updated_black_tiles = []
    checked_tiles = []
    for tile in initial_black_tiles:
        checked_tiles.append(tile)
        if 1 <= count_neighbours(tile, initial_black_tiles) <= 2:
            updated_black_tiles.append(tile)
        for loc in DIRECTIONS.values():
            new_tile = add_vectors(tile, loc)
            if new_tile not in initial_black_tiles and new_tile not in checked_tiles:
                checked_tiles.append(new_tile)
                if count_neighbours(new_tile, initial_black_tiles) == 2:
                    updated_black_tiles.append(new_tile)
    return updated_black_tiles


def count_neighbours(location, black_tiles):
    count = 0
    for loc in DIRECTIONS.values():
        if add_vectors(location, loc) in black_tiles:
            count += 1
    return count


def add_vectors(a, b):
    return [ai + bi for ai, bi in zip(a, b)]


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
