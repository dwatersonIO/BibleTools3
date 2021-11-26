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
    return chapter_text, len(chapter_text)
    

def get_chap_verse_indices(chapter):
    '''
    Uses re module to find the indices of chapter verse numbers (eg. 1:1, 1:2 ...) 
    and appends them to a list of tuples called chap_verse_indices
                 
    Hint:   \d = any digit
            + = one or more of previous character

    '''    
    pattern = re.compile(r'\d+:\d+') 
    matches = pattern.finditer(chapter)

    chap_verse_indices = []
    for _, match in enumerate(matches, 1): 
        # Don't need to use enumerate but useful in case need index later on for testing
        # last parameter starts index 1 instead of default of 0

        chap_verse_indices.append((match.start(), match.end()))
        # .start and .end methods get indice where search term starts and where if ends
    
    return chap_verse_indices  




def get_text_indices(chap_verse_indices, chapter_length):
    '''
    Appends the start and end indices of actual verse text to new list
    of tuples called text_indices which is then returned 
    As parameter takes CHAP_VERSE_INDICES list and CHAPTER_LENGTH integer
    (origina    l string from docx)

    '''
    text_indices=[]
    for index, _ in enumerate(chap_verse_indices, 1):
        # Uses enumerate to iterate over tuples in chap_verse_indices
        # Dont need to use enumerate but useful in case later want to use
        # index for some reason
        # last parameter starts index 1 instead of default of 0

        number_of_verses = len(chap_verse_indices)
        if index == number_of_verses: 
            # if processing last tuple then text indices will be from he 2nd number
            # the previous tuple (hence [index-1]) to the end of the string '''

            start = 1 + chap_verse_indices[index-1][1]
            # Add 1 to get rid of initial space after verse number

            text_indices.append((start, chapter_length))
            # Using chapter_length passed to function to get index of last char in string
        
        else:
            start = 1 + chap_verse_indices[index-1][1]
            # the text is found in the 2nd number [1] in the previous pair thus Index-1[1]
            # Add 1 to get rid of initial space after verse number
            
            end = chap_verse_indices[index][0] 
            # ends with the 1st number [0] in the current pair
            
            text_indices.append((start, end))

    return text_indices


def get_verse_text(text_indices, chapter):
    '''
    Takes the list of tuples called text_indices and returns
    the actual verse text between those two indices. Appends
    to a new list called verse_text
    
    '''
    verse_text = []
    for _, indices in enumerate(text_indices, 1):
        # Uses enumerate to iterate over text_indices pairs
        # Don't need to use enumerate here but useful in case later on 
        # need the index for testing
        # last parameter starts index 1 instead of default of 0

        start = indices[0]
        end = indices[1]
        verse_text.append(chapter[start:end])
    return verse_text

''' Get verse_text in a list  
NOT NEEDED NOW BUT MAY BE USEFUL LATER 
get_verse_text(text_indices, chapter) '''

def find_indices(chapter):
    '''
    Looks for a search term 'Alla' and returns the 
    start index of the search results
    
    '''

    search_term_indices=[]

    pattern = re.compile(r'Alla')
    matches = pattern.finditer(chapter)

    for _, match in enumerate(matches, 1):
        # Uses enumerate to iterate over text_indices pairs
        # span() returns the first and last index of search term
        # as a list of tuples
        search_term_indices.append(match.span())
    
    return search_term_indices




def search_results(filename):
    '''
    ****************************************************************************
    Will run functions above and return a dictionary
    containing chapter number: occurances of all hits in that chapter
    ****************************************************************************

    '''
    chapter, chapter_length = get_doc_text(filename)
    # Unpack:
    #   chapter: which is the chapter text as a string 
    #   chapter_length: which is number of chars in that chapter string
    
    chap_verse_indices = get_chap_verse_indices(chapter)
    # Get chap_verse_indices in a list

    text_indices = get_text_indices(chap_verse_indices, chapter_length)
    # Get text_indices in a list 
    
    search_indices = find_indices(chapter)
    # Get indices of search term Alla 

    found = {}
    for verse_number, text_index in enumerate(text_indices, 1):
        for _, search_term_index in enumerate(search_indices, 0):
            
            start, last = text_index
            # Unpack two indices in the current text index '''
            
            if search_term_index > last:
                # If the current index of search term is greater than the 2nd (last) number in 
                # the current text_index pair (last) then move on since no more occurances in this verse
                 
                continue 
            
            if search_term_index >= start and search_term_index <= last:
                ''' use get method to see if this is the first occurance or not 
                then add 1 to it '''
                found[verse_number] = found.get(verse_number, 0) + 1
                
                
    return found


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
    chapter, chapter_length = get_doc_text(filename) 
    
    # Uncomment below to test get_doc_text
    
    # print (chapter)
    # print ()
    # print (chapter_length)
    
    '''
    ************************************************************************
    Will print out the sist chap_verse_indices of Exodus 02
    ************************************************************************
    '''
    chap_verse_indices = get_chap_verse_indices(chapter)

    # Uncomment below to test
    
    # print ("Chapter Verse Indices are:")
    # print ()
    # print (chap_verse_indices)


    '''
    ************************************************************************
    Will print out the list text_indices of Exodus 02
    ************************************************************************
    '''
    text_indices = get_text_indices(chap_verse_indices, chapter_length)

    # Uncomment below to test get_text_indices
    
    print ("Text Indices are:")
    print ()
    print (text_indices)


    '''
    ************************************************************************
    Will print out the verse text of sample chapter
    ************************************************************************
    '''
    verse_text = get_verse_text(text_indices, chapter)

    # Uncomment below to test get_verse_text
    
    print ()  
    print ("Verse Text is: ")
    print ()  
    print (verse_text)


    '''
    ************************************************************************
    Will print out the context of the search term hits find_indices 
    ************************************************************************
    '''
    index_of_hits = find_indices(chapter)

    # Uncomment below to test get_verse_text
    
    # def get_context_start(chapter):
    #     for a in range (30, 50):
    #         context_start = index[0]-a
    #         if chapter[context_start] == " ":
    #             return context_start
    
    # def get_context_end(chapter):
    #     for a in range (20, 40):
    #         context_end = index[0]+a
    #         if chapter[context_end] == " ":
    #             return context_end
    
    # for _, index in enumerate(index_of_hits, 0):
        
    #     context_start = get_context_start(chapter)
    #     context_end = get_context_end(chapter)

    #     print (chapter[context_start:index[0]])
    #     print (chapter[index[0]:index[1]])
    #     print (chapter[index[1]:context_end])
    #     print ()



test_chapter_functions()


    