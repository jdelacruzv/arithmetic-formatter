# Returns string containing at least one letter
def only_letters(lst):
    letter = ''
    for x in lst:
        for y in x:
            if not y.isdigit():
                letter = letter + y.strip()
    return letter


def convert_list(lst):
    # Convert the list to a string
    str = ' '.join(lst)
    # Convert the string to a list
    lst = str.split()
    return lst


# Validates if the list returns true or false
def validate_true_false(lst):
    result = convert_list(lst)
    temp = False
    for res in result:
        if len(res) > 4:
            temp = True
    return temp


def validate_errors(lst):
    letters = only_letters(lst)
    print('String:', letters)

    if len(lst) > 5:
        print('Error: Too many problems')

    if ('*' in letters) or ('/' in letters):  # aqui esta mal
        print('Error: Operator must be \'+\' or \'-\'')

    for letter in letters:
        if letter.isalpha():
            print('Error: Numbers must only contain digits')
            break

    if validate_true_false(lst):
        print('Error: Numbers cannot be more than four digits')
    

def arithmetic_arranger(problems, show_answers=False):
    validate_errors(problems)


# arithmetic_arranger(['32 + 698', '3801 - 2', '45 + 43', '123 + 49', '1', '2'])
# arithmetic_arranger(['32 + 698', '3801 / 2', '45 + 43', '123 * 49'])
# arithmetic_arranger(['e2 + 698', '3801 - 2', '45 + 43', '123 + 49'])
# arithmetic_arranger(['32 + 698', '38011 - 2', '45 + 43', '123 + 49'])
# arithmetic_arranger(['xxxxx32 + 698', '3801 * 2', '45 + 43', '123 + 49', '1', '2'])
arithmetic_arranger(['32 + 698', '3801 - 2', '45 + 43', '123 + 49'])
