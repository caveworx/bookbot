def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_num = get_char_num(text)
    report_data = get_report_data(char_num)
    gen_report(book_path, num_words, report_data)



def gen_report(book_path, num_words, report_data):    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for dict in report_data:
        print(f"The '{dict['name']}' character was found {dict['num']} times")
    print('--- End report ---')

def get_char_num(text):
    lower_string = text.lower()
    char_count = {}
    for c in lower_string:
        if c not in char_count:
            char_count[c]= 1
        else:
            char_count[c] += 1
    return char_count



def get_report_data(dict):
    def sort_on(dict):
        return dict["num"]
    pre_list = []
    for key in dict:
        if key.isalpha() == True:
            new_dict = {}
            new_dict['name'] = key
            new_dict['num'] = dict[key]
            pre_list.append(new_dict)
    pre_list.sort(reverse=True, key=sort_on)
    return pre_list


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

