# Validate that the list is only digits
def only_digits(str):
    digits = ''
    for x in str:
        for y in x:
            if not y.isdigit():
                digits = digits + y.strip()
    # Returns string without digits
    return digits


def arithmetic_arranger(problems, show_answers=False):
    result = only_digits(problems)
    print(result)

    if len(problems) > 5:
        print('Error: Too many problems')

    if ('*' in result) or ('/' in result):  # aqui esta mal
        print('Error: Operator must be \'+\' or \'-\'')

    for res in result:
        if res.isalpha():
            print('Error: Numbers must only contain digits')


# arithmetic_arranger(['32 + 698', '3801 - 2', '45 + 43', '123 + 49', '1', '2'])
# arithmetic_arranger(['32 + 698', '3801 / 2', '45 + 43', '123 * 49'])
arithmetic_arranger(['e2 + 698', '3801 - 2', '45 + 43', '123 + 49'])
