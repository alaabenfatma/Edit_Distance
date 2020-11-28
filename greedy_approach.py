import generator
import random


# greedy_approach

def greedy_approach(s1, s2):
    # compute the length of the two strings
    n = len(s1)
    m = len(s2)

    # get the longest and the shortest
    k = min(n, m)
    l = max(n, m)

    # i will store a table of changed part
    modified = ['0'] * l

    '''compute the cost
    the optimal choice when finding two different characters in the first k moves
    (considering k is the length of the shortest string )
    is replacing'''

    cost = 0
    for i in range(k):
        if (s1[i] != s2[i]):
            cost += 1
            s = min(s1, s2)
            modified[i] = '/'
        else :
            modified[i] = '.'

   
    #print("the changed characters in the longest string are these : ")
    for i in range(k,l):
        a = random.randint(0,1)
        #print(a)
        if(a==0):
            modified[i] = '-'
        else:
            modified[i] = '+'

   # print(modified)
    return cost + (l - k), modified # because we should count also the last part where we can only delete or insert


if __name__ == '__main__':
    str1 = 'ki' #generator.randomword(30)
    str2 = 'sittinggfhejkzlrtemjryutkreiopzretyrj' #generator.randomword(30)



    print(f'Approximating edit distance by greedy approach between "{str1}" and "{str2}"')
    print(greedy_approach(str1, str2))