# A solution to process all the files
# By: Chris He, Samer Al-Khateeb

import os
from extractor import processFile


def main():
    input = os.getcwd() + "\input\\"
    output = os.getcwd() + "\output\\"
    for file in os.listdir(input):
        print(file)
        processFile(input + file)


main()
