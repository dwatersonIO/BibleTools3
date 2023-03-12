# No longer needed since specify book paths using data from a dictionary
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

# Not used since not reliable to get number of verses based on counting colons
def count_verses(chapter_text):
    """Returns number of verses by searching colon"""

    num_of_verses_with_colon = re.findall(r":\d+", chapter_text)[-1]

    return int(
        num_of_verses_with_colon[1:]
    )  # delete colon and returned as str so need int



   # Use code below if want to search occurances of particular string
   # This was when thought would search in chapter as a string but better 
   # to search when a dictionary.
   
    # count = 0
    # for m in matches:
    #     if "Ġeħova" in m.group(2):
    #         print (m.group(1), m.group(2))
    #         count += 1
    # print (count)

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
