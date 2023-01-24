
If need to extract the chapter number from the text this is the syntax
re.search with group method will find the first match only. 

chapter_num_with_colon = re.search(r'\d+:|$', CHAPTER_TEXT).group()

Comment: re.search returns the colon also so need to get rid of that below
# CHAPTER_NUM = chapter_num_with_colon[:-1]