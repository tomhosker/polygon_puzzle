"""
This code defines a class which determines whether a given string is a valid
word.
"""

# Standard imports.
import random

# Local imports.
import config

# Non-standard imports.
from autocorrect import Speller
from progressbar import progressbar

##############
# MAIN CLASS #
##############

class WordArbiter:
    """ The class in question. """
    def __init__(self):
        self.word_set = self.make_word_set()

    def make_word_set(self):
        """ Make a set containing all permitted words. """
        with open(config.PATH_TO_WORD_LIST, "r") as word_list_file:
            result = set(line.strip() for line in word_list_file)
        return result

    def is_a_word(self, string_of_letters):
        """ Decide whether a given string is a valid word. """
        if string_of_letters in self.word_set:
            return True
        return False

    def get_random_word(self):
        """ Get a random word from the set. """
        result = random.choice(tuple(self.word_set))
        return result

    def get_random_max_length_word(self):
        """ Get a random word from the set of our maximum length. """
        result = self.get_random_word()
        if len(result) == config.MAX_WORD_LENGTH:
            return result
        return self.get_random_max_length_word()
