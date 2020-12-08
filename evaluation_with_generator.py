import sys
import random
import string
import numpy as np
import time
import matplotlib.pyplot as plt
import divide_and_conquer as dc
import dynamic_programming_ED as dp
import naive_recursive as re
import branch_and_bound as bb
import greedy_approach as ga
import k_stripes_dynamic_programming as kdp



def randomword(n=0):
    '''
    A function to generate a random string of length n.
    '''
    return ''.join(random.choice(string.ascii_lowercase) for i in range(n))

def randomword_alphabet(n,alphabet):
    return ''.join(random.choices(alphabet, k=n))

#Time evaluation
#ED evaluation
#alignment evaluation

def evaluation_lenght_variation(n):
    step = 2
    K = 0
    T = int(n / step)
    tab_time = np.zeros((T, 3))
    absysse = np.zeros(T)
    for i in range(step, n+1, step):
        absysse[K] = i
        tab_time_j = np.zeros((3, 3))
        for j in range(3):
            print('j', j)
            string1, string2 = randomword(i), randomword(i)
            curr_time = time.time()
            ED1, alignement = dp.dynamic_programming(string1, string2)
            tab_time_j[0][j] = time.time() - curr_time
            curr_time = time.time()
            ED2, alignement = kdp.K_stripes_DP_ED(string1, string2, 3)
            tab_time_j[1][j] = time.time() - curr_time
            #if i < 10:
            """curr_time = time.time()
            ED3, alignement = re.recursive(string1, string2)
            tab_time_j[2][j] = time.time() - curr_time
            curr_time = time.time()
            ED5, alignement = bb.branch_and_bound(string1, string2)
            tab_time_j[4][j] = time.time() - curr_time
            curr_time = time.time()
            ED4, alignement = ga.greedy_approach(string1, string2)
            tab_time_j[3][j] = time.time() - curr_time"""
            curr_time = time.time()
            ED6, alignement = dc.divide_and_conquer(string1, string2)
            tab_time_j[2][j] = time.time() - curr_time
            print(ED1, ED2, ED6)
        tab_time[K] = np.mean(tab_time_j, axis=1)
        K += 1

    plt.plot(absysse, tab_time)
    #plt.yscale("log")
    #plt.legend(('Dynamic', 'K stripes DP', 'Greedy', 'Branch and Bound'), loc=0)
    plt.legend(('Dynamic', 'K stripes DP', 'Divide and Conquer'), loc=0)
    plt.title("time evaluation according to word length")
    plt.savefig('time_eval_n=20.png')
    plt.show()
    plt.close()


    return

def test():
    a = 4221000
    b = 46.5
    return 19359753 / (a/b)


if __name__ == '__main__':
    print(259.8 / 24)



