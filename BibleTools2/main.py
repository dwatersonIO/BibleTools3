'''
1. Read each chapter into a string - DONE
2. Get indices of search word occurances in string- DONE
3. Find indexes of verse text- DONE
4. Interate over the matches found in step 2 and return the chapter/verse number of the occurance DONE
5. Parse the files in the HS and GS directorys, skipping files that do not want to use DONE
6. Write Test functions to be able to text Chapter.py functions separately DONE
7. Write function to output context of search result DONE

TO DO
8. Write function, is_number_a reference to check if anumber is part of a chapter:verse combination
9. Write function to output search term and context to beginning of verse. 


10. Consider makeing functions OOP????


'''

import time
import os
import re
# from chapters import search_results
from file_functions import get_chapter_list

t0 = time.time()

os.chdir('C:/Users/dwate/OneDrive/Coding/BibleTools2')

base_path = os.path.join(os.getcwd(),'Hebrew Scriptures') # add HB Scriptures
''' base_path now C:/Users/dwate/OneDrive/Coding/BibleTools2/Hebrew Scriptures
'''

bible_books = os.listdir(base_path) # where bible book folders live
'''This wille be a list with the Bible book folder names it in 
    eg. ['01-Genesis''02-Exodus']'''

for book in bible_books:
    ''' Interate over the bible book folder names list  ''' 

    file_path = os.path.join(base_path, book)
    '''
    file_path now set to 
    FC:/Users/dwate/OneDrive/Coding/BibleTools2/Hebrew Scriptures/Exodus 02
    on first iteration
    '''

    book_chapters = get_chapter_list(file_path)
    # print (book_chapters)
    ''' book_chapters is a list of all the Word docx chapters in that
    bible book directory. So eg Genesis will have 50 entries''' 
    
    freq_in_book = 0 # used to count total occurances in book

    ''' interate over each chapter ''' 
    for chapter in book_chapters:
        
        name_chapter = re.findall(r'\w+', chapter)
        # Breaks current chapter file name into list like this: ['Exodus', '01', 'docx']
        # Will then use this list below to identify book name and current chapter number
           
        chapter_path = os.path.join(file_path, chapter) # add on chapter file to the path
        results = search_results(chapter_path) # pass the current file to the
        
        if bool(results) == False: # chk if dict empty = no occurances so next interation
            continue
        
        freq_in_chapter = sum(results.values()) # sum of values of dict. This Will be occuances in that chapter
        freq_in_book = freq_in_book + freq_in_chapter # add occurances for chapter to running total for book

        # print (name_chapter[0], name_chapter[1], 'Occurances in chapter-', freq_in_chapter, ' - ', results)
    
    print (f'Total occurances in {name_chapter[0]} = {freq_in_book}' )



t1 = time.time()

print (t1-t0)

 