"""
Student name: Nyasha Makaya

This program replaces all the tabs in a file with spaces, with the user getting
to specify the number of spaces they want each tab to be.

"""

# In MP3, os must only be used to check for whether a file exists
# (which we give to you)
import os


def tabs_to_spaces(filename, tab_length):
    """
    This functions accepts two arguments, the first one being a file name in form
    of a string, and the second one, tab_length, is an integer.
    Its function is to replace all the tabs in file <filename> and replace each tab 
    with tab_length spaces.
    The function is then supposed to write the text with replaced tabs in a new file called 
    spaced_filename, and it is not suppoed to make any changes to the original <filename>
    Finally, the function is supposed to print out the number of lines in <filename> with
    tabs, and the number of tabs replaced.

    For example;

    >>> tabs_to_spaces('math_fns.py', 4)
    Lines with tabs: 29
    Tabs replaced: 34

    >>> tabs_to spaces(two_tab_test.txt', 4)
    Lines with tabs: 1
    Tabs replaced: 2
    """
    if not os.path.exists(filename):
        print(f'{filename} not found. Aborting.')

    # TODO 2.1: Implement function as described in spec, removing TODOs here
    else:
        tab_lines, lines, tabs = 0, 0, 0

        file = open(filename, 'r')
        with open(f'spaced_{filename}', 'w') as spaced_file:

            for line in file:
                lines += 1
                if '    ' in line == True:
                    tab_lines += 1
                    line = line.replace('   ', tab_length * ' ')
                spaced_file.writelines(line)

        print(f'Lines with tabs: {tab_lines}\nTabs replaced: {tabs}')  

tabs_to_spaces('four_tab_test.txt', 2)