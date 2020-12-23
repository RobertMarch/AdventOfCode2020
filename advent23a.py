from TestRunner import run_tests


def solve(input):
    cups = [int(c) for c in input]

    for _ in range(100):
        cups = play_move(cups)

    return evaluate_result(cups)


def play_move(cups):
    current_cup = cups[0]
    moved_cups = cups[1:4]
    cups = cups[:1] + cups[4:]

    target_cup = current_cup - 1
    while target_cup not in cups:
        if target_cup > 1:
            target_cup -= 1
        else:
            target_cup = 9

    target_index = cups.index(target_cup) + 1
    cups[target_index:target_index] = moved_cups
    cups.pop(0)
    cups.append(current_cup)
    return cups


def evaluate_result(cups):
    one_index = cups.index(1)
    cups = cups[one_index + 1:] + cups[:one_index]
    return ''.join([str(c) for c in cups])


if __name__ == "__main__":
    run_tests([['67384529', '389125467']], solve)
    print(solve('789465123'))
