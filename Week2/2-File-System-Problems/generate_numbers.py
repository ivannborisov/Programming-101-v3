import sys
from random import randint


def genNum():
    return randint(1, 1000)


def main():

    fname = sys.argv[1]
    num_of_nums = int(sys.argv[2])

    fopen = open(fname, 'w')
    for i in range(1, num_of_nums):
        fopen.write("\"{}\" ".format(genNum()))
    fopen.close()

if __name__ == '__main__':
    main()
