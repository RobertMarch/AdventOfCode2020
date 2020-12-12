import numpy as np

from TestRunner import run_tests
from inputs.input12 import puzzle_input, test_cases_b

direction_vectors = {'N': np.array([0, 1]), 'E': np.array([1, 0]), 'S': np.array([0, -1]), 'W': np.array([-1, 0])}


def solve(input):
    position = np.array([0, 0])
    waypoint = np.array([10, 1])
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            action = line[0]
            value = int(line[1:])
            position, waypoint = perform_action(position, waypoint, action, value)

    return abs(position[0]) + abs(position[1])


def perform_action(position, waypoint, action, value):
    if action in 'NESW':
        waypoint = add_vectors(waypoint, direction_vectors[action] * value)
    elif action == 'F':
        position = add_vectors(position, waypoint * value)
    else:
        rotate_angle = (value if action == 'R' else -1 * value) % 360
        waypoint = rotate_waypoint(waypoint, rotate_angle)
    return position, waypoint


def rotate_waypoint(waypoint, angle):
    for _ in range(int(angle / 90)):
        waypoint = np.array([waypoint[1], -waypoint[0]])
    return waypoint


def add_vectors(a, b):
    return np.array([sum(x) for x in zip(a, b)])


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
