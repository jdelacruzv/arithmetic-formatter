# Returns string containing at least one letter
def only_letters(lst):
    letter = ''
    for x in lst:
        for y in x:
            if not y.isdigit():
                letter = letter + y.strip()
    return letter


def z():
    pass

# Returns a boolean
def count_digits(lst):
    lst_to_str = ' '.join(lst)
    str_to_lst = lst_to_str.split()
    print('Original:', lst)
    print('Cadena:', lst_to_str)
    print('Lista:', str_to_lst)
    
    temp = False
    for x in str_to_lst:
        if len(x) > 4:
            temp = True
    return temp


def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        print('Error: Too many problems')

    letters = only_letters(problems)
    print('String:', letters)

    if ('*' in letters) or ('/' in letters):  # aqui esta mal
        print('Error: Operator must be \'+\' or \'-\'')

    for letter in letters:
        if letter.isalpha():
            print('Error: Numbers must only contain digits')

    a = count_digits(problems)
    if a:
        print('Error: Numbers cannot be more than four digits')
    else:
        print('OK')

# arithmetic_arranger(['32 + 698', '3801 - 2', '45 + 43', '123 + 49', '1', '2'])
# arithmetic_arranger(['32 + 698', '3801 / 2', '45 + 43', '123 * 49'])
# arithmetic_arranger(['e2 + 698', '3801 - 2', '45 + 43', '123 + 49'])
arithmetic_arranger(['32 + 698', '38011 - 2', '45 + 43', '123 + 49'])
