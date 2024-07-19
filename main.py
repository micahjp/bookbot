def word_count(string):
    words = string.split()
    return len(words)


def main():
    with open('books/frankenstein.txt') as file:
        book_contents = file.read()

    print(word_count(book_contents))


main()
