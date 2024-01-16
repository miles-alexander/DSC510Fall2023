# DSC 510
# Week 8
# Programming Assignment Week 8
# Author Miles Peña
# 10/19/2023

def process_line(line, word_count):
    import string
    line = line.strip()
    words = line.split()
    for word in words:
        if word != "--":
            word = word.strip()
            word = word.lower()
            word = word.strip(string.punctuation)
            add_word(word, word_count)


def add_word(word, word_count):
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1


def pretty_print(word_count):
    print("Length of the Dictionary:", len(word_count))
    print("{:<15} {:<10}".format('Word', 'Count'))
    value_key_list = []
    for key, value in word_count.items():
        value_key_list.append((value, key))
    value_key_list.sort(reverse=True)
    for value, key in value_key_list:
        print('{:<15} {:<10}'.format(key, value))


def main():
    word_count = {}
    gba_file = open("Gettysburg.txt", 'r')
    for line in gba_file:
        process_line(line, word_count)

    pretty_print(word_count)


if __name__ == "__main__":
    main()
