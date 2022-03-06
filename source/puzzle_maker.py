"""
This code defines a class which builds a suitable polygon problem.
"""

# Standard imports.
import random

# Local imports.
import config
from polygon import Polygon
from word_arbiter import WordArbiter

##############
# MAIN CLASS #
##############

class PuzzleMaker:
    """ The class in question. """
    def __init__(self):
        self.word_arbiter = WordArbiter()
        self.polygon = self.make_polygon()

    def make_polygon(self):
        """ Make a suitable polygon object. """
        max_length_word = self.word_arbiter.get_random_max_length_word()
        decomposition = decompose_word(max_length_word)
        result = Polygon(decomposition[0], decomposition[1:], max_length_word)
        if len(result.other_words) >= config.MIN_OTHER_WORDS:
            return result
        return self.make_polygon()

    def save(self):
        """ Save the problem and the solution to their own files. """
        with open("problem.txt", "w") as problem_file:
            problem_file.write(self.polygon.get_problem_printout())
        with open("solution.txt", "w") as solution_file:
            solution_file.write(self.polygon.get_solution_printout())

    def print_to_screen(self):
        """ Print the problem and solution to the screen. """
        print(self.polygon.get_full_printout())

####################
# HELPER FUNCTIONS #
####################

def decompose_word(word):
    """ Decompose a word into a list of its letters, and scramble that list. """
    result = []
    for letter in word:
        result.append(letter)
    random.shuffle(result)
    return result
