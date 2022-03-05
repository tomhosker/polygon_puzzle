"""
This code tests the Polygon class.
"""

# Test imports.
from polygon import Polygon

###########
# TESTING #
###########

def test_synaptic():
    """ Test feeding in the word "synaptic". """
    polygon = Polygon('y', ['s', 'n', 'a', 'p', 't', 'i', 'c'], "synaptic")
    expected_other_words = [
        "async",
        "city",
        "cyan",
        "cyst",
        "itsy",
        "nasty",
        "pansy",
        "panty",
        "pasty",
        "pays",
        "piny",
        "pity",
        "sanity",
        "satiny",
        "scanty",
        "spay",
        "spicy",
        "spiny",
        "stay",
        "sync",
        "tansy",
        "tiny",
        "tipsy"
    ]
    assert polygon.inner_letter == 'y'
    assert polygon.outer_letters == ['s', 'n', 'a', 'p', 't', 'i', 'c']
    assert polygon.max_letter_word == "synaptic"
    assert polygon.other_words == expected_other_words
