""" Accepts full path to Book name such as:
    C:/Coding/BibleTools3/Hebrew Scriptures/02-Exodus/Exodus 01.docx

    Returns a dictionary of the chapter in the format:
    {book_name: "Exodus", chapter_num: 2, verse_num: 1, verse_text: "text of verse"}

    Gets text from Word doc filename using the docx package
    Returns:    chapter_text = string of contents
                len of chapter_text

    Appends each para to a list since this is how to interate over file using the docx package.
    But we want a string so ... returns string converted from list and replaces /n with a space

"""
import os
import re
import docx


def get_list_of_chapters(path):
    """Takes in the  path where the chapter files live eg: 'Hebrew Scriptures/02-Exodus'
    and returns a list called chapter_list that contains the files to process.
    This function makes sure that other files that are in bible book directory are not processed.
    For example Exodus 36.Advisor.docx and and temp files. S=Funtion is commented out that allows making a backup of files
    Later on if want to backup files first then commpare can include these lines if not os.path.exists('backup'):
    os.mkdir ('backup')
    Many of these commands explained in Corey Schafter YouTube video "Automate Parsing and renaming of multiple files"
    """
    chapter_list = []
    # path should be like this: 'Hebrew Scriptures/02-Exodus'
    os.chdir(path)

    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)  # separate file name from extension

        f_parts = f_name.split(
            "."
        )  # divide filename to list on period. eg will produce ['Exodus 01', 'Revised Text', 'Advisor']

        # print (f_parts[0][0])
        if (
            len(f_parts) < 2
            and f_parts[0][0] != "~"
            and f_parts[0] != "backup"
            and f_ext == ".docx"
        ):
            # only want 1. list item with 1 item 2. No files starting with "~" and 3. Not the backup folder

            new_name = "{}{}".format(
                f_parts[0], f_ext
            )  # piece the file name together again
            chapter_list.append(
                new_name
            )  # append it to the list we want to eventually return

    return chapter_list


def get_list_of_chapters(path):
    """Takes in the  path where the chapter files live eg: 'Hebrew Scriptures/02-Exodus'
    and returns a list called chapter_list that contains the files to process.
    This function makes sure that other files that are in bible book directory are not processed.
    For example Exodus 36.Advisor.docx and and temp files. S=Funtion is commented out that allows making a backup of files
    Later on if want to backup files first then commpare can include these lines if not os.path.exists('backup'):
    os.mkdir ('backup')
    Many of these commands explained in Corey Schafter YouTube video "Automate Parsing and renaming of multiple files"
    """
    chapter_list = []
    # path should be like this: 'Hebrew Scriptures/02-Exodus'
    os.chdir(path)

    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)  # separate file name from extension

        f_parts = f_name.split(
            "."
        )  # divide filename to list on period. eg will produce ['Exodus 01', 'Revised Text', 'Advisor']

        # print (f_parts[0][0])
        if (
            len(f_parts) < 2
            and f_parts[0][0] != "~"
            and f_parts[0] != "backup"
            and f_ext == ".docx"
        ):
            # only want 1. list item with 1 item 2. No files starting with "~" and 3. Not the backup folder

            new_name = "{}{}".format(
                f_parts[0], f_ext
            )  # piece the file name together again
            chapter_list.append(
                new_name
            )  # append it to the list we want to eventually return

    return chapter_list


def count_verses(chapter_text):
    """Returns number of verses by searching colon"""

    num_of_verses_with_colon = re.findall(r":\d+", chapter_text)[-1]

    return int(
        num_of_verses_with_colon[1:]
    )  # delete colon and returned as str so need int


def extract_chapter(chapter_path: str):
    """
    Explain function
    """
    doc = docx.Document(chapter_path)
    chapter_paragraphs = []

    for _, para in enumerate(doc.paragraphs, 1):

        chapter_paragraphs.append(para.text)  # append to list

        raw_chapter_text = " ".join(chapter_paragraphs)  # Convert back to a string

        chapter_text = raw_chapter_text

    return chapter_text


def get_chapter_dict(file):
    """
    Explain function
    """

    pattern = re.compile(r"(\d+:\d+)(.+?)(?=\d+:\d+|$)")
    matches = pattern.finditer(file)
    result = [
        {
            "chapter": int(m.group(1).split(":")[0]),
            "verse": int(m.group(1).split(":")[1]),
            "text": m.group(2),
            "words_in_verse": len(m.group(2)),
        }
        for m in matches
    ]
    # Use code below if want to search occurances of particular string
    # count = 0
    # for m in matches:
    #     if "Ġeħova" in m.group(2):
    #         print (m.group(1), m.group(2))
    #         count += 1
    # print (count)

    for match in matches:
        print(match.group(1), match.group(2))
        # print(match)
    return result


"""
"""

# books_in_bible = [("02", "Exodus", 40), ("01", "Genesis", 50)]
books_in_bible = [("02", "Exodus", 40)]
base_path="/home/david/Coding/BibleTools3/Hebrew Scriptures"
chap_paths_list = []
for book in books_in_bible:
    book_fname = f"{book[0]}-{book[1]}"  # eg 02-Exodus
    chaps_in_book = book[2]  # int eg 40

    for chapter in range(1, chaps_in_book + 1):  # Start: from 1, Stop: add one since starts from zero
        chap_num_str = str(chapter).zfill(2)  # eg 02 but a string padded out 2 digits
        book_path = f"{base_path}/{book_fname}/{book[1]} {chap_num_str}.docx"
        chap_paths_list.append(book_path)
        
    
all_chapters=chap_paths_list 

# all_chapters = get_list_of_chapters(book_path)

book_text = ""
for chapter_path in all_chapters:
    book_text += extract_chapter(chapter_path)


print (get_chapter_dict(book_text))

# for a in get_chapter_dict(result):
#     for b in a:
#         print(b, "->", a[b])


# result = ""
# for chapter in all_chapters:
#     result += extract_chapter(
#         "/home/david/Coding/BibleTools3/Hebrew Scriptures/02-Exodus/" + chapter
#     )

# with open("/home/david/Coding/BibleTools3/exodus.txt", "w", encoding="utf8") as file:
#     file.write(result)

# for a in get_chapter_dict(result):
#     for b in a:
#         print(b, "->", a[b])


# with open("C:/Coding/BibleTools3/matches.txt", "w", encoding="utf8") as file:
#     file.write(formatted_text)
