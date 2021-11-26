import docx
import re

def get_doc_text(filename):
    '''
    Gets text from Word doc filename using the docx package
    Returns:    chapter_text = string of contents 
                len of chapter_text

    Appends each para to a list since this is how to interate over file using the docx package.
    But we want a string so ... returns string converted from list and replaces /n with a space
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
    # pattern = re.compile(r'\d:') 
    chapter_num_with_colon = re.findall(r'\d+:|$', chapter)[0]
    chapter_num = chapter_num_with_colon[:-1]
    return int(chapter_num)

def get_num_of_verses(chapter):
    # pattern = re.compile(r'\d:') 
    num_of_verses_with_colon = re.findall(r':\d+', chapter)[-1]
    num_of_verses = num_of_verses_with_colon[1:]
    return int(num_of_verses)

def build_dict(chapter):
    '''
    Uses re module to find the indices of chapter verse numbers (eg. 1:1, 1:2 ...) 
    and appends them to a list of tuples called chap_verse_indices
                 
    Hint:   \d = any digit
            + = one or more of previous character

    '''    
    pattern = re.compile(r'\d+:\d+') 
    matches = pattern.finditer(chapter)

    found = []
    references = []
    result = []
    current_verse = {}
    chars_in_chapter=len(chapter)
    chapter_num = get_chapter_num(chapter)
    num_of_verses=get_num_of_verses(chapter)

    # result = [dict() for number in range(num_of_verses)]

    for index, match in enumerate(matches, 0): 
        # Interated over matches
        # Don't need to use enumerate but useful in case need index later on for testing
        # last parameter starts index 1 instead of default of 0

        chapter_num=get_chapter_num(chapter)
        num_of_verses = get_num_of_verses(chapter)

        references.append((match.start(), match.end()))
        # .start and .end methods get indice where search term starts and where if ends
        
        # print (f'Index is: {index} - Reference is: {references}')

        if index == 0:
            # skip first reference pair since will start with 2nd pair
            continue
        
        elif index + 1 == num_of_verses:  
            # if processing last tuple then text indices will be from he 2nd number
            # the previous tuple (hence [index-1]) to the end of the string '''

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
            
        current_verse["book_name"] = "Exodus"
        current_verse["chapter_num"] = chapter_num
        current_verse["verse_num"] = index 
        current_verse["verse_text"] = verse_text

        current_verse_copy = current_verse.copy()
        result.append(current_verse_copy)

        search_word_pattern = re.compile(r'tiegħek')
        search_matches = search_word_pattern.findall(verse_text)
        
        if search_matches:
            found_verse = current_verse.copy()
            found.append(found_verse)

            
    print (found)
    
    # a = next(item for item in result if item ["verse_num"] == 2)
    
    return result


'''
******************************************************
                TESTING FUNCTIONS
******************************************************
''' 

def test_chapter_functions():
    '''
    ************************************************************************
    Will print out the string of Exodus 2 and then number of chars in string
    ************************************************************************
    '''

    filename = r'C:\Users\dwate\OneDrive\Coding\BibleTools2\Hebrew Scriptures\02-Exodus\Exodus 20.docx'
    chapter = get_doc_text(filename) 
    
    build_dict(chapter)

test_chapter_functions()
