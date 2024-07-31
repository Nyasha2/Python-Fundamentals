"""
Credit: Leo Jenkins
CS 1 22fa
lab03_backend.py
"""

from lab03_solution import find_word_at_location


def decode_message(message_file_path, book_file_path, output_file_path):
    memoDict = {}

    code = open(message_file_path, "r")
    output = open(output_file_path, "w")
    

    line = code.readline()
    while line:
        message = ""
        words = line.split(":")
        for word in words:
            word = word.strip("\n")
            if word != "":
                location = tuple(map(int, word.replace("(", "").replace(")", "").split(', ')))
                if location in memoDict:
                    message += memoDict[location] + " "
                else:
                    word_at_location = find_word_at_location(location, book_file_path)
                    memoDict[word] = word_at_location
                    message += word_at_location + " "
        message += "\n"
        output.write(message)
        line = code.readline()

    code.close()
    output.close()
    return message


def find_word_location(target_word, book_file_path):
    book = open(book_file_path, "r")
    chapter_count = 0
    line_count = 0
    word_count = 0

    line = book.readline()
    while line:
        line_count += 1
        words = line.strip().split(" ")
        word_count =  0
        for word in words:
            word_count += 1
            if word == "Chapter":
                chapter_count += 1
                line_count = 0
            elif word.lower() == target_word.lower():
                book.close()
                return (chapter_count, line_count, word_count)
        line = book.readline()
    book.close()
    return target_word


def encode_message(message_file_path, book_file_path, output_file_path):
    read_file = open(message_file_path, "r")
    write_file = open(output_file_path, "w")

    line = read_file.readline()

    while line:
        words = line.split(" ")
        new_line = ""
        for word in words:
            word = word.strip("\n")
            location = find_word_location(word, book_file_path)
            new_line += str(location) + ":"
        write_file.write(new_line + "\n")
        line = read_file.readline()
    read_file.close()
    write_file.close()