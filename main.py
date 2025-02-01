def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = (get_num_words(text))
    chars_dict = get_characters_count(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    report(chars_dict)
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words_num = len(text.split())
    return words_num

def get_characters_count(text):
    chars_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1
    return chars_dict

def sort_on(dict):
    return dict["num"]

def report(dict):
    new_list = []
    alpha_count = 0
    for c in dict:
        if c.isalpha():
            c_count = dict[c]
            new_list.append({"char": c, "num": c_count})
            alpha_count += 1
    new_list.sort(reverse=True, key=sort_on)
    for c in range(0, alpha_count):
        print(f"The '{new_list[c]['char']}' character was found {new_list[c]['num']}") 
    return

main()