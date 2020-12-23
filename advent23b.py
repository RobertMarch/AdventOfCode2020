from TestRunner import run_tests


TOTAL_CUPS = 1000000


def solve(input):
    input_cup_array = [int(c) for c in input]
    cups = create_extended_dict(input_cup_array)

    current_cup = input_cup_array[0]

    for _ in range(10000000):
        current_cup, cups = play_move(current_cup, cups)

    return evaluate_result(cups)


def create_extended_dict(input_cup_array):
    max_val = max(input_cup_array)

    cups = {}
    for i in range(len(input_cup_array) - 1):
        cups[input_cup_array[i]] = input_cup_array[i + 1]
    cups[input_cup_array[-1]] = max_val + 1

    for i in range(max_val + 1, TOTAL_CUPS):
        cups[i] = i + 1
    cups[TOTAL_CUPS] = input_cup_array[0]

    return cups


def play_move(current_cup, cups):
    moved_cups = [cups[current_cup]]
    for i in range(2):
        moved_cups.append(cups[moved_cups[-1]])

    target_cup = current_cup - 1 if current_cup > 1 else TOTAL_CUPS
    while target_cup in moved_cups:
        if target_cup > 1:
            target_cup -= 1
        else:
            target_cup = TOTAL_CUPS

    target_cup_next = cups[target_cup]

    cups[current_cup] = cups[moved_cups[-1]]
    cups[target_cup] = moved_cups[0]
    cups[moved_cups[-1]] = target_cup_next

    current_cup = cups[current_cup]

    return current_cup, cups


def evaluate_result(cups):
    return cups[1] * cups[cups[1]]


if __name__ == "__main__":
    run_tests([[149245887792, '389125467']], solve)
    print(solve('789465123'))
