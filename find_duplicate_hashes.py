import pathlib
from FileHasher import FileHasher

SKIP_DIRS = ["temp", "temporary_files", "logs", ".idea", ".venv"]


def find_duplicates_files(root):
    generator = get_all_items(root)
    hashes_dict = get_hashes_as_dict(generator)
    return exchange_key_and_value(hashes_dict)


def get_all_items(root: pathlib.Path):
    for item in root.iterdir():
        if item.name in SKIP_DIRS:
            continue
        if item.is_dir():
            yield from get_all_items(item)
        else:
            hasher = FileHasher(item)
            yield item, hasher.hash_file()


def get_hashes_as_dict(generator):
    hashes_dict = {}
    for iterable in generator:
        key = iterable[0]
        value = iterable[1]
        hashes_dict[key] = value
    return hashes_dict


def exchange_key_and_value(hashes_dict):
    key_value_exchanged = {}
    for key, value in hashes_dict.items():
        if value not in key_value_exchanged:
            key_value_exchanged[value] = [key]
        else:
            key_value_exchanged[value].append(key)
    return key_value_exchanged
