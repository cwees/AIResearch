# A solution to process all the files
# By: Chris He, Samer Al-Khateeb

import os
from extractor import processFile


def main():
    input = os.getcwd() + "\input\\"
    for file in os.listdir(input):
        print(file)
        processFile(input + file)


main()
