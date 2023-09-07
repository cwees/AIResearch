# A solution to process all the files
# By: Chris He, Samer Al-Khateeb

import os
from networkExtractor import processFile


def main():
    input = os.getcwd() + "\input\\"
    missed = 0
    total = 0
    for file in os.listdir(input):
        miss, tot = processFile(input + file)
        total = total + tot
        missed = miss + missed
    print("Finished processing all csv files.")
    print("There were",total,"total data points processed")
    print(
        missed,
        "data points were not processed since they were incomplete",
    )


main()
