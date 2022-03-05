"""
This code tests the WordArbiter class.
"""

# Test imports.
import config
from word_arbiter import WordArbiter

###########
# TESTING #
###########

def test_weird_words():
    """ Test whether some weird, but valid, words are recognised. """
    arbiter = WordArbiter()
    weird_words = [
        "antidisestablishmentarianism",
        "kerfuffle",
        "hullabaloo",
        "cacophony",
        "ragamuffin",
        "gobbledygook",
        "lackadaisical",
        "lollygagging"
    ]
    for word in weird_words:
        assert arbiter.is_a_word(word)

def test_misspellings():
    """ Test whether misspellings are identified. """
    arbiter = WordArbiter()
    misspellings = [
        "absense",
        "acceptible",
        "accomodate",
        "acknowlege",
        "aquit",
        "beatiful",
        "camoflage",
        "comitted",
        "daquiri",
        "definately",
        "disasterous",
        "embarass",
        "hygene",
        "liason",
        "milennium",
        "mispell",
        "percieve",
        "potatoe",
        "questionaire",
        "restaraunt",
        "seperate",
        "supercede",
        "tyrany",
        "withold"
    ]
    for misspelling in misspellings:
        assert not arbiter.is_a_word(misspelling)

def test_correct_spellings():
    """ Test whether spellings are identified. """
    arbiter = WordArbiter()
    spellings = [
        "absence",
        "acceptable",
        "accommodate",
        "acknowledge",
        "acquit",
        "beautiful",
        "camouflage",
        "committed",
        "daiquiri",
        "definitely",
        "disastrous",
        "embarrass",
        "hygiene",
        "liaison",
        "millennium",
        "misspell",
        "perceive",
        "potato",
        "questionnaire",
        "restaurant",
        "separate",
        "supersede",
        "tyranny",
        "withhold"
    ]
    for spelling in spellings:
        assert arbiter.is_a_word(spelling)

def test_get_random_max_length_word():
    """ Test that the random max length word is of the right length. """
    arbiter = WordArbiter()
    assert len(arbiter.get_random_max_length_word()) == config.MAX_WORD_LENGTH
