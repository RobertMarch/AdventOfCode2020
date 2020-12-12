import numpy as np

from TestRunner import run_tests
from inputs.input12 import puzzle_input, test_cases_a

directions = {'N': 0, 'E': 90, 'S': 180, 'W': 270}
direction_vectors = {'N': np.array([0, 1]), 'E': np.array([1, 0]), 'S': np.array([0, -1]), 'W': np.array([-1, 0])}


def solve(input):
    position = np.array([0, 0])
    direction = 'E'
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            action = line[0]
            value = int(line[1:])
            position, direction = perform_action(position, direction, action, value)

    return abs(position[0]) + abs(position[1])


def perform_action(position, direction, action, value):
    if action in 'NESW':
        position = add_vectors(position, direction_vectors[action] * value)
    elif action == 'F':
        position = add_vectors(position, direction_vectors[direction] * value)
    else:
        angle_to_add = value if action == 'R' else -1 * value
        new_angle = (directions[direction] + angle_to_add) % 360
        direction = direction_from_angle(new_angle)
    return position, direction


def direction_from_angle(angle):
    for d, a in directions.items():
        if a == angle:
            return d


def add_vectors(a, b):
    return [sum(x) for x in zip(a, b)]


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
