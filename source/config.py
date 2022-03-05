"""
This code defines some configurations for the whole project.
"""

# Standard imports.
from pathlib import Path

##################
# CONFIGURATIONS #
##################

MAX_WORD_LENGTH = 8
MIN_WORD_LENGTH = 4
MIN_OTHER_WORDS = 4
PATH_TO_WORD_LIST = Path(__file__).parent.resolve()/"word_list.txt"
