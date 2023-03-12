BIBLE_BOOKS = [
    {"name": "Genesis", "book_num": "01", "num_of_chaps": 50},
    {"name": "Exodus", "book_num": "02", "num_of_chaps": 40},
    {"name": "Leviticus", "book_num": "03", "num_of_chaps": 27},
    {"name": "Numbers", "book_num": "04", "num_of_chaps": 36},
    {"name": "Deuteronomy", "book_num": "05", "num_of_chaps": 34},
]

for book in BIBLE_BOOKS:
    print(book["name"], book["book_num"], book["num_of_chaps"])



book = BIBLE_BOOKS[0]

print(book["name"])
# 'Genesis'

print (book["book_num"])
# 1

print (book["num_of_chaps"])
# 50



base_path="/home/david/Coding/BibleTools3/Hebrew Scriptures"
chap_paths_list = []
for book in BIBLE_BOOKS:
    
    book_fname = f"{book['book_num']}-{book['name']}"  # eg 02-Exodus
    chaps_in_book = book['num_of_chaps']  # int eg 40
    print (book_fname, chaps_in_book)




BIBLE_BOOK_NAMES = [
    "Genesis",
    "Exodus",
    "Leviticus",
    "Numbers",
    "Deuteronomy",
    "Joshua",
    "Judges",
    "Ruth",
    "1 Samuel",
    "2 Samuel",
    "1 Kings",
    "2 Kings",
    "1 Chronicles",
    "2 Chronicles",
    "Ezra",
    "Nehemiah",
    "Esther",
    "Job",
    "Psalms",
    "Proverbs",
    "Ecclesiastes",
    "Song of Solomon",
    "Isaiah",
    "Jeremiah",
    "Lamentations",
    "Ezekiel",
    "Daniel",
    "Hosea",
    "Joel",
    "Amos",
    "Obadiah",
    "Jonah",
    "Micah",
    "Nahum",
    "Habakkuk",
    "Zephaniah",
    "Haggai",
    "Zechariah",
    "Malachi"
]