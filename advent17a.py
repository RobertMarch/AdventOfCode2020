from TestRunner import run_tests
from inputs.input17 import puzzle_input, test_cases_a


def solve(input, cycles=6):
    active_cubes = []
    for y, line in enumerate(input.splitlines()):
        for x, cube in enumerate(line):
            if cube == '#':
                active_cubes.append([x, y, 0])

    for _ in range(cycles):
        new_active_cubes = []
        for x in range(min([cube[0] for cube in active_cubes]) - 1, max([cube[0] for cube in active_cubes]) + 2):
            for y in range(min([cube[1] for cube in active_cubes]) - 1, max([cube[1] for cube in active_cubes]) + 2):
                for z in range(min([cube[2] for cube in active_cubes]) - 1, max([cube[2] for cube in active_cubes]) + 2):
                    coord = [x, y, z]
                    if coord in active_cubes:
                        if count_active_neighbours(coord, active_cubes) in [2, 3]:
                            new_active_cubes.append(coord)
                    else:
                        if count_active_neighbours(coord, active_cubes) == 3:
                            new_active_cubes.append(coord)

        active_cubes = new_active_cubes

    return len(active_cubes)


def count_active_neighbours(coordinate, active_cubes):
    count = 0
    for dx in [-1, 0, 1]:
        x = coordinate[0] + dx
        for dy in [-1, 0, 1]:
            y = coordinate[1] + dy
            for dz in [-1, 0, 1]:
                z = coordinate[2] + dz
                if dx == dy == dz == 0:
                    continue
                if [x, y, z] in active_cubes:
                    count += 1
    return count


if __name__ == "__main__":
    run_tests(test_cases_a, solve, 6)
    print(solve(puzzle_input,6))
