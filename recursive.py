import generator
import numpy as np
str1 = 'QrLZNMZ3Egrd'
str2 = 'w0T3QpRLGn'
print(f'Calculating edit distance between "{str1}" and "{str2}"')

# replace can cost either 1 (insert a character on top of another) or 2 (remove a character and then insert the new one)
replace_add_cost = 0  # case where replace is 1 operation (= 1 otherwise)


def prepare_mat(n, m):
    mat = np.full((n+1, m+1), float('inf'))
    mat[0, 0] = 0
    return mat

#operations counter
i = 0
def ed_with_alignement(s1, s2, mat):
    global i
    i += 1
    n = len(s1)
    m = len(s2)
    if(n == 0 or m == 0):
        return max(n, m)
    if(s1[-1] == s2[-1]):
        mat[n, m] = ed_with_alignement(s1[:-1], s2[:-1], mat)
    else:
        insertionBranch = 1+ed_with_alignement(s1[:-1], s2, mat)
        deletionBranch = 1+ed_with_alignement(s1, s2[:-1], mat)
        replaceBranch = ed_with_alignement(
            s1[:-1], s2[:-1], mat) + 1
        mat[n, m] = min(replaceBranch, deletionBranch, insertionBranch)
    return mat[n, m]


def alignment(s1, s2, mat):
    color_red = '\033[91m'
    color_blue = '\033[94m'
    color_purple = '\033[95m'
    color_end = '\033[0m'
    final_string = ''
    
    i = len(s1)
    j = len(s2)

    minval = -1

    while (i, j) != (0, 0):
        diagonal = mat[i-1, j-1]
        vertical = mat[i-1, j]
        horizontal = mat[i, j-1]
        current_position = mat[i, j]
        minval = min(diagonal, vertical, horizontal)
        if(minval == vertical):
            i -= 1
            final_string = color_red + '-' + color_end + final_string
        elif minval == diagonal:
            i -= 1
            j -= 1
            if(minval == current_position):
                final_string = s2[j]+color_end + final_string
            else:
                final_string = color_purple+s2[j]+color_end + final_string
        elif minval == horizontal:
            j -= 1
            final_string = color_blue + s2[j]+color_end + final_string
    return final_string


if __name__ == "__main__":
    matrix = prepare_mat(len(str1), len(str2))
    ed = (ed_with_alignement(str1, str2, matrix))
    print(f'This program took {i} operations to finish.\nThe minimum edit distance is {ed}')
    print(alignment(str1, str2, matrix))
