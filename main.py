def convert_list(operations):
    # Convert the list to a string
    initial_list = ' '.join(operations)
    # Convert the string to a list
    final_list = initial_list.split()
    return final_list


# Removes characters ('+', '-', '*', '/') from lists
def remove_characters(operations):
    temp = []
    for operation in operations:
        if (operation != '+') and (operation != '-') and (operation != '*') and (operation != '/'):
            temp.append(operation)
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
