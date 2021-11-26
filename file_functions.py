import os

def get_chapter_list(path):
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

''' Line below for testing
print (get_chapter_list('Hebrew Scriptures/02-Exodus')) 
'''