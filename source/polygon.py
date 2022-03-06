"""
This code defines a class which models a specific polygon and its properties.
"""

# Standard imports.
from itertools import combinations, permutations

# Local imports.
import config
from word_arbiter import WordArbiter

##############
# MAIN CLASS #
##############

class Polygon:
    """ The class in question. """
    def __init__(self, inner_letter, outer_letters, max_letter_word):
        self.inner_letter = inner_letter
        self.outer_letters = outer_letters
        self.max_letter_word = max_letter_word
        self.word_arbiter = WordArbiter()
        self.other_words = self.get_other_words()

    def get_other_words(self):
        """ Get a list of all the shorter words which also meet our
        requirements. """
        word_set = set()
        for combination in get_all_combinations(self.max_letter_word):
            for permutation in permutations(combination):
                candidate = letter_tuple_to_string(permutation)
                if (
                    (self.inner_letter in candidate) and
                    self.word_arbiter.is_a_word(candidate)
                ):
                    word_set.add(candidate)
        result = list(word_set)
        result.sort()
        return result

    def get_problem_printout(self):
        """ Get a string representation of the problem. """
        result = (
            "Inner letter: "+self.inner_letter+"\n"+
            "Outer letters: "+str(self.outer_letters)+"\n"
            "Possible words: "+str(len(self.other_words))
        )
        return result

    def get_solution_printout(self):
        """ Get a string representation of the solution. """
        result = (
            "SOLUTION\n"+
            "Max letter word: "+self.max_letter_word+"\n"
            "Other words: "+str(self.other_words)
        )
        return result

    def get_full_printout(self):
        """ Get a printout of both the problem and the solution. """
        result = self.get_problem_printout()+"\n\n"+self.get_solution_printout()
        return result

####################
# HELPER FUNCTIONS #
####################

def letter_tuple_to_string(letter_tuple):
    """ Ronseal. """
    string = ""
    for letter in letter_tuple:
        string = string+letter
    return string

def get_combinations_of_length(base_string, length):
    """ Like the below, but for a specific string length. """
    result = []
    for letter_tuple in combinations(base_string, length):
        result.append(letter_tuple_to_string(letter_tuple))
    return result

def get_all_combinations(base_string):
    """ Get all the possible combinations of letters from a string. """
    length = len(base_string)
    result = []
    for length in range(config.MIN_WORD_LENGTH, len(base_string)):
        result = result+get_combinations_of_length(base_string, length)
    return result
