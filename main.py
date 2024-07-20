def word_count(string):
    words = string.split()
    return len(words)


def count_unique_chars(string):
    lowered_string = string.lower()
    char_counts = {}

    for char in lowered_string:
        if char not in char_counts and char.isalpha():
            char_counts[char] = 1
        elif char in char_counts:
            char_counts[char] += 1
        else:
            continue

    return char_counts




def create_dict_list(dictonary):
    dictonary_list = []

    for key in dictonary:
        dictonary_list.append(
                {'key': key, 'value': dictonary[key]})
    return dictonary_list


def sort_key(dictonary):
    return dictonary['value']


def main():
    print('---Welcome to BookBot2000---\n\n')
    with open('books/frankenstein.txt') as file:
        book_contents = file.read()

    wc = word_count(book_contents)

    print(f'There are {wc} words in this document!\n')

    unsorted_char_counts = count_unique_chars(book_contents)

    sorted_dict_list = create_dict_list(unsorted_char_counts)
    sorted_dict_list.sort(reverse=True, key=sort_key)

    sorted_char_counts = {}
    for dict in sorted_dict_list:
        sorted_char_counts[dict['key']] = dict['value']

    for char in sorted_char_counts:
        print(f'The letter "{char}" occurs {sorted_char_counts[char]} times')


main()
