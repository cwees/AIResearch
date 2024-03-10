# A solution to process all the files
# By: Chris He, Samer Al-Khateeb

import os
from networkExtractor import process_file


def main():
    input = os.getcwd() + "\input\\"
    missed = 0
    total = 0
    rows = 0
    user = 0
    url = 0
    hashtag = 0
    for file in os.listdir(input):
        miss, tot, data, user_count, url_count, hashtag_count = process_file(
            input + file
        )
        total = total + tot
        missed = miss + missed
        rows = data + rows
        user = user_count + user
        url = url + url_count
        hashtag = hashtag_count + hashtag

        print("------------------------------------------------")
    print(f"There were {total} total data points processed with {rows} rows")
    print(f"TOTAL Users:{user} Urls:{url} Hashtags:{hashtag}")
    print(f"{missed} incomplete data points were not processed")


if __name__ == "__main__":
    main()
