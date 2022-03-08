'''
TO DO 

0. Make github repo for this project.
1. Separate main code so loops are not nested but simplier to read
2. need to append to the nwt dictionary each time.
3. Check thisç Bug where last verse is being included with 2nd to last verse.
    
'''

import time
import os
import re

# from search_bible import get_search_term_verses
from get_chapter import get_chapter_as_dict
from utils import get_list_of_chapters
from utils import get_list_of_bible_books


t0 = time.time()

BOOKS_FOLDER='C:/Coding/BibleTools3'

base_path, bible_books_list = get_list_of_bible_books(BOOKS_FOLDER)


for book in bible_books_list:
    ''' Interate over the bible book folder names list  ''' 

    file_path = os.path.join(base_path, book)
    ''' File_path now set to:
        C:/Users/dwate/OneDrive/Coding/BibleTools2/Hebrew Scriptures/Exodus 02
        on first iteration '''

    book_chapters_list = get_list_of_chapters(file_path)
    ''' book_chapters is a list of all the Word docx chapters in that
        bible book directory. So eg Genesis will have 50 entries ''' 
    
    for chapter in book_chapters_list:
        ''' interate over each chapter ''' 

        chapter_filename = re.findall(r'\w+', chapter)
        ''' Breaks current chapter file name into list like this: ['Exodus', '01', 'docx']
            Will then us    e this list below to identify book name and current chapter number '''

        chapter_path = os.path.join(file_path, chapter) # add on chapter file to the path

        # filepath = r'C:\Users\dwate\OneDrive\Coding\BibleTools-Flask\Hebrew Scriptures\02-Exodus\Exodus 06.docx'
        
        b = chapter_filename[0]
        c = int(chapter_filename[1])
        
        print (f"Getting book: {b} and chapter: {c} and making dictionary")

        nwt = get_chapter_as_dict(chapter_path, b, c)
        print (nwt)

        # for v in nwt:
        #     print (v["book_name"], v["chapter_num"], v["verse_num"], v["verse_text"])


t1 = time.time()

print (t1-t0)

