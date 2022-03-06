"""
This code is the entry point for the module as a whole.
"""

# Path voodoo.
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.resolve()/"source"))

# Local imports.
from puzzle_maker import PuzzleMaker

##############
# RUN SCRIPT #
##############

def run():
    maker = PuzzleMaker()
    maker.print_to_screen()
    maker.save()

if __name__ == "__main__":
    run()
