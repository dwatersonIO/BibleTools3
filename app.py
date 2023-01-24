'''
TO DO 

1. DONE - Separate main code so loops are not nested but simplier to read
2. DONE - could be simpler Refactor chapters.py so simplier
2. DONE - need to append to the nwt dictionary each time. but list within list needs fixing 
3. Check this Bug where last verse is being included with 2nd to last verse.
    
'''

import time
import os
import re

# from search_bible import get_search_term_verses
from chapters import get_chapter_dict
from utils import get_list_of_chapters
from utils import get_list_of_bible_books

t0 = time.time()

BOOKS_FOLDER='C:/Coding/BibleTools3'

#  Later could use to iterate over all Bible books in dir
#  eg 
#       base_path, bible_books_list = get_list_of_bible_books(BOOKS_FOLDER)
#       for "book in bible_books_list:"
#  for now just use book variable

book = "02-Exodus"
base_path = "C:\Coding\BibleTools3\Hebrew Scriptures"

book_path = os.path.join(base_path, book)
''' book_path set to: C:/Users/dwate/OneDrive/Coding/BibleTools2/Hebrew Scriptures/02 Exodus
'''

list_of_chapters_in_book = get_list_of_chapters(book_path)
''' Get all the Word docx chapters in the bible book directory.''' 

complete_chapter = [] # Will return this 
partial_chapter = []
book_list = []
for chapter in list_of_chapters_in_book:

    chapter_path = os.path.join(book_path, chapter) # add on chapter file to the path

    book_and_chapter_list = re.findall(r'\w+', chapter)
    ''' Breaks current chapter file name into list like this: ['Exodus', '01', 'docx']
        Used to identify book name and current chapter number '''

    book_name = book_and_chapter_list[0]
    chapter_num = int(book_and_chapter_list[1])

    print (f"Getting book: {book_name} and chapter: {chapter_num} and making dictionary")

    chapter_list = get_chapter_dict(chapter_path, book_name, chapter_num, book_list)
    copy_chapter_list = chapter_list.copy()
    book_list.append(copy_chapter_list)
    # book_dict = book_dict | copy_partial_book 
    
    # complete_chapter.append(copy_partial_chapter)

print (book_list)

print (book_list[1])

    # for v in nwt:
    #     print (v["book_name"], v["chapter_num"], v["verse_num"], v["verse_text"])




t1 = time.time()

print (t1-t0)

