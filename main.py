def main():
    book_text = "books/frankenstein.txt"
    text = get_book_text(book_text)
    word_count = get_word_count(text)
    character_dict = get_character_dict(text)
    sorted_list = sort_dict(character_dict)
    print("---- Start Report for books/frankenstein.txt ----")
    print(f"There are {word_count} words in the document")
    for char_info in sorted_list:
        char = char_info[0]
        amount = char_info[1]
        print(f"The '{char}' character was found {amount:,} times")
    print("---- End of report ----")
    
def get_word_count(text):
    word = text.split()
    return len(word)

def get_book_text(book_text):
    with open("books/frankenstein.txt") as f:
        return f.read()

def get_character_dict(text):
    characters = {}
    for c in text:
        if c.isalpha():
            lower_case = c.lower()
            if lower_case in characters:
                characters[lower_case] += 1
            else:
                characters[lower_case] = 1
        else:
            pass    
    return(characters)

def sort_dict(character_dict):
    character_list = list(character_dict.items())
    character_list.sort(reverse = True, key = num_sort)
    return character_list

def num_sort(character_dict):
    return character_dict[1]

main()
