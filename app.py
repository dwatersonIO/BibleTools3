'''
TO DO 

1. Load all Bible books for inserted into DB but dont make nested FOR statements

Function to get Book,
Then calls function to get Chapters
Then insers

    
'''

import sqlite3

import time
import os
import re
# from search_bible import get_search_term_verses
from get_bible import get_all_verses
from file_functions import get_chapter_list


t0 = time.time()

conn = sqlite3.connect(':memory:')
c=conn.cursor()
c.execute("""CREATE TABLE verses (
        book_name text,
        chapter_num integer,
        verse_num integer,
        verse_text text
        )""")

conn.commit()

os.chdir('C:/Users/dwate/OneDrive/Coding/BibleTools3')

base_path = os.path.join(os.getcwd(),'Hebrew Scriptures') # add HB Scriptures
''' base_path now C:/Users/dwate/OneDrive/Coding/BibleTools2/Hebrew Scriptures
'''

bible_books = os.listdir(base_path) # where bible book folders live
'''This will be a list with the Bible book folder names it in 
eg. ['01-Genesis','02-Exodus']'''


for book in bible_books:
    ''' Interate over the bible book folder names list  ''' 

    file_path = os.path.join(base_path, book)
    ''' File_path now set to:
        C:/Users/dwate/OneDrive/Coding/BibleTools2/Hebrew Scriptures/Exodus 02
        on first iteration '''

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

        for v in nwt:
            c.execute("INSERT INTO verses VALUES (?,?,?,?)", (v["book_name"], v["chapter_num"], v["verse_num"], v["verse_text"]))
            conn.commit()

# c.execute("SELECT * FROM verses WHERE verse_text LIKE '%40%'")

c.execute("SELECT * FROM verses WHERE chapter_num = 2")
print(c.fetchall())

conn.close()
t1 = time.time()

print (t1-t0)

