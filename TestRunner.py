def run_tests(test_cases, solve, args=None):
    failed_test = False
    for case in test_cases:
        [expected_answer, case_input] = case
        solution = solve(case_input) if args is None else solve(case_input, args)
        if not solution == expected_answer:
            print('Error in test case: expected {}, got {} for input {}'.format(expected_answer, solution, case_input))
            failed_test = True
    if len(test_cases) == 0:
        print('No test cases given. \n')
    elif not failed_test:
        print('All test cases passed! \n')
    else:
        print('\n')
