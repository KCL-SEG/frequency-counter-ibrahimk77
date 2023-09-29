"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for str(item) in items:
        if item in frequencies.keys():
            frequencies[str(item)] += 1
        else:
            frequencies[str(item)] = 1
    

    return frequencies
