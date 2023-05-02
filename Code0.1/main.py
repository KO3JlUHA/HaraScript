import sys
import os


def read_file(file_name: str) -> None:
    with open(file_name, "r") as f:
        print(f.readlines())


def file_exists(file_name: str) -> bool:
    return os.path.exists(file_name) and file_name.endswith(".phe")


def main():
    file_name: str = str(sys.argv[1])
    if file_exists(file_name=file_name):
        read_file(file_name=file_name)
    input()


if __name__ == '__main__':
    main()
