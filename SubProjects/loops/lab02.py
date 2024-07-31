"""
Student Name: Nyasha Makaya
CS 1 22fa
Filename: lab02.py

TODO: Write a brief docstring overview of this program.
"""

import random

RNA_BASES = ["A", "U", "C", "G"]


# Section 1: For loops
def get_complement(rna_seq):
    """
    Given a string RNA sequence comprised of 'A', 'U', 'C', 'G'
    bases, returns a list representing the sequence complement.

    For example, get_complement('ACGAU') returns 
    ['U', 'G', 'C', 'U', 'A']

    Parameters:
        `rna_seq` (str) - RNA sequence string
    
    Returns:
        (list) - list of characters representing the complement.
    """
    # TODO: write your own code here alongside with a docstring

    complements = []
    for base in rna_seq:
        if base == 'A':
            complements.append('U')
        elif base == 'U':
            complements.append('A')
        elif base == 'C':
            complements.append('G')
        elif base == 'G':
            complements.append('C')
    return complements


# Section 2: range()
def search_sequence(rna_seq, segment):
    """
    TODO: write your code here, along with a docstring
    """
    for position in range(0, len(rna_seq)):
        if rna_seq[position: position + len(segment)] == segment:
            return True
            break
    return False


# Section 3: zip()
def get_similarity_score(seqA, seqB):
    """
    TODO: write your code here, along with a docstring
    """
    count = 0
    similar = 0
    for base1, base2 in zip(seqA, seqB):
        if base1 == base2:
            similar += 1

        count += 1

    similarity_score = (similar/count)# * 100
    return similarity_score
        
    


# Section 4: enumerate()
def find_close_contacts(source, infected_list):
    """
    TODO: write your code here, along with a docstring
    """
    close_contacts =[]
    for index, value in enumerate(infected_list):
        if get_similarity_score(source, value) > 0.90:
            close_contacts.append(index)
    return close_contacts

        

    return


# Section 5 (Optional): random and while
def rna_transcription(sequence, error_rate):
    """
    TODO: write your code here, along with a docstring
    """
    return


def simulate_vaccine_falloff(vaccine, sequence, error_rate):
    """
    TODO: write your code here, along with a docstring
    """
    '''
    transcriptions = 0
    complement = get_complement(vaccine)
    while search_sequence(sequence, complement) == True:

    return
    '''
