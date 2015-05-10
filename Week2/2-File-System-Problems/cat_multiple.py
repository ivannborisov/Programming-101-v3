# cat.py
import sys


def has_arguments(count=1):
    return len(sys.argv[1:]) >= count


def count_arguments():
    return len(sys.argv[1:])


def main():
    if has_arguments():
        txt_print = ""
        nums_file = count_arguments()
        for x in range(1, nums_file+1):
            fname = sys.argv[x]
            fopen = open(fname, "r")
            txt_print += fopen.read()
            txt_print += "\n"
            fopen.close()
        print(txt_print)
    else:
        print("There are no arguments")

if __name__ == '__main__':
    main()
