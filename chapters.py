import docx
import re

''' Accepts full path to Book name such as:
    C:/Coding/BibleTools3/Hebrew Scriptures/02-Exodus/Exodus 01.docx

    Returns a dictionary of the chapter in the format:
    {book_name: "Exodus", chapter_num: 2, verse_num: 1, verse_text: "text of verse"}

    Gets text from Word doc filename using the docx package
    Returns:    chapter_text = string of contents 
                len of chapter_text

    Appends each para to a list since this is how to interate over file using the docx package.
    But we want a string so ... returns string converted from list and replaces /n with a space

    '''

def extract_chapter(chapter: str, chapter_num: int):
    doc = docx.Document(chapter)
    chapter_paragraphs = []

    for _, para in enumerate(doc.paragraphs, 1): 
        
        chapter_paragraphs.append(para.text) # append to list
        raw_chapter_text = ' '.join(chapter_paragraphs) # Convert back to a string
        
        chapter_text = raw_chapter_text
        if chapter_num == 1:
            # if chap 1 get rid of Bible book name from start of string
            chapter_text = ' '.join(raw_chapter_text.split()[1:])
  
    return chapter_text

def count_verses(chapter_text):
    '''Returns number of verses by searching colon'''

    num_of_verses_with_colon = re.findall(r':\d+',chapter_text)[-1]

    return int(num_of_verses_with_colon[1:]) # delete colon and returned as str so need int

def get_chapter_dict(chapter_path, book_name, chapter_num, book_dict):
    
    chapter_text = extract_chapter(chapter_path, chapter_num)
    number_of_verses = count_verses(chapter_text)

    match_pairs = []
    result = [] # {}

    pattern = re.compile(r'\d+:\d+') 
    matches = pattern.finditer(chapter_text)

    for match in matches:
        match_pairs.append((match.start(), match.end()))
        
    for index, _ in enumerate(match_pairs, 0): 

        # Check if this is the last chapter/verse pair in the list
        if index == number_of_verses - 1:   
            start = 1 + match_pairs[index][1] 
            # Add 1 to get rid of initial space after verse number

            end = len(chapter_text) # since the last pair, the end of text will be the end of the chapter
            verse_text = chapter_text[start:end]

        else:
            # This runs for all chapter/verse pairs if not last one 
            start = 1 + match_pairs[index][1]
            # Add 1 to get rid of initial space after verse number
            end = match_pairs[index + 1][0]
            verse_text =chapter_text[start:end]
            

        book_dict["book_name"] = book_name
        book_dict["chapter_num"] = chapter_num
        book_dict["verse_num"] = index + 1 # verse numbers don't start from zero like indices
        book_dict["verse_text"] = verse_text

        # copy_chapter_dict = chapter_dict.copy()
        # result |= copy_chapter_dict
    
    return book_dict

       
def test():

    # Testing
    # get_chapter_as_dict(filename, BOOK_NAME, CHAPTER_NUMBER):

    filename = "C:/Coding/BibleTools3/Hebrew Scriptures/02-Exodus/Exodus 01.docx"
    BOOK_NAME="Exodus"
    CHAPTER_NUMBER=1

    result = chapter_dict(filename, BOOK_NAME, CHAPTER_NUMBER)
    print (result)

# test()