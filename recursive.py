import generator

str1 = generator.randomword(5)
str2 = generator.randomword(5)
print(f'Calculating edit distance between "{str1}" and "{str2}"')

# replace can cost either 1 (insert a character on top of another) or 2 (remove a character and then insert the new one)
replace_add_cost = 0 #case where replace is 1 operation (= 1 otherwise)


def ed(s1, s2, n, m):
    if(n == 0):
        return m
    if(m == 0):
        return n
    if(s1[n-1] == s2[m-1]):
        return ed(s1, s2, n-1, m-1)
    else:
        return 1 + min(ed(s1, s2, n-1, m), ed(s1, s2, n, m-1), ed(s1, s2, n-1, m-1)+replace_add_cost)


print(f'The edit distance equals: {ed(str1, str2, len(str1), len(str2))}')
