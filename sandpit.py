import os
import re

  # Use code below if want to search occurances of particular string
   # This was when thought would search in chapter as a string but better 
   # to search when a dictionary.
   
    # count = 0
    # for m in matches:
    #     if "Ġeħova" in m.group(2):
    #         print (m.group(1), m.group(2))
    #         count += 1
    # print (count)

    # result = ""
#
#  for chapter in all_chapters:
#     result += extract_chapter(
#         "/home/david/Coding/BibleTools3/Hebrew Scriptures/02-Exodus/" + chapter
#     )

# with open("/home/david/Coding/BibleTools3/exodus.txt", "w", encoding="utf8") as file:
#     file.write(result)

# for a in get_chapter_dict(result):
#     for b in a:
#         print(b, "->", a[b])


import itertools
from collections import Counter

list_of_dict = [{"book_name": "Genesis", "chapter_num": 1, "verse_num": 1, "verse_text": "In the beginning God created the heavens and the earth."}, {"book_name": "Genesis", "chapter_num": 1, "verse_num": 2, "verse_text": "Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters."}]

import itertools
from collections import Counter


# group the dictionaries by their book_name using itertools.groupby()
groups = itertools.groupby(list_of_dict, lambda dict: dict["book_name"])

# for each group, count the words in the "verse_text" field and print the total
for book_name, group in groups:
    words_iterable = itertools.chain.from_iterable(dict["verse_text"].split() for dict in group)
    word_count = Counter(words_iterable)
    total_words = sum(word_count.values())
    print(f"{book_name}: {total_words} words")