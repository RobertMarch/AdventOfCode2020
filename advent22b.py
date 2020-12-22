from TestRunner import run_tests
from inputs.input22 import puzzle_input, test_cases_b


def solve(input):
    deck_a, deck_b = extract_decks(input)

    winner, deck = play_game(deck_a, deck_b)

    return evaluate_deck(deck)


def extract_decks(input):
    dA, dB = input.split('\n\n')
    deck_a = [int(card) for card in dA.splitlines()[1:]]
    deck_b = [int(card) for card in dB.splitlines()[1:]]
    return deck_a, deck_b


def play_game(deck_a, deck_b):
    deck_history = []
    while len(deck_a) > 0 and len(deck_b) > 0:
        if [deck_a, deck_b] in deck_history:
            return 'A', deck_a
        deck_history.append([deck_a.copy(), deck_b.copy()])
        deck_a, deck_b = play_turn(deck_a, deck_b)

    winner = 'A' if len(deck_b) == 0 else 'B'
    deck = deck_a if winner == 'A' else deck_b
    return winner, deck


def play_turn(deck_a, deck_b):
    card_a = deck_a.pop(0)
    card_b = deck_b.pop(0)
    if len(deck_a) >= card_a and len(deck_b) >= card_b:
        winner, _ = play_game(deck_a[:card_a].copy(), deck_b[:card_b].copy())
    else:
        winner = 'A' if card_a > card_b else 'B'
    if winner == 'A':
        deck_a.append(card_a)
        deck_a.append(card_b)
    else:
        deck_b.append(card_b)
        deck_b.append(card_a)
    return deck_a, deck_b


def evaluate_deck(deck):
    result = 0
    for i in range(1, len(deck) + 1):
        result += i * deck[-1 * i]
    return result


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
