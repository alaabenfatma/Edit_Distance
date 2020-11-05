'''
Things to keep in mind: 
    - lowerBound will NEVER surpass the length of the longest string
    - if the currentDistance reaches, somehow, the length of the longest string, we break out of the function.
'''
from generator import randomword

str1 = 'QrLZNMZ3Egrd'
str2 = 'w0T3QpRLGn'
print(f'Calculating edit distance between "{str1}" and "{str2}"')

i = 0


def bounded_ed(a, b, currentDistance, lowerBound):
    """
    Edit distance - but bounded.
    """
    global i
    i += 1
    n = len(a)
    m = len(b)
    if(a == b):
        return currentDistance
    if currentDistance >= lowerBound:
        return lowerBound
    if (n == 0):
        return m + currentDistance
    if (m == 0):
        return n + currentDistance

    replace = 0 if (a[-1] == b[-1]) else 1

    insertionBranch = bounded_ed(a[:n - 1], b, currentDistance + 1, lowerBound)
    deletionBranch = bounded_ed(a, b[:m - 1], currentDistance + 1,
                                min(insertionBranch, lowerBound))
    replaceBranch = bounded_ed(
        a[:n - 1], b[:m - 1], currentDistance + replace,
        min(insertionBranch, deletionBranch, lowerBound))
    return min(insertionBranch, deletionBranch, replaceBranch)


print(f'The edit distance equals: {bounded_ed(str1, str2, 0, max(len(str1), len(str2)))} after {i} operations.')
