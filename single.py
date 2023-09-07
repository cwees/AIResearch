# A solution to process all the files
# By: Chris He, Samer Al-Khateeb

import os
from networkExtractor import processFile


def main():
    input = os.getcwd() + "\input\\" + "bard.csv"
    processFile(input)


main()
