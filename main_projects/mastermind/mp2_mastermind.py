'''
Name: Nyasha Makaya
Assignment: Mini Project 2
'''

def make_random_code():
    '''
    This function randomly generates a four-lettered string from 6 letters
    '''
    import random
    secret_code =''
    for count in range(4):
        secret_code += random.choice(['R','G','B','Y','O','W'])
    return secret_code


def count_exact_matches(string1, string2):
    '''
    This function takes two separate strings of the same length
    and determines how many characters in the first string are 
    similar and in the same exact postion as the second string
    
    >>>count_exact_matches('RRGB', 'RWGR)
       2
    >>>count_exact_matches('GRBB', 'GRBB')
       4
    '''
    matches = 0
    for count in range(0,3):
        if string1[count] == string2[count]:
            matches += 1
    return matches

def count_letter_matches(string1, string2):
    '''
    This function takes two strings, string1 and string2, as 
    arguments and it determines the number of characters in 
    string1 are also in string2, without taking into consideration
    the position of the characters.

     >>>count_letter_matches('RYGB', 'RWRY)
       2
    >>>count_letter_matches('GRRR', 'RYWB')
       1
    '''
    list1 = list(string1)
    list2 = list(string2)
    letter_matches = 0

    for letter in list1:
        count = 0
        for character in list2:
            if letter == character:
                while count == 0:
                    count +=1
                    letter_matches += 1
                    list1.remove(character)
                else:
                    continue
    return letter_matches 

def compare_codes(code, guess):
    """
    This functions takes two arguments of the same length, code and guess, and it returns a 
    four-charactered string made up of 'b', 'w' and '-', where b means that a character is
    both code and guess on the same position, 'w' means that a character is in both strings
    but not necessarily on the same position, and - signifies a character in code that is not 
    in guess.

    >>>compare_codes('RGBW','BYBY')
       'b---'
    >>>compare_codes('GWRB', 'WWRG')
       'bbw-'
    """
    blacks = count_exact_matches(code, guess)
    whites = count_letter_matches(code, guess)
    blanks = 4 - blacks - whites
    return blacks*'b' + whites*'w' + blanks*'-'

def run_game():
    """
    This functions simulate a game in which the computer generates a random 
    four-lettered string and allows the user to guess what the code is until they 
    get it right, after which it returns the total number of trials the user made 
    and end the game.

    >>>run_game()
       New game
       Enter your guess: 'GRBY'
       Result: 'bw--'
       Enter your guess: 'GBYW'
       Result: 'bbww'
       Enter your guess: 'GBWY'
       Result: 'bbbb'
       Congratulations! You cracked the code in 3 moves!

    """
    print('New game')
    secret_code = make_random_code()
    result = 0
    moves = 1
    while result != 'bbbb':
        guess = input('Enter your guess ')
        result = compare_codes(secret_code, guess)
        print('Result: ', result)
        moves += 1
    print('Result: ', result)
    print('Congratulations! You cracked the code in {} moves!'.formart(result))


run_game()