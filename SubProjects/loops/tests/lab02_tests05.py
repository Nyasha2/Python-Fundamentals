import random
import pytest

import sys

sys.path.insert(0, '../lab02_loops')
from lab02 import rna_transcription, simulate_vaccine_falloff

def generate_random_sequence():
    random_sequence = []
    for _ in range(10000):
        random_sequence.append(random.choice(["U", "A", "C", "G"]))
    return random_sequence

def test_rna_transcription():
    sequence = generate_random_sequence()

    counter = 0
    for _ in range(500):
        original = sequence.copy()
        rna_transcription(sequence, 10000)
        if sequence != original:
            counter += 1

    assert 300 <= counter and counter <= 334

def test_rna_transcription_long():
    sequence = generate_random_sequence()

    counter = 0
    for _ in range(1000):
        original = sequence.copy()
        rna_transcription(sequence, 10000)
        if sequence != original:
            counter += 1

    assert 615 <= counter and counter <= 650

def test_simulate_vaccine_falloff_both_empty():
    assert simulate_vaccine_falloff([], [], 0) == 0

def test_simulate_vaccine_falloff_empty_vaccine():
    assert simulate_vaccine_falloff(["U", "A", "C", "G"], [], 0) == 0

def test_simulate_vaccine_falloff():
    assert simulate_vaccine_falloff(['G', 'G', 'U', 'A', 'C', 'C', 'A', 'A'], \
        ['G', 'G', 'U', 'A', 'C', 'C', 'A', 'A', 'U', 'U', 'G', 'G', 'A', 'C', 'U', 'G', 'G', 'U', 'U', 'G'], 0) == 0

def test_simulate_vaccine_falloff2():
    sum = 0
    for _ in range(100):
        sum += simulate_vaccine_falloff(['C', 'C', 'A', 'U', 'G', 'G', 'U', 'U'], \
        ['G', 'G', 'U', 'A', 'C', 'C', 'A', 'A', 'U', 'U', 'G', 'G', 'A', 'C', 'U', 'G', 'G', 'U', 'U', 'G'], 10000)
    average = sum / 100

    assert average > 1000
