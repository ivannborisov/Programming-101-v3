import os
import sys


def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            try:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
            except:
                pass
    return total_size


def bytes_to_gb(b):
    return b / (10 ** 9)


def main():
    path = sys.argv[1]
    print(path + " size is: " + str(bytes_to_gb(get_size(path))) + " GB")

if __name__ == '__main__':
    main()
