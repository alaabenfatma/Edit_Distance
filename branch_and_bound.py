'''
Things to keep in mind: 
    - lowerBound will NEVER surpass the length of the longest string
    - if the currentDistance reaches, somehow, the length of the longest string, we break out of the function.
'''
from generator import randomword

str1 = 'cat'
str2 = 'carpet'
print(f'Calculating edit distance between "{str1}" and "{str2}"')

i = 0

k = max(len(str1), len(str2))
'''
-the first 3 table are here for the sake of understanding the problem
-the idea was to store in different tables each ind of operation
-to see what choice has been made or could have been made at that bound or node
-the last table named table is for storing the operations that have been exactly with the algo
'''
insert_table = [0] * k
delete_table = [0] * k
replace_table = [0] * k
table = [0] * k #the table where i will store the operation chosen at each bound (node)

def bounded_ed(a, b, currentDistance, lowerBound):
    """
    Edit distance - but bounded.
    """
    global i
    i += 1
    n = len(a)
    m = len(b)

     
    
   

    if(a == b):
        #update the operations table

        return currentDistance
    if currentDistance >= lowerBound:
        #update the operations table

        return lowerBound
    if (n == 0):
        #update the operations table
        return m + currentDistance
    if (m == 0):
        return n + currentDistance
    if (a[-1] == b[-1]):
         #update the operations table

        return bounded_ed(
            a[:- 1], b[:- 1], currentDistance,
            lowerBound)
           

    else:

        insertionBranch = bounded_ed(a[:n - 1], b, currentDistance + 1, lowerBound)
        deletionBranch = bounded_ed(a, b[:m - 1], currentDistance + 1,
                                    min(insertionBranch, lowerBound))
        replaceBranch = bounded_ed(
            a[:n - 1], b[:m - 1], currentDistance + 1,
            min(insertionBranch, deletionBranch, lowerBound))
        
        '''
        as we need to find what branch will minimize our cost,
        we need to store that operation before calling next recursion
        that's what is done here
        '''
        if(min(insertionBranch, deletionBranch, replaceBranch)==insertionBranch):
            table[currentDistance] = 1 # 1 is for encoding the insertion operation
            insert_table[currentDistance] =1
        elif(min(insertionBranch, deletionBranch, replaceBranch)==deletionBranch):
            delete_table[currentDistance] =1
            table[currentDistance] = 2 # 2 is for encoding the deletion operation
        elif(min(insertionBranch, deletionBranch, replaceBranch)==replaceBranch):
            replace_table[currentDistance] =1
            table[currentDistance] = 3 # 3 is for encoding the replacement operation
    



    return min(insertionBranch, deletionBranch, replaceBranch)

    


print(f'The edit distance equals: {bounded_ed(str1, str2, 0, max(len(str1), len(str2)))} after {i} operations.')


print("insert table is ",  list(reversed(insert_table)))
print("delete table is ",  list(reversed(delete_table)))
print("replace table is ", list(reversed(replace_table)))

'''Since the table stored the operation in a recursive way
   We need to reverse the printage of the table to read from left to right
   We can keep it as it is but rememberif you do that when reading you should start from right to left
'''
print("the operations table is", list(reversed(table)))
