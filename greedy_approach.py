import generator



#greedy_approach

def greedy_approach(s1, s2):
    #compute the length of the two strings
    n = len(s1)
    m = len(s2)
    
    #get the longest and the shortest
    k = min(n, m)
    l = max(n, m)

    # i will store a table of changed part
    modified = ['0'] * k

    '''compute the cost
    the optimal choice when finding two different characters in the first k moves
    (considering k is the length of the shortest string )
    is replacing'''
    
    cost = 0
    for i in range(k):
        if(s1[i] != s2[i]):
            cost += 1
            s = min(s1,s2)
            modified[i] = s[i]
    
    print("the changed characters in the longest string are these : ")
    print(modified)
    return cost + (l-k) # because we should count also the last part where we can only delete or insert


if __name__ == '__main__':
    str1 = generator.randomword(10)
    str2 = generator.randomword(15)
    print(f'Approximating edit distance by greedy approach between "{str1}" and "{str2}"')
    print(greedy_approach(str1,str2))