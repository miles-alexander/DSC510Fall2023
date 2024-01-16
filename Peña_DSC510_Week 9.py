# DSC 510
# Week 9
# Programming Assignment Week 9
# Author Miles Peña
# 10/29/2023

import string


def process_line(line, word_count_dict):
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        if word != '--':
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            add_word(word, word_count_dict)


def add_word(word, word_count_dict):
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1


def process_file(word_count_dict, filename):
    new_file = open(filename, 'a')
    value_key_list = []
    for key, val in word_count_dict.items():
        value_key_list.append((val, key))
    value_key_list.sort(reverse=True)
    new_file.write('{:11}{:11}'.format('Word', 'Count' + '\n'))
    new_file.write(' ' * 21 + '\n')
    for val, key in value_key_list:
        new_file.write('{:12s} {:<3d}'.format(key, val) + '\n')
    new_file.close()


# def pretty_print(word_count_dict):
#     value_key_list = []
#     for key, val in word_count_dict.items():
#         value_key_list.append((val, key))
#     value_key_list.sort(reverse=True)
#     print('{:11}{:11}'.format('Word', 'Count'))
#     print(' ' * 21)
#     for val, key in value_key_list:
#         print('{:12s} {:<3d}'.format(key, val))


def main():
    word_count_dict = {}
    try:
        gba_file = open("gettysburg.txt", 'r')
    except FileNotFoundError as e:
        print(e)
    for line in gba_file:
        process_line(line, word_count_dict)
    file = input("Enter the file name: ")
    filename = (file + '.txt')
    new_file = open(filename, 'w')
    new_file.write('Length of the dictionary: ' + str(len(word_count_dict)) + '\n')
    new_file.close()
    process_file(word_count_dict, filename)
    print('New File Created Successfully!')

if __name__ == "__main__":
    # execute only if run as a script
    main()
