from collections import Counter
from typing import List


def get_most_freq_words(words: List[str]):
    """Returns most frequent words in collections"""
    words_counter = Counter(words)
    max_qty = max(words_counter.values())
    most_freq_words = [word for word, qty in words_counter.items() if qty == max_qty]
    qty_words = {word: max_qty for word in most_freq_words}
    return qty_words
