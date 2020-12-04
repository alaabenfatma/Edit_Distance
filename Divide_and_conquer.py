import numpy as np


def dynamic_programming(string_1, string_2, fill_path_backwards=False, offset_right = np.array([0,0]), offset_left = np.array([0,0]) ):
    """
    Solve the edit distance problem with dynamic programming.
    :param string_1:
    :param string_2:
    :return: edit_distance between string1 and string2, transformation of string1.
    """
    edit_distance = dynamic_programming_forward(string_1, string_2, len(string_2))
    return edit_distance[-1, -1], set_path(string_1, string_2, edit_distance, False, fill_path_backwards, offset_right, offset_left)

def dynamic_programming_forward(string_1, string_2, k):
    """
    Generate the k first columns of the cost matrice forwards
    """

    m = len(string_1)
    # row string2, column string1
    edit_distance = np.zeros(
        (m + 1, k + 1))
    edit_distance[::, 0] = range(
        0, m + 1)  # first column
    edit_distance[0, ::] = range(
        0, k + 1)  # first row

    for i in range(1, m + 1):
        for j in range(1, k + 1):
            if string_1[i - 1] == string_2[j - 1]:
                # this is true because no adjacent elements by row/column
                edit_distance[i,
                              j] = edit_distance[i - 1, j - 1]
                #have difference >1, so this is always the min
                #when two characters are the same
            else:
                edit_distance[i, j] = 1 + min(edit_distance[i - 1, j],  # remove
                                              edit_distance[i, j - 1], # insert
                                              edit_distance[i - 1, j - 1])  # replace

    return edit_distance

def dynamic_programming_backward(string_1, string_2, k):
    """
    Generate the k first columns of the cost matrice forwards
    """
    m = len(string_1)
    n = len(string_2)

    # row string1, column string2
    edit_distance = np.zeros((m + 1, k + 1))
    edit_distance[::, k] = range(m , -1, -1)  # last column
    edit_distance[m, ::] = range(k , -1, -1)  # last row

    for i in range(m-1 , -1, -1 ):
        for j in range(k-1, -1, -1):
            if string_1[i] == string_2[n+j - k]: #we start comparing from the last character of string2 
                edit_distance[i, j] = edit_distance[i + 1, j + 1] #this is true because no adjacent elements by row/column
                                                                  #have difference >1, so this is always the min    
                                                                  #when two characters are the same
            else:
                edit_distance[i, j] = 1 + min(edit_distance[i+1, j],  # remove
                                              # insert
                                              edit_distance[i, j+1],
                                              edit_distance[i+1, j+1])  # replace

    return edit_distance

# print path can be prettier
def set_path(string_1, string_2, edit_distance, with_colors=True, fill_path_backwards=False, offset_right = np.array([0,0]), offset_left = np.array([0,0])):
    """
    red means replace
    blue means insert
    purple means remove
    color end resets to standard shell color
    :param string_1:
    :param string_2:
    :param edit_distance:
    :return: the transformation of string1 in string2 with the steps.
    """
    color_red = '\033[91m' if with_colors else '-'
    color_blue = '\033[94m' if with_colors else '+'
    color_purple = '\033[95m' if with_colors else ''
    color_end = '\033[0m' if with_colors else ''  

    new_string = ""
    i = len(string_1) 
    j = len(string_2) 

    if ( fill_path_backwards == True ) :
        path[-1 + offset_left[0],-1 + offset_left[1]] = 1
    else:
        path[i + offset_right[0], j + offset_right[1]] = 1
    while (i, j) != (0, 0):
        #declaring the indexes we need to fill the path matrice to prevent repetition
        row_forwards = i + offset_right[0]
        row_backwards = -1 - (len(string_1)-i) + offset_left[0]
        column_forwards = j + offset_right[1]
        column_backwards =  -1 - (len(string_2)-j) + offset_left[1]

        #small optimization, if either one of the strings is empty, just insert/delete the whole thing
        if (i == 0): #case: we do j insertions and end the while loop
            for k in range(j,0,-1): 
                new_string = color_blue + string_2[k - 1] + color_end + new_string
                if ( fill_path_backwards == True ) :
                    path[row_backwards, -2 - (len(string_2)-k)+offset_left[1]] = 1
                else : 
                    path[row_forwards,k-1+offset_right[1]] = 1
            break

        if (j == 0): #case: we do i deletions and end the while loop
            for k in range(i,0,-1): 
                new_string = color_purple + "_" + color_end + new_string
                if ( fill_path_backwards == True ) :
                    path[-2 - (len(string_1)-k)+offset_left[0], column_backwards] = 1
                else : 
                    path[k-1+offset_right[0],column_forwards] = 1
            break

        if string_1[i-1] == string_2[j-1] and edit_distance[i,j] == edit_distance[i-1,j-1]:  # case: don't do anything
            new_string = string_1[i - 1] + new_string 
            if ( fill_path_backwards == True ) :
                path[row_backwards-1, column_backwards-1]=1
            else :
                path[row_forwards-1,column_forwards-1]=1
            i -= 1
            j -= 1
            

        elif string_1[i-1] != string_2[j-1] and edit_distance[i,j] == edit_distance[i-1,j-1] + 1: #case: replace
            new_string = color_red + string_2[j - 1] + color_end + new_string
            if ( fill_path_backwards == True ) :
                path[row_backwards-1, column_backwards-1]=1
            else :
                path[row_forwards-1,column_forwards-1]=1
            i -= 1
            j -= 1
            

        elif edit_distance[i,j] == edit_distance[i-1,j] + 1:  # case: remove
            new_string = color_purple + "_" + color_end + new_string
            if ( fill_path_backwards == True ) :
                path[row_backwards-1 ,row_backwards]=1
            else: 
                path[row_forwards-1,column_forwards]=1
            i -= 1
            

        elif edit_distance[i,j] == edit_distance[i,j-1] + 1:  # case: insert
            new_string = color_blue + string_2[j - 1] + color_end + new_string
            if ( fill_path_backwards == True ) :
                path[column_backwards , column_backwards-1]=1
            else: 
                path[row_forwards,column_forwards-1]=1
            j -= 1
            
    return new_string

def divide_and_conquer_rec(string_1, string_2, fill_path_backwards=False,offset_right = np.array([0,0]), offset_left = np.array([0,0])):
    m = len(string_1)
    n = len(string_2)
    

    #stopping condition
    if ( m < 2 or n < 2):
        dynamic_programming(string_1, string_2, fill_path_backwards, offset_right, offset_left )
        #path[0,0] = 1 
        #path[-1,-1] = 1
        return

    mat_for = dynamic_programming_forward(string_1, string_2, int(n/2) ) 
    #print(mat_for)

    # add 1 if n is unpair, so that both matrices have a shared column
    mat_back = dynamic_programming_backward(string_1, string_2, int(n/2) + (n%2) ) 
    #print (mat_back)
    column =  mat_for[::, int(n/2)] + mat_back[::, 0]

    #the first index for which the sum of c+g is minimal
    min_index = np.where( column == column.min() )[0][0]
    #the values of the new offset are the coordinates of the chosen middle point in the global path coord system
    new_offset_right = np.array([min_index, int(n/2)]) + offset_right
    new_offset_left = np.array([min_index+offset_right[0]-path.shape[0]+1, int(n/2)+offset_right[1]-path.shape[1]+1]) 

    #the common column in the backwards matrice is always the last starting from the end
    col_index = -mat_back.shape[1]
    
    if (fill_path_backwards == False):
        path[min_index+offset_right[0], int(n/2)+offset_right[1]] = 2
    else:
        row_index = -1-(mat_back.shape[0]-1 - min_index)  
        #print("col index: " + str(col_index) + " / row index " + str(row_index) )
        path[row_index+offset_left[0], col_index+offset_left[1]] = 2
    #print("min ind: " + str(min_index))

    #callback D&Q over the two diagonal submatrices
    divide_and_conquer_rec( string_1[:min_index], string_2[:int(n/2)], False, offset_right, new_offset_left.copy() )
    divide_and_conquer_rec( string_1[min_index:], string_2[int(n/2):], True , new_offset_right.copy(), offset_left )
    #print( "first CB: (" + string_1[:min_index] +","+ string_2[:int(n/2)]+")")
    #print( "second CB: (" + string_1[min_index:] +","+ string_2[int(n/2):]+")")

def print_path(string_1, string_2, path) :
    newstring = ""
    ed=0
    def replace(i,j):
        nonlocal newstring,ed
        newstring += "/"
        ed+=1
        return [i+1,j+1]
    def do_nothing(i,j):
        nonlocal newstring
        newstring += "."
        return [i+1,j+1]
    def insert(i,j):
        nonlocal newstring,ed
        newstring += "+"
        ed+=1
        return [i,j+1]
    def remove(i,j):
        nonlocal newstring,ed
        newstring += "-"
        ed+=1
        return [i+1,j]
    
    i,j = 0,0
    while (i,j) != (np.shape(path)[0]-1, np.shape(path)[1]-1) :
        if (i ==  np.shape(path)[0]-1) :
            i,j = insert(i,j)
        elif (j == np.shape(path)[1]-1):
            i,j = remove(i,j)
        else : 
            #print (f"i: {i} ,j: {j}")
            switcher = {
                path[i+1][j] == 1 : remove,
                path[i][j+1] == 1 : insert,
                path[i+1][j+1] == 1 and string_1[i] != string_2[j] : replace,
                path[i+1][j+1] == 1 and string_1[i] == string_2[j] : do_nothing,
            }
            func = switcher.get(True)
            i,j = func(i,j)
    return (ed, newstring)
     
def divide_and_conquer(string_1, string_2):
    #possible paths are turned into '1's in this matrice
    global path
    path = np.zeros( ( len(string1) + 1, len(string2)+1 ) )
    divide_and_conquer_rec(string1, string2)
    #print(path)
    return print_path(string1,string2,path)

if __name__ == '__main__':
    string1 = 'sldjfpdjfsdm'  #string 1 in rows
    string2 = 'sdifjpdsjfpj'
    print( divide_and_conquer(string1, string2) )
    #print( dynamic_programming(string1, string2) )
    
    
    
