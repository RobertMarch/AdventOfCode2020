MODULO_NUMBER = 20201227


def solve(a, b):
    val = 1
    subject_number = 7
    for loop_count in range(MODULO_NUMBER):
        if val == a:
            return encrypt(b, loop_count)
        elif val == b:
            return encrypt(a, loop_count)
        val = (val * subject_number) % MODULO_NUMBER

    return -1


def encrypt(subject, loops):
    val = 1
    for _ in range(loops):
        val = (val * subject) % MODULO_NUMBER
    return val


if __name__ == "__main__":
    print('Test case result: ', solve(5764801, 17807724))
    print(solve(8252394, 6269621))
