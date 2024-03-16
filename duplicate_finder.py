import pathlib
import sys
from find_duplicate_hashes import find_duplicates_files


def main():
    directory = pathlib.Path(sys.argv[1])
    duplicates_dictionary = find_duplicates_files(directory)
    print_duplicates(duplicates_dictionary)


def print_duplicates(dict):
    for item in dict:
        if len(dict[item]) > 1:
            print(f"\nHash {item} is duplicated in these files: ", *dict[item], sep="\n")


if __name__ == "__main__":
    main()
