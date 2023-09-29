""" 

"""
import json
import pickle
import re
import docx
import time
import pprint 
from constants import BIBLE_BOOKS, BASE_PATH_WINDOWS


def get_list_of_chapters(book_to_process: str) -> list:
    """
    accepts a list of paths to chapter files in that book
    
    """
    
    chaps_to_process = []

    for chapter in range(1, BIBLE_BOOKS[book_to_process]['num_of_chaps'] + 1):  # Start: from 1, Stop: add 1 since Range not includng last number

        chap_num_str = str(chapter).zfill(2)  # eg 02. Int converted to str  padded out to 2 digits
        
        book_num_str = str(BIBLE_BOOKS[book_to_process]['book_num']).zfill(2) # eg 02 Pad out chap num to two digits and make it a str
        if book_to_process == "Psalms":
            chap_num_str = str(chapter).zfill(3)  # eg 002. Psalms has more than 99 "chapters" so pad out to 3 digits

        book_dir_name = f"{book_num_str}-{book_to_process}"

        chapter_path = f"{BASE_PATH_WINDOWS}\{book_dir_name}\{book_to_process} {chap_num_str}.docx"
        chaps_to_process.append(chapter_path) 
    
    
    return chaps_to_process    

        
def convert_word_doc(chapter_path: str) -> str: 
    """
    Accepts a path to a Bible book chapter Word docx 
    Returns chapter contents as a string
    """
    doc = docx.Document(chapter_path)
    chapter_paragraphs = []

    for _, para in enumerate(doc.paragraphs, 1):
        chapter_paragraphs.append(para.text)  # append to list
        raw_chapter_text = " ".join(chapter_paragraphs)  # Convert back to a string
        chapter_text = raw_chapter_text
    return chapter_text


def get_book_content(chapters_in_book: list) -> str:  
    """
    Interates over list of chapters in a book and appends to book_contents str
    """

    book_contents =''
    for chapter in chapters_in_book: # iterate over list of chapters
        book_contents += convert_word_doc(chapter)
    return book_contents


def make_list_of_dicts_for_book(book_contents: str, book_name: str) -> list:
    """
    Accepts book contents as str and return a dictionary of book contents. 
    Uses the regex group keyword to split the chapter, verse and verse text
    """

    pattern = re.compile(r"(\d+:\d+)(.+?)(?=\d+:\d+|$)")
    matches = pattern.finditer(book_contents)
    chapter_dict = [
        {
            "book_name": book_name,
            "chapter_num": int(m.group(1).split(":")[0]),
            "verse_num": int(m.group(1).split(":")[1]),
            "verse_text": m.group(2).strip(), # strip off extra spaces at both ends of verse            
        }
        for m in matches
    ]
    return chapter_dict

def make_bible_list_of_dicts(list_of_books: list) -> list:
    """
    Accepts list of Bible books and returns list of a dicts with keys:
    book_name, chapter_num, verse_num, verse_text
    """
    
    cummulative_list_of_dicts =[]

    for book in list_of_books:
        chapters_in_book=get_list_of_chapters(book)
      
        book_content =  get_book_content(chapters_in_book)
   
        cummulative_list_of_dicts += make_list_of_dicts_for_book(book_content, book)

    bible_list_of_dicts = cummulative_list_of_dicts # dict now contains all Bible books

    return bible_list_of_dicts


def save_bible_as_json(result):
    with open("result.txt", "w", encoding="utf8") as f:
        json.dump(result, f, ensure_ascii=False)


def pickle_bible(result):
    with open("result.pickle", "wb") as f:
        pickle.dump(result, f)
        


def make_bible_object():
    start_time = time.time()
    books_to_get = list(BIBLE_BOOKS.keys())  
    
    result=make_bible_list_of_dicts(books_to_get[:5])  # change number to determine how many books are processed

    # save_bible_as_json(result)
    pickle_bible(result)

    end_time = time.time()

    total_time = end_time - start_time
    print("Time taken:", total_time, "seconds")
    

# doit()

def search_bible(search_text):
    with open("result.pickle","rb") as f:
        result = pickle.load(f)
    
    # print (result)

    for chapter in result:
           if search_text in chapter['verse_text']: 
            print (f"{chapter['book_name']} {chapter['chapter_num']}:{chapter['verse_num']} {chapter['verse_text']}")
            
search_bible("Adam")

# pprint.pprint(result)

