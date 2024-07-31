"""
Write your information here:
Name: Nyasha
Class: CS 1
File: lab03.py
"""

[          ] # This is an example of a blank space
# Fill in all blank spaces in the following code, removing the [ ]


# Section 1: Warm-up
def relocate_file():
    """
    Copies a file from one location to another.
    In this case, rewrites a 'read.txt' file found in 
    some/subdirectory/path/... to 
    a new file in the current directory called 'write.txt'; 

    The relative path to 'read.txt' will need to be 
    determined by students to assign `filepath`.
    """
    filepath = 'users/nyashalie/Desktop/cs1/lab03_files/a/1/c/3/this/is/getting/repetitive/read.txt'
    new_filepath = 'users/nyashalie/Desktop/cs1/lab03_files'
    read_file = open(filepath, "r")
    write_file = open(new_filepath, "w")

    line = read_file.readline()

    while line:
        write_file.[          ]
        line = line + 1

    read_file.close()
    write_file.close()


# Section 2: Ransom Note
def can_hide_ransom_message(message, filepath):
    file = open(filepath, "r")
    curr = 0

    line = file.readline()

    while line:
        for char in line:
            if [          ]:
                return True
            if [          ]:
                curr += 1
        line = [          ]

    if curr >= len(message):
        return True

    file.close()
    return False


# Section 3: Skip Code
def decode_skip_code(filepath, skip_amount):
    file = [          ]
    code = file.read()
    words = code.strip().split(" ")

    decoded_string = ""

    [          ]
    
    [          ]
    return decoded_string


