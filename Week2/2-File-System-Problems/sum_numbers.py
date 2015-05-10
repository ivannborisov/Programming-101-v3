import sys


def main():

    fname = sys.argv[1]

    fopen = open(fname, 'r')
    str_of_nums = fopen.read().replace('"', '')
    fopen.close()

    list_of_nums = str_of_nums.split(' ')
    list_of_nums.pop(len(list_of_nums)-1)
    sum_of_nums = 0

    for x in list_of_nums:
        sum_of_nums += int(x)
    print(sum_of_nums)


if __name__ == '__main__':
    main()
