# A solution to process all the files
# By: Chris He, Samer Al-Khateeb

import os
from networkExtractor import process_file


def main():
    input = os.getcwd() + "\input\\"
    missed = 0
    total = 0
    rows = 0
    for file in os.listdir(input):
        miss, tot, data = process_file(input + file)
        total = total + tot
        missed = miss + missed
        rows = data + rows

        print("------------------------------------------------")

    print("Finished processing all csv files.")
    print(
        "There were",
        total,
        "total data points processed with",
        rows,
        "rows of data written",
    )
    print(
        missed,
        "incomplete data points were not processed",
    )


if __name__ == "__main__":
    main()
