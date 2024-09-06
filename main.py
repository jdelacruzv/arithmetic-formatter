# Converting list to string
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


# Returns true if all elements are digits
def only_digits(operations):
    is_true = False
    for operation in operations:
        if not operation.isdigit():
            is_true = True
    return is_true
    

# Validate that the number is less than four digits
def length_digits(operations):
    is_true = False
    for operation in operations:
        if len(operation) > 4:
            is_true = True
    return is_true


def arithmetic_arranger(problems, show_answers=False):
    data = [[], [], [], []]
    final_data = []
    results = convert_list(problems)
    digits = remove_characters(results)
    space_len = 4
    separator = ' ' * space_len

    if len(results) > 6:
        return print('Error: Too many problems.')

    elif ('*' in results) or ('/' in results):
        return print("Error: Operator must be '+' or '-'.")

    elif only_digits(digits):
        return print('Error: Numbers must only contain digits.')

    elif length_digits(digits):
        return print('Error: Numbers cannot be more than four digits.')

    else:
        for problem in problems:
            items = problem.split(' ')

            if len(items[2]) >= len(items[0]):
                second = f'{items[1]} {items[2]}'
            else:
                second = f'{items[1]}{' ' * (len(items[0]))}{items[2]}'

            data[0].append(' ' * (len(second) - len(items[0])) + items[0])
            data[1].append(second)
            data[2].append('-' * len(second))

            # Evaluates a mathematical expression passed as a string
            sum_items = eval(items[0] + items[1] + items[2])
            data[3].append(' ' * (len(second) - len(str(sum_items))) + str(sum_items))

        if show_answers:
            final_data.append(separator.join(data[0]))
            final_data.append(separator.join(data[1]))
            final_data.append(separator.join(data[2]))
            final_data.append(separator.join(data[3]))
        else:
            final_data.append(separator.join(data[0]))
            final_data.append(separator.join(data[1]))
            final_data.append(separator.join(data[2]))

        return '\n'.join(final_data)


#####  Test  #####
print(f'{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
print(f'{arithmetic_arranger(["1 + 2", "1 - 9380"])}')
print(f'{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
print(f'{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')
print(f'{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
print(f'{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
