'''
The module that is responsible of generating strings.
Usage example:
python generator.py data.text 10
'''
import sys
import random
import string


def randomword(n=0):
    '''
    A function to generate a random string of length n.
    '''
    return ''.join(random.choice(string.ascii_lowercase) for i in range(n))


def generate_file(filename='data.txt', n=0):
    '''
    A function to generate a text file that contains N random strings.
    '''
    file = open(filename, mode='w')
    words = []
    for i in range(int(n)):
        file.write(randomword(random.randint(5, 15)) + '\n')
    file.close()


if __name__ == "__main__":
    generate_file(sys.argv[1], sys.argv[2])
