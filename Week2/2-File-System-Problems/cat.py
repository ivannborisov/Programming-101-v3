# cat.py
import sys


def has_arguments(count=1):
    return len(sys.argv[1:]) >= count


def main():
    filename = sys.argv[1]
    first_file = open(filename, "r")
    print(first_file.read())

if __name__ == '__main__':
    main()
