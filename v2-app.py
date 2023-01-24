import docx, os, re

from pprint import pprint

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


def get_list_of_chapters(path):
    ''' Takes in the  path where the chapter files live eg: 'Hebrew Scriptures/02-Exodus'
    and returns a list called chapter_list that contains the files to process. This function makes sure that other files
    that are in bible book directory are not processed. For example Exodus 36.Advisor.docx and and temp files
    Funtion is commented out that allows making a backup of files
    
    Many of these commands explained in Corey Schafter YouTube video "Automate Parsing and renaming of multiple files"
    '''
    chapter_list = []
    # path should be like this: 'Hebrew Scriptures/02-Exodus'
    os.chdir (path)


    ''' Later on if want to backup files first then commpare
        can include these lines

    if not os.path.exists('backup'):
    os.mkdir ('backup') '''

    for f in os.listdir():
        
        f_name, f_ext = os.path.splitext(f) # separate file name from extension

        f_parts = f_name.split('.') # divide filename to list on period. eg will produce ['Exodus 01', 'Revised Text', 'Advisor']

        # print (f_parts[0][0])
        if len(f_parts) < 2 and f_parts[0][0] != "~" and f_parts[0] != "backup" and f_ext == '.docx': 
            # only want 1. list item with 1 item 2. No files starting with "~" and 3. Not the backup folder

            new_name = '{}{}'.format(f_parts[0], f_ext) # piece the file name together again
            chapter_list.append(new_name)  # append it to the list we want to eventually return

    return chapter_list

def extract_chapter(chapter_path: str):
    doc = docx.Document(chapter_path)
    chapter_paragraphs = []

    for index, para in enumerate(doc.paragraphs, 1): 
        
        chapter_paragraphs.append(para.text) # append to list

        raw_chapter_text = ' '.join(chapter_paragraphs) # Convert back to a string
        
        chapter_text = raw_chapter_text
  
    return chapter_text
    
def count_verses(chapter_text):
    '''Returns number of verses by searching colon'''

    num_of_verses_with_colon = re.findall(r':\d+',chapter_text)[-1]

    return int(num_of_verses_with_colon[1:]) # delete colon and returned as str so need int


def get_chapter_dict(file):
    
    pattern = re.compile(r"(\d+:\d+)(.+?)(?=\d+:\d+|$)")   
    matches = pattern.finditer(file)
    # result = [{"chapter": int(m.group(1).split(":")[0]), "verse": int(m.group(1).split(":")[1]), "text": m.group(2)} for m in matches]

    # count = 0
    # for m in matches:
    #     if "Ġeħova" in m.group(2):
    #         print (m.group(1), m.group(2))
    #         count += 1
    # print (count)


    for m in matches:
        print (m)
    print(result)
        
  
    # for index, _ in enumerate(match_pairs, 0): 

    #     # Check if this is the last chapter/verse pair in the list
    #     if index == number_of_verses - 1:   
    #         start = 1 + match_pairs[index][1] 
    #         # Add 1 to get rid of initial space after verse number

    #         end = len(chapter_text) # since the last pair, the end of text will be the end of the chapter
    #         verse_text = chapter_text[start:end]

    #     else:
    #         # This runs for all chapter/verse pairs if not last one 
    #         start = 1 + match_pairs[index][1]
    #         # Add 1 to get rid of initial space after verse number
    #         end = match_pairs[index + 1][0]
    #         verse_text =chapter_text[start:end]
  
    
    # return book_dict

all_chapters = get_list_of_chapters("C:/Coding/BibleTools3/Hebrew Scriptures/02-Exodus")

# print (all_chapters)
result = ""

for chapter in all_chapters:
    result += extract_chapter("C:/Coding/BibleTools3/Hebrew Scriptures/02-Exodus/" + chapter)

with open("C:/Coding/BibleTools3/exodus.txt", "w", encoding="utf8") as file:
    file.write(result)

get_chapter_dict(result)



# with open("C:/Coding/BibleTools3/matches.txt", "w", encoding="utf8") as file:
#     file.write(formatted_text)

