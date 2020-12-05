import generator
import numpy as np

str1 = 'x'
str2 = 'y'

print(f'Calculating edit distance between "{str1}" and "{str2}"')

# replace can cost either 1 (insert a character on top of another) or 2 (remove a character and then insert the new one)
replace_add_cost = 0  # case where replace is 1 operation (= 1 otherwise)


def prepare_mat(n, m):

    A = np.zeros((n+1,m+1))
    for i in range(0,n+1):
        A[i,0]=i
        for j in range(i,m+1):
            A[i,j]=j
    return A

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

    color_red = '-'
    color_green = '+'
    color_purple = '/'
    color_end = '.'
    final_string = ''

    i = len(s1)
    j = len(s2)
    while (i, j) != (0, 0):
            vertical = mat[i-1, j]
            horizontal = mat[i, j-1]
            current_position = mat[i, j]
            print(i,j, [current_position])
            if(vertical>=current_position ):
                if(horizontal<current_position):
                    j -= 1
                    final_string = color_green+final_string
                else:
                    i-=1
                    j-=1
                    if(mat[i, j]<current_position):
                        final_string = color_purple+final_string
                    else:
                        final_string = color_end + final_string
            elif(vertical<current_position):
                i -= 1
                final_string = color_red+final_string
    return final_string

def compute(a,b):
    print('Please run the UI for a better experience and to visualize the alignment.')
    matrix = prepare_mat(len(a), len(b))
    ed = (ed_with_alignement(a, b, matrix))
    print(matrix)
    return ed, alignment(a, b, matrix)

print(compute(str1,str2))
