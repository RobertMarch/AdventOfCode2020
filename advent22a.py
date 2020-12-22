from TestRunner import run_tests
from inputs.input22 import puzzle_input, test_cases_a


def solve(input):
    deck_a, deck_b = extract_decks(input)

    while len(deck_a) > 0 and len(deck_b) > 0:
        deck_a, deck_b = play_turn(deck_a, deck_b)

    return evaluate_decks(deck_a, deck_b)


def extract_decks(input):
    dA, dB = input.split('\n\n')
    deck_a = [int(card) for card in dA.splitlines()[1:]]
    deck_b = [int(card) for card in dB.splitlines()[1:]]
    return deck_a, deck_b


def play_turn(deck_a, deck_b):
    card_a = deck_a.pop(0)
    card_b = deck_b.pop(0)
    if card_a > card_b:
        deck_a.append(card_a)
        deck_a.append(card_b)
    else:
        deck_b.append(card_b)
        deck_b.append(card_a)
    return deck_a, deck_b


def evaluate_decks(deck_a, deck_b):
    deck = deck_a if len(deck_a) > 0 else deck_b
    result = 0
    for i in range(1, len(deck) + 1):
        result += i * deck[-1 * i]
    return result


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
