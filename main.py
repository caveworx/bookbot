def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_num = get_char_num(text)
    print(char_num)
    print(gen_report(char_num))




def get_char_num(text):
    lower_string = text.lower()
    char_count = {}
    for c in lower_string:
        if c not in char_count:
            char_count[c]= 1
        else:
            char_count[c] += 1
    return char_count


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# need to sort. lisst of dics working
def gen_report(dict):
    pre_list = []
    for key in dict:
        if key.isalpha() == True:
            new_dict = {}
            new_dict['name'] = key
            new_dict['num'] = dict[key]
            pre_list.append(new_dict)
    return pre_list
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

