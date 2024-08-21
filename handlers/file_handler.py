import re
from functools import lru_cache


@lru_cache(maxsize=200)
def exclude_words(word: str):
    """Check if word no in ban list"""
    ban_list = {'and', 'the', 'whom', 'this', 'for', 'with', 'from'}
    return word not in ban_list


@lru_cache(maxsize=200)
def normalize_rows(line: str):
    """Normalize rows from user txt file"""
    words = re.findall(r'\w{3,}', line)
    words_lower = map(str.lower, words)
    words_nums_filter = filter(str.isalpha, words_lower)
    words_without_ban = filter(exclude_words, words_nums_filter)
    words = list(words_without_ban)
    return words


def read_data_from_file(filename: str):
    """Read ata from txt file"""
    result = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line:
                normalize_line = normalize_rows(line)
                result.extend(normalize_line)
    return result
