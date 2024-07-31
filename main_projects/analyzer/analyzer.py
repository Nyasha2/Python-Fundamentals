"""
Student name: Nyasha Makaya

This program provides functionality to analyze files and report statistics to users


"""

# In MP3, os must only be used to check for whether a file exists
# (which we give to you).
import os


# Exercise 1.1.
def print_fns(filename):
    """""
    Given a filename, outputs a report of any defined functions in the
    corresponding file, where a function must be defined as a valid Python
    function statement line starting with "def ".

    For example, a program containing a single function "def foo(x, y):"
    would correspond to

    foo(x, y)

    in one line of the output. Prints an error if the filename isn't found.

    Arguments:
        - `filename` (str) - name of file to analyze.

    Returns:
        - `None`
    """
    if not os.path.exists(filename):
        print(f'{filename} not found. Aborting.')
    else:
        print(f'Functions in {filename}: ')
        files = open(filename, 'r')
        for line in files:
            if 'def' in line == True:
                sentence = line
                sentence = sentence.replace('def ', '')
                sentence = sentence.replace(':','')
                print(f'    {sentence}\n')
    files.close()
        
        




        


# Exercise 1.2.
def file_info(filename):
    """
    Given a filename, analyzes the contents of the file, returning a
    dictionary with the following keys:
    - 'words' (word count of file)
    - 'lines' (line count of file)
    - 'characters' (character count of file, including '\n' characters)

    Supports any file extension, and prints an error message if the file
    isn't found.

    Arguments:
        - `filename` (str) - Name of file to analyze

    Returns:
        - (dict) - dictionary of three str keys having int count values
                   (or `None` if filename is invalid)

    """
    if not os.path.exists(filename):
        print(f'{filename} not found. Aborting.')

    else:
        # TODO 1.2: Implement function as described in spec, removing TODOs.
        files = open(filename, 'r')
        lines = 0
        words = 0
        characters = 0

        
        for line in files:
            lines += 1
            for character in line:
                characters += 1

            number_of_words = len(line.split)
            words = words + number_of_words
            
        statistics = { lines: 'lines';
            words: 'words';
            characters: 'characters';}
        
        files.close()
        return statistics

