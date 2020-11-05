import generator

str1 = 'QrLZNMZ3Egrd'
str2 = 'w0T3QpRLGn'
print(f'Calculating edit distance between "{str1}" and "{str2}"')

# replace can cost either 1 (insert a character on top of another) or 2 (remove a character and then insert the new one)
replace_add_cost = 0  # case where replace is 1 operation (= 1 otherwise)
i = 0


def ed(s1, s2, n, m):
    global i
    i += 1
    if (s1 == s2):
        return 0
    if (n == 0):
        return m
    if (m == 0):
        return n
    if (s1[n - 1] == s2[m - 1]):
        return ed(s1, s2, n - 1, m - 1)
    else:
        insertionBranch = ed(s1, s2, n - 1, m)
        deletionBranch = ed(s1, s2, n, m - 1)
        replaceBranch = ed(s1, s2, n - 1, m - 1) + replace_add_cost
        return 1 + min(insertionBranch, deletionBranch, replaceBranch)


print(
    f'The edit distance equals: {ed(str1, str2, len(str1), len(str2))} after {i} operations.'
)
