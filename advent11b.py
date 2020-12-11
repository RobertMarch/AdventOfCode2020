from TestRunner import run_tests
from inputs.input11 import puzzle_input, test_cases_b


def solve(input):
    seats = []
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            seats.append('.{}.'.format(line))

    seats.insert(0, '.' * len(seats[0]))
    seats.append('.' * len(seats[0]))

    changes_made = True

    while changes_made:
        seats, changes_made = update_seats(seats)

    return count_seats(seats)


def update_seats(seats):
    change_made = False

    new_seats = []
    for i, row in enumerate(seats):
        new_row = ''
        for j, seat in enumerate(row):
            if seat == '.':
                new_row += '.'
                continue

            occupied_directions = count_occupied_directions(seats, i, j)

            if seat == 'L' and occupied_directions == 0:
                new_row += '#'
                change_made = True
            elif seat == 'L' and occupied_directions > 0:
                new_row += 'L'

            if seat == '#' and occupied_directions >= 5:
                new_row += 'L'
                change_made = True
            elif seat == '#' and occupied_directions < 5:
                new_row += '#'
        new_seats.append(new_row)

    return new_seats, change_made


def count_occupied_directions(seats, i, j):
    count = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if dj == 0 and di == 0:
                continue
            i += di
            j += dj
            seat = seats[i][j]
            while 0 <= i < len(seats) and 0 <= j < len(seats[0]) and seat == '.':
                seat = seats[i][j]
                i += di
                j += dj

            if seat == '#':
                count += 1

    return count


def count_seats(seats):
    return sum([row.count('#') for row in seats])


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
