from stats import get_num_words
from stats import get_book_text
from stats import get_character_data 
from stats import sort_characters
import sys

def main():
    if len(sys.argv) < 2:
        print("Missing file path argument:")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + str(path))
    print("----------- Word Count ----------")
    text = get_book_text(path)
    print("Found " + str(get_num_words(text)) + " total words")
    print("--------- Character Count -------")
    
    character_data = sort_characters(get_character_data(text))
    for i in range(len(character_data)):
        if character_data[i]["character"].isalpha():
            print(str(character_data[i]["character"]) + ": " + str(character_data[i]["count"]))

    print("============= END ===============")

main()
