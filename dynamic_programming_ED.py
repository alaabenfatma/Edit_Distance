import numpy as np
from generator import randomword


def dynamic_programming(string_1, string_2):
    """
    solve the edit distance problem with dynamic programming.
    :param string_1:
    :param string_2:
    :return: edit_distance between string1 and string2, transformation of string1.
    """

    edit_distance = np.zeros((len(string_1) + 1, len(string_2) + 1))  # row string2, column string1
    edit_distance[::, 0] = range(0, len(string_1) + 1)  # first column
    edit_distance[0, ::] = range(0, len(string_2) + 1)  # first row

    matrix_operations = np.zeros((len(string_1) + 1, len(string_2) + 1))
    matrix_operations[1:, 0] = 2  # means remove operations
    matrix_operations[0, 1:] = 3  # means insert operations

    for i in range(1, len(string_1) + 1):
        for j in range(1, len(string_2) + 1):
            if string_1[i - 1] == string_2[j - 1]:
                edit_distance[i, j] = edit_distance[i - 1, j - 1]
                matrix_operations[i, j] = 1
            else:
                edit_distance[i, j] = 1 + min(edit_distance[i - 1, j],  # remove
                                              edit_distance[i, j - 1],  # insert
                                              edit_distance[i - 1, j - 1])  # replace
                update_matrix_operations(matrix_operations, edit_distance, i, j)
    print(print_path(string_1, string_2, matrix_operations))
    return edit_distance[len(string_1), len(string_2)], print_path(string_1, string_2, matrix_operations)


def update_matrix_operations(path, edit_distance, i, j):
    """
    Update the matrix operations
    1 : string1[i] ==  string2[j]
    2 : remove string1[i]
    3 : insert string1[i]
    4 : replace string1[i]
    """
    if edit_distance[i, j] - 1 == edit_distance[i - 1, j]:  # remove
        path[i, j] = 2
    elif edit_distance[i, j] - 1 == edit_distance[i, j - 1]:  # insert
        path[i, j] = 3
    else:
        path[i, j] = 4
    return


def print_path(string_1, string_2, matrix_operations):
    """
    red means replace
    blue means insert
    :param string_1:
    :param string_2:
    :param matrix_operations:
    :return: the transformation of string1 in string2 with the steps.
    """
    color_red = '\033[91m'
    color_blue = '\033[94m'
    color_purple = '\033[95m'

    color_end = '\033[0m'

    new_string = ""
    i = len(string_1)
    j = len(string_2)
    while (i, j) != (0, 0):
        if matrix_operations[i, j] == 1:  # identical symbol
            new_string = string_1[i - 1] + new_string
            i -= 1
            j -= 1
        elif matrix_operations[i, j] == 2:  # remove
            new_string = color_purple + "_" + color_end + new_string
            i -= 1
        elif matrix_operations[i, j] == 3:  # insert
            new_string = color_blue + string_2[j - 1] + color_end + new_string
            j -= 1
        elif matrix_operations[i, j] == 4:  # replace
            new_string = color_red + string_2[j - 1] + color_end + new_string
            i -= 1
            j -= 1
    return new_string


if __name__ == '__main__':
    string1 = randomword(30)
    string2 = randomword(30)
    print("Two randoms strings : ", string1, string2)
    print(dynamic_programming(string1, string2))
