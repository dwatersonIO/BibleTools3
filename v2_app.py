""" Accepts full path to Book name such as:
    C:/Coding/BibleTools3/Hebrew Scriptures/02-Exodus/Exodus 01.docx

    Returns a dictionary of the chapter in the format:
    {book_name: "Exodus", chapter_num: 2, verse_num: 1, verse_text: "text of verse"}

    Gets text from Word doc filename using the docx package
    Returns:    chapter_text = string of contents
                len of chapter_text

    Appends each para to a list since this is how to interate over file using the docx package.
    But we want a string so ... returns string converted from list and replaces /n with a space

    TO DO

    1. When making the dict with all data need to add book name key somehow

"""
import json
import re
import docx
import time



BASE_PATH='/home/david/Coding/BibleTools3/Hebrew Scriptures'

BIBLE_BOOKS2 = {
    "Genesis": {"book_num": 1, "num_of_chaps": 50 },
    "Exodus" : {"book_num": 2, "num_of_chaps": 40},
    "Leviticus" : {"book_num": 3, "num_of_chaps": 27},
    "Numbers": {"book_num": 4, "num_of_chaps": 36},
    "Deuteronomy": {"book_num": 5, "num_of_chaps": 34},
    "Joshua": {"book_num": 6, "num_of_chaps": 24},
    "Judges": {"book_num": 7, "num_of_chaps": 21},
    "Ruth": {"book_num": 8, "num_of_chaps": 4},
    "1 Samuel": {"book_num": 9, "num_of_chaps": 31},
    "2 Samuel": {"book_num": 10, "num_of_chaps": 24},
    "1 Kings": {"book_num": 11, "num_of_chaps": 22},
    "2 Kings": {"book_num": 12, "num_of_chaps": 25},
    "1 Chronicles": {"book_num": 13, "num_of_chaps": 29},
    "2 Chronicles": {"book_num": 14, "num_of_chaps": 36},
    "Ezra": {"book_num": 15, "num_of_chaps": 10},
    "Nehemiah": {"book_num": 16, "num_of_chaps": 13},
    "Esther": {"book_num": 17, "num_of_chaps": 10},
    "Job": {"book_num": 18, "num_of_chaps": 42},
    "Psalms": {"book_num": 19, "num_of_chaps": 150},
    "Proverbs": {"book_num": 20, "num_of_chaps": 31},
    "Ecclesiastes": {"book_num": 21,"num_of_chaps": 12},
    "Song of Solomon": {"book_num": 22, "num_of_chaps": 8},
    "Isaiah": {"book_num": 23, "num_of_chaps": 66}, 
    "Jeremiah": {"book_num": 24, "num_of_chaps": 52},
    "Lamentations": {"book_num": 25, "num_of_chaps": 5},
    "Ezekiel": {"book_num": 26, "num_of_chaps": 48},
    "Daniel": {"book_num": 27, "num_of_chaps": 12},
    "Hosea": {"book_num": 28, "num_of_chaps": 14},
    "Joel": {"book_num": 29, "num_of_chaps": 3},
    "Amos": {"book_num": 30, "num_of_chaps": 9},
    "Obadiah": {"book_num": 31, "num_of_chaps": 1},
    "Jonah": {"book_num": 32, "num_of_chaps": 4},
    "Micah": {"book_num": 33, "num_of_chaps": 7}, 
    "Nahum": {"book_num": 34, "num_of_chaps": 3},
    "Habakkuk": {"book_num": 35, "num_of_chaps": 3},
    "Zephaniah": {"book_num": 36, "num_of_chaps": 3},
    "Haggai": {"book_num": 37, "num_of_chaps": 2},
    "Zechariah": {"book_num": 38, "num_of_chaps": 14},
    "Malachi": {"book_num": 39, "num_of_chaps": 4}
}

# for book in BIBLE_BOOKS2:
#     print (book, BIBLE_BOOKS2[book]["book_dir_name"])

# bk = "Genesis"

# print (BIBLE_BOOKS2[bk]["book_dir_name"])

# print ("Exodus" in BIBLE_BOOKS2)


def get_list_of_chapters(book_to_process: str) -> list:
    """
    accapts Bible book name:
    returns a list of chapters incl full path for that book
    
    """
    
    chaps_to_process = []

    for chapter in range(1, BIBLE_BOOKS2[book_to_process]['num_of_chaps'] + 1):  # Start: from 1, Stop: add 1 since Range not includng last number

        chap_num_str = str(chapter).zfill(2)  # eg 02. Int converted to str  padded out to 2 digits
        book_num_str = str(BIBLE_BOOKS2[book_to_process]['book_num']).zfill(2)

        book_dir_name = f"{book_num_str}-{book_to_process}"

        if book_to_process == "Psalms":
            chap_num_str = str(chapter).zfill(3)  # eg 002. Psalms has more than 99 "chapters" so pad out to 3 digits

        chapter_path = f"{BASE_PATH}/{book_dir_name}/{book_to_process} {chap_num_str}.docx"
        chaps_to_process.append(chapter_path) 
    
    return chaps_to_process    

        
def convert_word_doc(chapter_path: str) -> str: 
    """
    takes a Word docx of a Bible book chapter incl path
    returns chapter as a string
    """
    doc = docx.Document(chapter_path)
    chapter_paragraphs = []

    for _, para in enumerate(doc.paragraphs, 1):
        chapter_paragraphs.append(para.text)  # append to list
        raw_chapter_text = " ".join(chapter_paragraphs)  # Convert back to a string
        chapter_text = raw_chapter_text
    return chapter_text


def make_list_of_dicts_for_book(book_contents: str, book_name: str) -> list:
    """
    Takes a book as str and return a dictionary. 
    Use the regex group keyword to split the chapter, verse and verse text
    """

    pattern = re.compile(r"(\d+:\d+)(.+?)(?=\d+:\d+|$)")
    matches = pattern.finditer(book_contents)
    chapter_dict = [
        {
            "book_name": book_name,
            "chapter_num": int(m.group(1).split(":")[0]),
            "verse_num": int(m.group(1).split(":")[1]),
            "verse_text": m.group(2).strip(),
            "num_words_in_verse": len(m.group(2).split()),  
        }
        for m in matches
    ]

    return chapter_dict

    # for match in matches:
    #     print(match.group(1), match.group(2))


def get_book_content(chapters_in_book):
    book_contents =''
    for chapter in chapters_in_book: # iterate over list of chapters
        book_contents += convert_word_doc(chapter)
    return book_contents

def make_bible_list_of_dicts(list_of_books: list) -> list:
    progressive_list_of_dicts =[]
    temp_list=[]

    for book in list_of_books:
        chapters_in_book=get_list_of_chapters(book)
      
        book_content =  get_book_content(chapters_in_book)
   
        temp_list = make_list_of_dicts_for_book(book_content, book)
        progressive_list_of_dicts += temp_list

    return progressive_list_of_dicts


def save_bible_as_json(result):
    with open("/home/david/Coding/BibleTools3/result.txt", "w", encoding="utf8") as f:
        json.dump(result, f, ensure_ascii=False)

def doit():
    start_time = time.time()
    keys = list(BIBLE_BOOKS2.keys())
    
    result=make_bible_list_of_dicts(keys)
    save_bible_as_json(result)

    end_time = time.time()

    total_time = end_time - start_time
    print("Time taken:", total_time, "seconds")


doit()


# pprint.pprint(result)

