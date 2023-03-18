import json
from constants import BIBLE_BOOKS


def read_json_bible(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf8") as f:
        data = json.load(f)
    return data    


def add_total_verse_words(verses: dict, book_name: str) -> int: 
    total_words=0
    
    for verse in verses:
        if verse['book_name'] == book_name:
            total_words += len(verse['verse_text'].split()) # default split is on space so len with count words

    return total_words


verses = read_json_bible("/home/david/Coding/BibleTools3/result.txt")
books_to_get = list(BIBLE_BOOKS.keys())  
total_words ={}

for book in books_to_get:
    print (f'Total words in {book}: {add_total_verse_words(verses, book)}')


# total_words=0
# for book in bible:
#     total_words += book['num_words_in_verse']
        
person = {'first_name': 'Jane', 'last_name': 'Doe'}
new_dictionary = {}
for k, v in person.items():
    print (k)
    print (v)

# print (new_dictionary)