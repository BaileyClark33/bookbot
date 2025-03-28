def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
    return contents

def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_data(text):
    letters = {}

    for char in text:
        c = char.lower()
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1

    return letters

def sort_characters(dict):
    sorted_list = [{'character': char, 'count': count} for char, count in dict.items()]
    sorted_list.sort(key=lambda x: x['count'], reverse=True)
    return sorted_list
