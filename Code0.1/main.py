import sys
import os


def main():
    file_name: str = str(sys.argv[1])
    print(file_name)
    if os.path.exists(file_name):
        print("exists")
        with open(file_name, "r") as f:
            print(f.readlines())
    else:
        print("error no such file")
    input()


if __name__ == '__main__':
    main()
