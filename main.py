from sort_dict_by_value import sort_dictonary_by_value

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


def main():
    print('---Welcome to BookBot2000---\n\n')
    with open('books/frankenstein.txt') as file:
        book_contents = file.read()

    wc = word_count(book_contents)

    print(f'There are {wc} words in this document!\n')

    unsorted_char_counts = count_unique_chars(book_contents)

    sorted_char_counts = sort_dictonary_by_value(unsorted_char_counts)

    for char in sorted_char_counts:
        print(f'The letter "{char}" occurs {sorted_char_counts[char]} times')


main()
