import json
import itertools
from collections import Counter
from constants import BIBLE_BOOKS
import pprint


def read_json_bible(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf8") as f:
        list_of_verse_dicts = json.load(f)
    return list_of_verse_dicts


def add_total_verse_words(verses: dict, book_name: str) -> int: 
    total_words=0
    
    for verse in verses:
        if verse['book_name'] == book_name:
            total_words += len(verse['verse_text'].split()) # default split is on space so len with count words

    return total_words


verses_list_of_dicts = read_json_bible("/home/david/Coding/BibleTools3/result.txt")

books_to_get = list(BIBLE_BOOKS.keys())  # Not needed but will get the book names and put in list


# group the dictionaries by their book_name using itertools.groupby()
verses_grouped_by_book_name = itertools.groupby(verses_list_of_dicts, lambda dict: dict["book_name"])


for book_name, group in verses_grouped_by_book_name:
    print (f'Book: {book_name}, has total of verses:  {len(list(group))}')
    # for verse in group:
    #     print (verse)


verses_grouped_by_book_name = itertools.groupby(verses_list_of_dicts, lambda dict: dict["book_name"])
# for each group, count the words in the "verse_text" field and print the total
for book_name, group in verses_grouped_by_book_name:
    words_iterable = itertools.chain.from_iterable(dict["verse_text"].split() for dict in group)
    word_count = Counter(words_iterable)
    total_words = sum(word_count.values())

