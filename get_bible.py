import docx
import re

def get_doc_text(filename):
    '''
    Gets text from Word doc filename using the docx package
    Returns:    chapter_text = string of contents 
                len of chapter_text

    Appends each para to a list since this is how to interate over file using the docx package.
    But we want a string so ... returns string converted from list and replaces /n with a space

    There is also commented out functionality to return every verse if needed later. Could be moved
    to a seperate function
    '''

    doc = docx.Document(filename)
    chapter_paragraphs = []

    # Append to a list
    for para in doc.paragraphs:
        chapter_paragraphs.append(para.text)
        
    # Then convert back to a string
    chapter_text = ' '.join(chapter_paragraphs)
    return chapter_text
    
def get_chapter_num(chapter):
    chapter_num_with_colon = re.findall(r'\d+:|$', chapter)[0]
    chapter_num = chapter_num_with_colon[:-1]
    return int(chapter_num)

def get_num_of_verses(chapter):
    num_of_verses_with_colon = re.findall(r':\d+', chapter)[-1]
    num_of_verses = num_of_verses_with_colon[1:]
    return int(num_of_verses)

def get_all_verses(filepath,book_name):
    '''
    Uses re module find the search term and adds the verses with that term
    to a dictionary. The dictionaries are then appended to a list that is returned
                 
    Hint:   \d = any digit
            + = one or more of previous character

    '''    
    chapter = get_doc_text(filepath) # get the chapter text as a string

    pattern = re.compile(r'\d+:\d+') 
    matches = pattern.finditer(chapter)
    
    verses_with_search_term = []
    all_verses = [] 
    references = []
    current_verse = {}
    chars_in_chapter=len(chapter)
    chapter_num = get_chapter_num(chapter)
    num_of_verses=get_num_of_verses(chapter)

    # all_verses = [dict() for number in range(num_of_verses)]

    for index, match in enumerate(matches, 0): 
        # Interate over matches, leave index at default of 0

        chapter_num=get_chapter_num(chapter)
        num_of_verses = get_num_of_verses(chapter)

        references.append((match.start(), match.end()))
        # .start and .end methods get indice where search term starts and where it ends
        
        # print (f'Index is: {index} - Reference is: {references}')

        if index == 0:
            # skip first reference pair since will start with 2nd pair
            continue
        
        elif index + 1 == num_of_verses:  
            # if processing last tuple then text indices will be from the 2nd number
            # of the previous tuple (hence [index-1]) to the end of the string '''

            start = 1 + references[index-1][1]
            # Add 1 to get rid of initial space after verse number

            verse_text = chapter[start:chars_in_chapter]
            # Using chapter_length passed to function to get index of last char in string
        
        else:
            start = 1 + references[index-1][1]
            # the text is found in the 2nd number [1] in the previous pair thus Index-1[1]
            # Add 1 to get rid of initial space after verse number
            
            end = references[index][0] 
            # ends with the 1st number [0] in the current pair
            
            verse_text = chapter[start:end]
            
        current_verse["book_name"] = book_name
        current_verse["chapter_num"] = chapter_num
        current_verse["verse_num"] = index 
        current_verse["verse_text"] = verse_text

        current_verse_copy = current_verse.copy() 
        all_verses.append(current_verse_copy) 
  
            
    return all_verses
 
