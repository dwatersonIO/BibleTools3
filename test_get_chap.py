
# setup path to Bible book and 

import os
import re
# from search_bible import get_search_term_verses
from get_bible import get_all_verses
from file_functions import get_chapter_list

file_path = "C:/Coding/BibleTools3/Hebrew Scriptures/02-Exodus"

book_chapters = get_chapter_list(file_path)
''' book_chapters is a list of all the Word docx chapters in that
    bible book directory. So eg Genesis will have 50 entries ''' 
    
   
for chapter in book_chapters:
    ''' interate over each chapter ''' 
    
    name_chapter = re.findall(r'\w+', chapter)
    ''' Breaks current chapter file name into list like this: ['Exodus', '01', 'docx']
        Will then use this list below to identify book name and current chapter number '''
        
    chapter_path = os.path.join(file_path, chapter) # add on chapter file to the path

    # filepath = r'C:\Users\dwate\OneDrive\Coding\BibleTools-Flask\Hebrew Scriptures\02-Exodus\Exodus 06.docx'

    nwt = get_all_verses(chapter_path, name_chapter[0])


print (nwt)